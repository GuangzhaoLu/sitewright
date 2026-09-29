## game.pattern-cell

## English

**Complete the pattern.** Problem: A visual rule is taught as a definition, and the reader never has to continue the pattern.

**When:** A small grid, one empty cell, and up to four candidate tiles. The tiles differ by shape, count, or position, not by a paragraph.
**When not:** The candidates are sentences. Use `game.choice-round`.

**Steps:**

1. Show the pattern with one gap. Candidate tiles are buttons under it.
2. Tap a tile to drop it into the gap. Swap by tapping another tile.
3. A wrong tile says which feature broke the rule (shape, count, or direction). The right tile locks.
4. `mark` only for the tile in the spec.

**Don't:** An IQ-test wall of tiny matrices. One gap is enough for a page.

**Example:** A three-by-three of simple shapes. The rule and the correct tile id are in JSON.

---

## 中文

**补上图案的一格.** 问题：一条看图就能懂的规则被写成定义，读者从不用把它续下去。

**何时用:** 一小格网格，空一格，最多四块候选。候选靠形状、数量或位置区分，不靠一段话。
**何时不用:** 候选是句子。用 `game.choice-round`。

**步骤:**

1. 出示图案，留一个空。候选块是下面的按钮。
2. 点一块，它就落到空格里。再点另一块就换上。
3. 放错就说哪一个特征坏了规则（形状、数量或方向）。放对就锁住。
4. 只有规格里的那一块才 `mark`。

**反例:** 一整墙极小的智力测验矩阵。一页空一格就够。

**实例:** 三乘三的简单形状。规则和正确块的 id 写在 JSON 里。
