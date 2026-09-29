## game.highlight-span

## English

**Highlight the sentence.** Problem: The evidence is buried in a paragraph, and the player only memorizes the conclusion.

**When:** A passage of about 120 characters or fewer, and one sentence in it supports or overturns the prompt's claim.

**When not:** The whole passage is evidence, or none of it is.

**Steps:**

1. Cut tappable sentences into `<button>` elements. Do not ask the player to drag-select free text. That is unstable on a phone.
2. A hit: highlight it and say why this sentence counts. A miss: say this sentence is atmosphere, retelling, or fiction.
3. If two sentences are both right, the brief says "select all."
4. Do not use color as the only sign that "this sentence is evidence."

**Don't:** A whole long article as one round, with hit areas stacked so a tap cannot land.

**Example:** Sitewright has not used this yet. The highlight-the-claim pattern common in news interactives.

---

## 中文

**划出那一句.** 问题：证据埋在段落里，玩家只背结论。

**何时用:** 一段不超过约 120 字，其中有一句能支撑或推翻题干主张。

**何时不用:** 整段都是证据，或整段都不是。

**步骤:**

1. 可点的句切成 `<button>`。不要让玩家在自由文本里拖选，移动端不稳。
2. 点对：高亮并说明这句为什么算数。点错：说明这句是气氛、转述或文艺。
3. 若有两句都对，简报写明「点全」。
4. 不要用颜色当唯一的「这句是证据」。

**反例:** 整篇长文当一局，句与句的热区叠在一起点不中。

**实例:** Sitewright 尚未用过。新闻互动里常见的 highlight-the-claim。
