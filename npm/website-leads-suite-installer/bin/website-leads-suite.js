#!/usr/bin/env node
"use strict";

const { spawnSync } = require("node:child_process");
const process = require("node:process");

const REPOSITORY = "https://github.com/Lesleykaps/website-leads-suite.git";
const MARKETPLACE = "cipher-technologies";
const PLUGIN = "website-leads-suite";

function usage(exitCode = 0) {
  const output = `
Website Leads Suite installer

Usage:
  npx @ciphertechnologies/website-leads-suite <codex|claude> [--yes]

Examples:
  npx @ciphertechnologies/website-leads-suite codex
  npx @ciphertechnologies/website-leads-suite claude --yes

This installer adds the Cipher Technologies marketplace and installs Website Leads Suite.
It never runs research or contacts any business.\n`;
  (exitCode === 0 ? process.stdout : process.stderr).write(output);
  process.exit(exitCode);
}

function executable(name) {
  // Codex is commonly installed as a .cmd shim on Windows, while the Claude
  // installer supplies claude.exe. Let cmd.exe resolve the right extension.
  return name;
}

function run(command, args) {
  const options = {
    stdio: "inherit",
    shell: false
  };
  // Node cannot directly launch a Windows .cmd wrapper. Invoke cmd.exe explicitly
  // with fixed, validated arguments instead of enabling a shell for spawnSync.
  const result = process.platform === "win32"
    ? spawnSync(process.env.ComSpec || "cmd.exe", ["/d", "/c", [executable(command), ...args].join(" ")], options)
    : spawnSync(executable(command), args, options);
  if (result.error && result.error.code === "ENOENT") {
    throw new Error(`${command} was not found. Install ${command === "codex" ? "Codex CLI/Desktop" : "Claude Code"} first, then run this command again.`);
  }
  return result.status === 0;
}

function confirm() {
  if (process.argv.includes("--yes")) return Promise.resolve(true);
  if (!process.stdin.isTTY) {
    return Promise.resolve(false);
  }
  process.stdout.write("This will configure a marketplace and install Website Leads. Continue? [y/N] ");
  return new Promise((resolve) => {
    process.stdin.setEncoding("utf8");
    process.stdin.once("data", (value) => resolve(/^y(es)?$/i.test(String(value).trim())));
  });
}

async function main() {
  const target = process.argv.slice(2).find((argument) => !argument.startsWith("-"));
  if (!target || process.argv.includes("--help") || process.argv.includes("-h")) usage();
  if (!["codex", "claude"].includes(target)) {
    process.stderr.write("Choose either 'codex' or 'claude'.\n");
    usage(1);
  }

  if (!(await confirm())) {
    process.stdout.write("Cancelled. No changes were made.\n");
    process.exit(0);
  }

  const marketplaceArgs = target === "codex"
    ? ["plugin", "marketplace", "add", REPOSITORY, "--ref", "main"]
    : ["plugin", "marketplace", "add", "Lesleykaps/website-leads-suite"];
  const pluginArgs = target === "codex"
    ? ["plugin", "add", `${PLUGIN}@${MARKETPLACE}`]
    : ["plugin", "install", `${PLUGIN}@${MARKETPLACE}`];
  const refreshArgs = target === "codex"
    ? ["plugin", "marketplace", "upgrade", MARKETPLACE]
    : ["plugin", "marketplace", "update", MARKETPLACE];

  process.stdout.write(`\nAdding the ${MARKETPLACE} marketplace…\n`);
  const marketplaceAdded = run(target, marketplaceArgs);
  if (!marketplaceAdded) {
    process.stdout.write("Marketplace add returned a message. It may already be configured; continuing with installation.\n");
  }

  process.stdout.write("Refreshing the marketplace…\n");
  if (!run(target, refreshArgs)) {
    throw new Error("Website Leads marketplace could not be refreshed. Check the marketplace command output above and try again.");
  }

  process.stdout.write("Installing Website Leads Suite…\n");
  if (!run(target, pluginArgs)) {
    throw new Error("Website Leads Suite could not be installed. Check the marketplace command output above and try again.");
  }

  const invoke = target === "codex" ? "$website-leads-suite" : "/website-leads-suite:website-leads";
  process.stdout.write(`\nInstalled successfully. In a new ${target === "codex" ? "Codex" : "Claude Code"} chat, use ${invoke}.\n`);
}

main().catch((error) => {
  process.stderr.write(`\nInstallation failed: ${error.message}\n`);
  process.exit(1);
});
