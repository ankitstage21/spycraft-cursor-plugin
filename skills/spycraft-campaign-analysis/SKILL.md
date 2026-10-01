---
name: spycraft-campaign-analysis
description: Analyze connected advertising metrics, period changes, creative fatigue, and combination insights. Use for campaign reviews and performance questions.
---

# Campaign analysis

1. Check `health_check`, then `list_adaccounts`. Select the account requested by the
   user; confirm ambiguous choices. Record currency, timezone, attribution context,
   exact period, and comparison period where available. Mark unavailable context explicitly.
2. Inspect `get_metrics` schema. The inspected backend describes Meta metrics;
   do not promise Google metric support without the live tool confirming it.
   Request only relevant metrics and breakdowns for an authorized account.
3. Normalize dates explicitly. Compare equal-length periods and avoid silently comparing
   an incomplete current day to a full day. Preserve metric definitions and denominators.
4. Use `get_fatigue_diagnosis` and `get_combination_insights` if available and relevant.
   Validate their date scope and evidence before combining them with other results.
5. Compute CPA as spend/conversions and ROAS as attributed revenue/spend only when
   these inputs are compatible. For zero denominators, report undefined, not zero.
   Distinguish percentage-point changes from relative percentage changes.
6. Explain the largest evidence-backed shifts and confounding factors. Present budget,
   targeting, and creative changes as recommendations; this workflow does not execute them.

Deliver: account/date/context, metric table with comparison, key findings with underlying
values, prioritized recommendations, and missing data. Do not call missing data a tracking failure.

## Shared operating contract

Read `../../docs/OPERATING-CONTRACT.md` relative to this skill before using Spycraft.
Discover the connected server's current tool schemas; the source tool list is a snapshot,
not proof that every tool is deployed or available to this account. Use actual tool names
and arguments returned by the client. Never invent data when a tool is missing or fails.
