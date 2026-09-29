## game.flash-recall

## English

**Flash recall.** Problem: The reader recognizes a term in a list and still cannot recall it.

**When:** A small deck. The front is a prompt. The back is the answer they should produce or pick.
**When not:** There is no stable answer. If they only need to recognize one option, use `game.choice-round`.

**Steps:**

1. Show the front. Then "show answer," or three candidate backs as buttons.
2. "I had it / not yet" does not `mark`. `mark` only when they pick the correct back.
3. A missed card may return once in the same round. No streak punishment.
4. At most eight cards on one page.

**Don't:** A timer that fails the card. Do not print the answer on the front.

**Example:** Term on the front, one-sentence sense on the back, taken from the page's glossary JSON.

---

## 中文

**翻卡回想.** 问题：读者在列表里认得这个词，却回想不起来。

**何时用:** 一小叠卡片。正面是提示，背面是要回想或点中的答案。
**何时不用:** 没有稳定答案。若只要认出一个选项，用 `game.choice-round`。

**步骤:**

1. 先给正面。再给「看答案」，或三个背面候选按钮。
2. 「我想起来了 / 还没有」不能 `mark`。只有点中正确背面才 `mark`。
3. 没记住的卡可以在这一局里再出现一次。不要连击惩罚。
4. 一页最多八张。

**反例:** 用计时判失败。不要把答案印在正面。

**实例:** 正面是术语，背面是一句释义，内容来自这一页的术语 JSON。
