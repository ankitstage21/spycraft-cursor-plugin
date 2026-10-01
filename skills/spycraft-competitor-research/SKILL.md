---
name: spycraft-competitor-research
description: Research competitor brands, ad examples, creative patterns, and industry trends using Spycraft. Use for competitor comparisons and ad-library research.
---

# Competitor research

1. Capture the target brands, market, product, research question, and period. Use the
   user's named brands; ask only for missing choices that change the result.
2. Check connection with `health_check`. Resolve each brand using `search_brand` or
   `list_followed_brands`, keeping exact `page_id` values. Resolve ambiguous brands before fetching.
3. Fetch the relevant `get_recent_ads`, `get_ads`, `get_top_performing_ads`,
   `fetch_brand`, or `get_brand_analysis_section` data. Keep limits modest and paginate
   only to the depth needed. A page of ten examples is not an exhaustive brand audit.
4. If `not_followed` is returned, explain what following/requesting the brand changes.
   Use `follow_brand` or `request_competitor_brand` only when the user has authorized that action.
   For pending brand analysis, poll the same brand; if marked stuck, report it.
5. Group observed hooks, offers, formats, proof devices, and landing destinations.
   Show public ad images or video poster frames and direct source links when available.
   Competitor longevity, engagement, and tool rankings are proxies, not verified ROAS.
6. Separate observed findings from test ideas. Do not infer targeting, spend, revenue,
   conversion rates, or audience demographics without returned evidence.

Deliver: scope/date/coverage, evidence table (brand, ad ID/link, hook, offer, format,
proxy used), repeated patterns, three differentiated test ideas, and data limitations.

## Shared operating contract

Read `../../docs/OPERATING-CONTRACT.md` relative to this skill before using Spycraft.
Discover the connected server's current tool schemas; the source tool list is a snapshot,
not proof that every tool is deployed or available to this account. Use actual tool names
and arguments returned by the client. Never invent data when a tool is missing or fails.
