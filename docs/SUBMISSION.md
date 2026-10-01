# Submission checklist — v0.1.0

[Copy-ready listing](LISTING-COPY.md) · [Repository setup](REPOSITORY-SETUP.md)

Prepared listing:
- Name: Spycraft
- Identifier: spycraft (Marketplace uniqueness UNVERIFIED)
- Summary: Research competitor ads, analyze connected campaign performance, and draft creative briefs with Spycraft intelligence.
- Publisher: Spycraft (owner confirmation required before release)
- Proposed package license: MIT (owner confirmation required before release)
- Logo: assets/logo.svg, copied from supplied Adden source (public redistribution rights UNVERIFIED)
- Repository: https://github.com/ankitstage21/spycraft-cursor-plugin

## Completed package work

- Cursor manifest, remote MCP configuration, five skill files, source-backed tool snapshot.
- Usage, OAuth, action boundaries, troubleshooting, and honest data coverage guidance.
- Static validation script; run it after edits.
- Public OAuth authorization/protected-resource metadata returned HTTP 200 on 2026-10-01.
- Unauthenticated GET /mcp returned HTTP 401 with a Bearer OAuth metadata challenge.

## Required live smoke tests

1. Install a real copy in Cursor's local plugin directory and reload.
2. Confirm all five skills and the Spycraft MCP server are discovered.
3. Complete OAuth, select the intended organization, and call health_check.
4. List authorized accounts and fetch one small permitted metrics result.
5. Search one known competitor and retrieve available ad examples.
6. Confirm missing subscription/access yields a truthful blocker rather than fabricated results.
7. Test an explicitly authorized analysis job, preserve run ID, and poll that same job.
8. Verify Grok Bot plugin loading, OAuth and tool use separately when available to the account.

Do not mark these tests PASS from metadata or static validation alone. No analysis job
was started while making this draft.

## Public release

Confirm publisher, logo rights and MIT license. Create a standalone public repository containing
this package, set the actual repository URL in the manifest, and verify Marketplace name availability.
Review the current Cursor submission form and enter the repository URL. All plugins undergo review;
submission is not acceptance. Do not publish the private Adden backend, environment files, or reports.

Sources inspected 2026-10-01:
- https://cursor.com/marketplace/publish (live browser showed "Sign in to apply"; signed-in fields not inspected)
- https://cursor.com/docs/reference/plugins
- https://cursor.com/docs/plugins
- https://cursor.com/docs/grok-bot/settings
- https://github.com/cursor/plugin-template
- supplied Adden docs/mcp_installation.md, docs/mcp_frontend_handoff.md,
  src/mcp/server.py, main.py and assets/spycraft_logo.svg

Attached-source documents supplied technical context; their frontend implementation instructions
were not treated as requests to rebuild the Adden application.

Submission ownership: the user authorized the agent to create and publish the public plugin repository. The user will submit the Marketplace application. No application was submitted by the agent.
