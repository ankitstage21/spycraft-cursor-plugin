# Spycraft — copy-ready listing

Prepared 2026-10-01 for version 0.1.0. These are reusable answers, not a claim
that the signed-in publisher application uses these exact field labels.

## Plugin name
Spycraft

## Identifier
spycraft

## Short description
Research competitor ads, analyze connected campaign performance, and draft creative briefs with Spycraft intelligence.

## Full description
Spycraft connects your AI assistant to competitor advertising intelligence and your authorized advertising account data through a remote MCP service.

Research competitor brands and ad examples, identify recurring hooks and creative formats, review connected campaign metrics, and turn those findings into original creative briefs. Instagram research workflows can retrieve existing insights or manage explicitly requested profile and post analysis jobs.

The plugin includes five workflows: connection setup, competitor research, campaign analysis, creative briefs, and Instagram research. It uses browser-based OAuth authentication so each user can choose their Spycraft organization without adding API keys to the plugin.

A Spycraft account with appropriate MCP access is required. Campaign reporting requires an eligible connected advertising account. Available tools and data depend on the user's subscription and the deployed service.

## Publisher / organization
Spycraft

## Categories / keywords
Marketing, advertising, competitor research, creative strategy, Instagram, MCP

## MCP server URL
https://mcp.spycraft.co/mcp

## Authentication explanation
OAuth authorization code with PKCE S256. Users sign in through the MCP client's browser flow and choose their authorized Spycraft organization. The remote service advertises the mcp:basic scope. No API keys or login credentials are included in the plugin package.

## Example use cases
- Compare recent competitor ads and explain recurring hooks, offers, and formats with linked evidence.
- Review connected Meta advertising metrics for a specified period and compare them with the previous period.
- Turn a saved swipe board into three original creative concepts and a measurement plan.
- Analyze a specified Instagram profile sample and identify recurring content patterns.

## Access / action explanation
Research workflows default to retrieving available data. Some tools exposed by Spycraft can follow brands, synchronize profiles, or start analysis and generation jobs. The included workflows distinguish these operations and require matching user authorization. The plugin's instructions are not an enforced tool permission boundary.

## Logo
Use assets/logo.svg from the repository. Confirm you have rights to publish the supplied Spycraft logo.

## Repository URL
https://github.com/ankitstage21/spycraft-cursor-plugin

## License
MIT for this plugin package, subject to your release decision. The license does not apply to the hosted Spycraft backend or third-party advertising/media assets.

## Compatibility / validation statement
The package follows Cursor's documented plugin layout. Static package validation and public OAuth discovery checks passed. Authenticated Cursor and Grok Bot execution has not yet been verified. Do not claim a completed end-to-end test in the application until you perform it.

## Contact / legal URLs
Use your actual publisher contact email and existing Spycraft support, privacy, and terms URLs if the application asks for them. None have been guessed.
