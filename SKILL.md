---
name: industry-stock-selection
description: Build and maintain a reproducible industry-first A-share stock research system after the user confirms an industry. Use for value-chain mapping, full-market company-pool construction, screening, company modeling, valuation, portfolio construction, and periodic refreshes; do not use for one-off stock opinions detached from industry work.
---

# Industry Stock Selection

Turn a user-confirmed industry into a maintainable investment-research project:

`industry trend -> value chain -> supply/demand and capital cycle -> profit pool -> global benchmarks -> A-share capture -> company universe -> earnings -> valuation -> risk/reward -> portfolio maintenance`

## Start by identifying the operating mode

- **New industry:** confirm the industry boundary, investable market, forecast horizon, and risk preference. Then run the data audit before substantive research.
- **Existing project:** read the project README, changelog, latest source registry, current universe, latest models, and portfolio ledger. Continue from the current stage; do not restart completed work.
- **Periodic update:** update only changed sources, forecasts, models, rankings, and decisions. Preserve prior snapshots and reasons for changes.

For a new project, copy `assets/project-template/` or run `scripts/init_project.py`. Read [workflow.md](references/workflow.md) before execution.

## Non-negotiable research rules

1. Research the industry before deep-diving individual popular stocks.
2. Keep separate judgments for a good industry, a good business, and a good stock at the current price.
3. Analyze both demand and supply. Explicitly model the capital cycle: demand, profit, capital entry, capacity, competition, ASP/margin, and ROIC.
4. Do not add revenue mechanically across a supply chain. Separate spending flow, revenue pool, gross-profit pool, operating profit, and economic profit.
5. Use global companies as demand, technology, supply, and competition anchors. Map every important global conclusion back to investable A-shares through volume, ASP, share, margin, or capital intensity.
6. The theme determines the incremental growth path, but value the entire listed company. Include non-theme businesses, debt, dilution, capex, working capital, and non-recurring profit.
7. Keep the broad mother pool stable. Excluded and watch-list companies remain in a secondary pool with explicit upgrade conditions.
8. Missing data is `NA`, not zero and not an automatic rejection. Never invent precision.
9. Tag material numbers as `Reported`, `Derived`, `Third-party Estimate`, `Agent Estimate`, or `NA`. Every Agent Estimate needs assumption, formula, source, confidence, and invalidation condition.
10. Every market price, market cap, estimate, valuation, and conclusion needs an `as_of_date`.

## User-supplied Choice data

The user manually exports Choice data. After the complete mother pool is formed, request the comprehensive dataset for **all mother-pool companies in one batch**. Exporting 100 companies costs the user about the same effort as exporting 50, while repeated requests create unnecessary work.

- Write the request in plain Chinese that a person can follow in Choice.
- Do not use JSON, API field codes, or machine-oriented parameter syntax.
- Ask once for all fields reasonably foreseeable for screening, deep dives, and valuation.
- Accept blanks as missing coverage and continue unless the missing item can materially alter the conclusion.
- Make later requests only for a newly added company, a genuinely unforeseen critical field, or a scheduled whole-pool refresh.

Read [data-and-choice.md](references/data-and-choice.md) before requesting or ingesting data.

## Stage gates

- Do not screen stocks before the industry map and profit-pool map are usable.
- Do not request Choice data before the mother pool and ticker list are complete.
- Do not confuse a high thematic score with whole-company quality.
- Do not build final target prices from consensus alone. Consensus is a coordinate; Bear/Base/Bull must be driven by business variables.
- Do not force a fixed number of companies. Narrow only when evidence supports it.
- Do not let share-lot constraints or a desire to stay fully invested distort sector allocation. Cash is an explicit portfolio position.

Read [screening-and-modeling.md](references/screening-and-modeling.md) for scoring, company analysis, and valuation.

## Sources and evidence

Use this priority unless the task provides a stronger reason:

`regulatory filing > company IR/call/investor day > customer/supplier/competitor disclosure > official/industry association > authoritative industry research > broker research > high-quality media > social media`

Cross-check important claims through customers, suppliers, competitors, or adjacent value-chain nodes. Store source metadata before using the evidence in a conclusion. Read [deliverables.md](references/deliverables.md) for required files and schemas.

## Interaction and stopping rules

After the user confirms the initial scope and data-audit result, proceed autonomously. Interrupt only when:

- missing private or paid data could materially change stock selection, earnings, or valuation;
- authoritative primary sources materially conflict;
- a user choice would change the project scope or risk posture;
- continued work would be large and clearly low value.

Do not ask for confirmation at every phase. Record assumptions and keep moving.

## Maintenance

For a live portfolio, read [maintenance.md](references/maintenance.md). Maintain industry, company, and portfolio loops separately. Do not trade merely to restore neat weights, and do not manufacture daily actions when nothing material changed.

Before final delivery, read [failure-modes.md](references/failure-modes.md) and perform the checks there. For a concrete example of how the method evolved, read [ai-case-lessons.md](references/ai-case-lessons.md).
