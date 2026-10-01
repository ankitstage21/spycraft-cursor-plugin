---
name: spycraft-instagram-research
description: Analyze Instagram profiles, posts, hooks, and formats using existing Spycraft results or explicitly requested analysis jobs. Use for Instagram research and content strategy.
---

# Instagram research

1. Capture the exact username or post URL, research question, and requested sample.
   Check connection and prefer existing results via `list_instagram_analyses`,
   `get_tracked_profile_overview`, `get_tracked_profile_formats`, or
   `search_instagram_posts` when they satisfy the request.
2. If new analysis is needed, verify the current trigger tool schema and entitlement.
   Starting analysis creates server work and may consume subscription allowance.
   A direct user request to analyze the specified profile/post authorizes that matching job
   within known limits; do not start extra sync, generation, or brand-following work implicitly.
   Unknown charges or jobs beyond the authorized scope require clarification.
3. Use `trigger_instagram_profile_analysis` or `trigger_instagram_post_analysis` as
   appropriate. Save the returned `run_id` immediately, then poll the corresponding
   `get_instagram_profile_analysis` or `get_instagram_post_analysis` for that run.
   Honor `poll_after_seconds`/retry metadata. Never retrigger because the run is slow.
4. For pending, failed, or partial responses, report the exact state and keep the run ID.
   Do not claim the analysis completed or synthesize unseen posts.
5. Analyze observed hook, format, pacing, offer, proof, and engagement. Engagement is
   not sales performance; a small recent sample is not the account's full history.

Deliver sample size/period/status, linked examples, repeatable patterns, three original
content ideas, limitations, and the run ID for any submitted job.

## Shared operating contract

Read `../../docs/OPERATING-CONTRACT.md` relative to this skill before using Spycraft.
Discover the connected server's current tool schemas; the source tool list is a snapshot,
not proof that every tool is deployed or available to this account. Use actual tool names
and arguments returned by the client. Never invent data when a tool is missing or fails.
