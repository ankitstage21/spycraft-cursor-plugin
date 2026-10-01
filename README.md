# Spycraft

Plan Instagram and TikTok content marketing, develop original hooks and scripts, and
research Meta ad creative with dedicated agents and Spycraft's remote MCP service.

Version **0.2.0 — submission candidate**. Package checks pass; authenticated Cursor/Grok Bot
execution is not yet verified. This package contains workflows and connection configuration;
Spycraft runs the backend. It does not contain the Adden application or credentials.

## Dedicated agents

| Agent | Responsibility |
|---|---|
| Content Strategist | Instagram and TikTok content pillars, concepts, calendars and learning plans |
| Hooks & Scripts | Original opening hooks, short-form scripts, shot direction, captions and variants |
| Meta Ads Strategist | Competitor ad research, first-party creative insights and paid creative test plans |

Agent definitions live in `agents/` and are registered in the manifest. They can share structured
briefs where the client supports delegation; they do not automatically create persistent Bots.
TikTok creative planning is included. Direct TikTok data retrieval is not established by the current
Spycraft tool snapshot; research uses supplied examples or available public browsing.

## Included workflows

| Skill | Use it for |
|---|---|
| spycraft-connect | OAuth setup and access troubleshooting |
| spycraft-competitor-research | Brand comparisons, ad examples, creative patterns |
| spycraft-campaign-analysis | Connected metrics, period comparisons, fatigue |
| spycraft-creative-brief | Original concepts and test plans grounded in research |
| spycraft-instagram-research | Profile/post analysis and content patterns |

## Requirements and authentication

Use a current Cursor or Grok Bot client with plugin and HTTP MCP OAuth support.
A Spycraft organization with appropriate MCP entitlement is required; campaign analysis
also requires an eligible connected ad account. Specific availability depends on your plan
and the deployed server. Start with `spycraft-connect` to verify access.

The package connects to `https://mcp.spycraft.co/mcp`. Sign in through the client's browser
flow, choose your organization, and approve the connection. No API key belongs in this repository.
Public metadata advertises `mcp:basic` and PKCE S256. That alone does not verify user login.

## Test locally in Cursor

Copy this directory's contents into `~/.cursor/plugins/local/spycraft/`, preserving hidden
`.cursor-plugin/` files. Restart Cursor or run **Developer: Reload Window**. Open **Customize**
and confirm all three agents, five skills and the Spycraft MCP server. Local plugin imports must be allowed
by your organization. Use a real directory; Cursor skips symlinks pointing outside its local folder.

Ask: "Use spycraft-connect to verify my organization and list my eligible ad accounts."
Then test a retrieval for an account or brand you are authorized to access.
No local installation was performed when this draft was created.

## Grok Bot

Cursor's Grok Bot documentation describes Marketplace and Yours under plugin settings.
Once the plugin is available to your account, install/connect Spycraft there, complete browser
login, and verify tool access. Desktop-local Cursor testing does not prove Grok Bot cloud access.
This draft has not been installed in Grok Bot, and private/custom import availability is unverified.

## Example requests

- "Compare the recent creative patterns of these three brands; cite the ad examples."
- "Review last month's Meta campaign performance against the previous month."
- "Turn my saved swipe board into three original creative briefs for this product."
- "Analyze this Instagram profile's five recent posts and explain the recurring hooks."

These workflows default to retrieval. Some server tools can follow brands, sync profiles,
start analysis, or generate content. The skills distinguish those actions and require matching
user authorization; instructions are not a technical tool-permission lock.

## Validate and submit

[Copy-ready listing](docs/LISTING-COPY.md) · [Public repository setup](docs/REPOSITORY-SETUP.md)


Run `python3 scripts/validate.py` from the plugin directory. Review
[the submission checklist](docs/SUBMISSION.md) and complete the authenticated smoke tests.
Push the contents as a standalone public Git repository, then submit its repository link at
[Cursor's publishing page](https://cursor.com/marketplace/publish).

The MIT license is a proposed license for this plugin package. Confirm publisher identity,
rights to the supplied logo, and license before public release. Backend services and third-party
ad/media content retain their own terms; this license does not grant rights to them.

[Cursor plugin reference](https://cursor.com/docs/reference/plugins) ·
[Grok Bot plugins settings](https://cursor.com/docs/grok-bot/settings)
