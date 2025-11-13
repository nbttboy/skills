---
name: Investment Advisor
description: This skill provides comprehensive guidance for investment analysis and decision-making, covering 10 core strategies including market trend judgment, risk assessment, position management, and information source management. It should be used when the user needs structured advice or tools related to investment trading, portfolio optimization, or financial strategy.
---

# Investment Advisor Skill - 投资顾问技能

## Purpose

本技能库旨在为Claude Code提供一个结构化的投资策略知识库，帮助用户进行投资决策分析与建议、风险评估与仓位管理、市场趋势判断、交易策略制定以及投资组合优化。

**核心理念**: 尽所能，敬所不能 —— 把握可控，敬畏未知。

## When to use this skill

This skill should be used when:
- The user asks for advice or analysis on investment opportunities.
- The user needs help with formulating a trading strategy.
- The user wants guidance on risk management or position sizing.
- The user is looking for tools or concepts related to portfolio optimization.
- The user needs to evaluate a potential investment target or an existing holding.
- The user is asking about managing information sources for investment decisions.

## How to use this skill

This skill encompasses 10 core investment strategies (SKILL-01 to SKILL-10), each detailed with definitions, core concepts, practical examples, and key checkpoints.

### General Usage Guidelines for Sub-Skills:

1.  **识别用户场景 (Identify User Scenario):** Determine if the user is in the phase of discovering opportunities, building positions, holding, or exiting. Match the scenario to the relevant skill combinations provided in the "综合应用指南" (Comprehensive Application Guide).
2.  **提供结构化建议 (Provide Structured Advice):**
    *   **引用相关技能编号 (Reference Skill ID):** Always cite the relevant `SKILL-XX` when providing advice (e.g., "根据SKILL-01确定性投资策略...").
    *   **给出具体操作步骤 (Provide Specific Steps):** Based on the skill's methodologies, outline actionable steps.
    *   **提醒风险控制要点 (Highlight Risk Control):** Emphasize risk management principles relevant to the advice given.
3.  **个性化调整 (Personalize Guidance):** Consider the user's risk tolerance, capital size, and investment experience.
4.  **强调免责 (Emphasize Disclaimer):** Remind the user that investment involves risks and advice is for reference only; independent judgment is crucial.
5.  **持续学习 (Continuous Learning):** Use user feedback to refine and update the skill knowledge base.

### Sub-Skills Index & Reusable Contents:

Below is an index of the core investment strategies within this skill, along with guidance on how to use their associated reusable contents (scripts, references, and assets).

#### SKILL-01: 确定性投资策略 (Deterministic Investment Strategy)
*   **Purpose:** Operating only in high-certainty investment opportunities.
*   **When to Use:** When evaluating the certainty of an investment, managing leverage, or defining risk control principles.
*   **Reusable Contents:**
    *   `scripts/skill_01_risk_management.py`: Use this script to calculate and get actions/notes for risk management based on market volatility and position profit.
    *   `references/skill_01_deterministic_strategy_concepts.md`: Reference this file for detailed concepts on certainty identification and the leverage management matrix.

#### SKILL-02: 标的选择能力 (Target Selection Ability)
*   **Purpose:** Selecting market-leading targets with inimitable moats.
*   **When to Use:** When evaluating potential investment targets, using the "Number One + Unique" criteria, or applying the selection decision tree.
*   **Reusable Contents:**
    *   `references/skill_02_target_selection_concepts.md`: Reference this file for detailed criteria, judgment dimensions, and the selection decision tree.
    *   `assets/target_evaluation_template.md`: Use this template to create a structured scorecard for evaluating investment targets.

#### SKILL-03: 仓位管理与市场适应 (Position Management and Market Adaptation)
*   **Purpose:** Synchronizing with market trends through phased entry, dynamic adjustments, and strict stop-losses.
*   **When to Use:** When planning position entry (军队调度建仓法), managing existing positions, or determining stop-loss triggers.
*   **Reusable Contents:**
    *   `scripts/skill_03_stop_loss_decision.py`: Use this script to determine if a stop-loss should be executed based on price movements and market trends.
    *   `references/skill_03_position_management_concepts.md`: Reference this file for the "Army Deployment Entry Method," position management rules, and adding to positions timing.

#### SKILL-04: 抄底四要素 (Four Elements of Bottom-Fishing)
*   **Purpose:** Lowering costs and expanding profit margins during market downturns.
*   **When to Use:** When planning to buy during market corrections, designing price gaps, or implementing phased buying strategies.
*   **Reusable Contents:**
    *   `references/skill_04_bottom_fishing_concepts.md`: Reference this file for detailed principles on price gap design, phased buying, position reservation, and diversification, along with the bottom-fishing checklist.

#### SKILL-05: 定投策略应用 (Regular Investment Strategy Application)
*   **Purpose:** Reducing market timing difficulty through periodic fixed-amount investments.
*   **When to Use立刻:** When setting up a regular investment plan, adjusting investment amounts based on valuation, or considering market timing for periodic investments.
*   **Reusable Contents:**
    *   `scripts/skill_05_valuation_model.py`: Use this script to calculate fair valuation and determine investment actions (increase, pause, normal).
    *   `references/skill_05_regular_investment_concepts.md`: Reference this file for detailed considerations on valuation judgment, timing selection, and combining with price gaps.
    *   `assets/regular_investment_plan_template.md`: Use this template to generate a structured regular investment plan for the user.

#### SKILL-06: "控成本、撑空间"策略 ("Control Cost, Expand Space" Strategy)
*   **Purpose:** Maintaining stable psychology by lowering holding costs and expanding profit margins for long-term holding.
*   **When to Use:** When actively managing positions during uptrends or oscillations to reduce cost basis and improve psychological holding power.
*   **Reusable Contents:**
    *   `references/skill_06_cost_space_strategy_concepts.md`: Reference this file for detailed methods on operations during uptrends, swing trading for cost reduction, and building psychological space.
    *   `assets/holding_management_plan_template.md`: Use this template to create a structured holding management plan.

#### SKILL-07: 趋势终结判断 (Trend Termination Judgment)
*   **Purpose:** Identifying signals for the end of a profitable trend to exit trades promptly.
*   **When to Use:** When assessing whether a market trend is ending, using technical or fundamental indicators, or planning exit strategies.
*   **Reusable Contents立刻:**
    *   `references/skill_07_trend_termination_concepts.md`: Reference this file for detailed core judgment dimensions (technical, fundamental), the decision matrix, and phased exit strategies.

#### SKILL-08: 耐心修炼 (Patience Cultivation)
*   **Purpose:** Developing investment patience to identify and seize major opportunities, avoiding frequent trading.
*   **When to Use:** When guiding the user on improving investment discipline, managing emotions during market fluctuations, or training for a "hunter's mindset."
*   **Reusable Contents:**
    *   `references/skill_08_patience_cultivation_concepts.md`: Reference this file for details on the hunter mindset, levels of patience, and patience training methods.

#### SKILL-09: 投资纪律坚守 (Investment Discipline Adherence)
*   **Purpose:** Establishing and strictly adhering to investment discipline, especially profit-taking mechanisms.
*   **When to Use:** When helping the user establish personal investment rules, enforce stop-loss/profit-taking, or analyze the difference between rational investing and gambling.
*   **Reusable Contents:**
    *   `references/skill_09_discipline_adherence_concepts.md`: Reference this file for detailed mechanisms for profit-taking, stop-loss, position sizing, and trading action discipline.
    *   `assets/investment_commitment_letter.md`: Use this template to generate an investment commitment letter.
    *   `assets/discipline_execution_checklist.md`: Use this template to generate a monthly discipline execution checklist.

#### SKILL-10: 信息源管理 (Information Source Management)
*   **Purpose:** Establishing a diversified, high-quality information system to avoid information cocoons and maintain independent judgment.
*   **When to Use:** When advising the user on building reliable information sources, evaluating information quality, or avoiding common information traps.
*   **Reusable Contents立刻:**
    *   `references/skill_10_info_source_management_concepts.md`: Reference this file for details on building an information system, CREAM evaluation, processing flow, and avoiding information traps.
    *   `assets/info_source_checklist_template.md`: Use this template to generate a personal information source checklist.

---

## Appendices

### A. Core Concepts Quick Reference
`references/core_concepts_quick_reference.md`

### B. Common Formulas Summary
`references/common_formulas_summary.md`

### C. Practical Tools List
`references/practical_tools_list.md`

### D. Recommended Reading List
`references/recommended_reading_list.md`

---

## Disclaimer

This skill content is for learning and reference only and does not constitute any investment advice. Investment involves risks, and market entry requires caution. Any investment decisions should be based on personal independent judgment and consider one's own risk tolerance.

**核心原则**:
- 尽所能：把握自己能掌控的
- 敬所不能：敬畏市场和社会的不确定性
- 万物皆周期：没有永远的云端
- 长期主义：在春风得意时布局，平淡了才有退路

---

*Last Updated: November 2024*
*Applicable Scenario: Claude Code Investment Analysis and Advice*
*Continuous optimization...*
