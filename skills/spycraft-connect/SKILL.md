---
name: spycraft-connect
description: Connect and troubleshoot Spycraft OAuth and organization access. Use when setting up Spycraft or diagnosing authentication, subscription, or connection errors.
---

# Connect Spycraft

1. Check whether the client exposes the Spycraft MCP server configured at
   `https://mcp.spycraft.co/mcp`. If missing, explain installation using the README.
2. Call `health_check`. If the client requests OAuth, let the user sign in through
   the client's browser flow and choose the intended organization. Never ask for passwords,
   access tokens, or refresh tokens in chat or files.
3. Verify authentication from the tool result. Call `list_adaccounts` only when
   the user needs campaign access. Record the actual organization and available accounts.
4. Report three states separately: plugin loaded, OAuth authenticated, and requested
   data accessible. A metadata HTTP 200 only proves discovery is reachable.
5. For unauthorized/invalid-token errors, request client reauthentication. For forbidden
   or insufficient-scope errors, explain entitlement/access limits. Empty accounts do not
   mean zero advertising spend. For rate limits, respect the returned retry delay.

Deliver a concise connection receipt with verified state, requested scope, and any blocker.

## Shared operating contract

Read `../../docs/OPERATING-CONTRACT.md` relative to this skill before using Spycraft.
Discover the connected server's current tool schemas; the source tool list is a snapshot,
not proof that every tool is deployed or available to this account. Use actual tool names
and arguments returned by the client. Never invent data when a tool is missing or fails.
