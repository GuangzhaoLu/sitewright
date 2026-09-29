## game.myth-trap

## English

**Popular-claim trap.** Problem: The sentence that sounds best is not the historical one, and the player will pick it as the answer.

**When:** The brief names a popular line that must not count as a win.

**When not:** There is no popular misunderstanding. Do not invent a trap just to have a fail animation.

**Steps:**

1. The trap item is `correct: false`. You may add a flag such as `fiction`.
2. On select, play a separate fail (it closes, a line of narration). Do **not** write progress.
3. A regex fallback: the popular line still counts as the trap if a few characters change.
4. The correct item must be the sentence the brief names. On a win, keep evidence and fiction as two lines. Do not mix them into one upgrade path.

**Don't:** Selecting the trap still calls `mark`. The trap is a joke, and progress is granted anyway.

**Example:** The popular line named in the brief must not `mark` when it is selected.

---

## 中文

**流行说法陷阱.** 问题：最好听的那句不是史实，但玩家会拿它当答案。

**何时用:** 简报点名某句流行话不得当赢。

**何时不用:** 没有流行误解，不要为了「有失败动画」而造陷阱。

**步骤:**

1. 陷阱项 `correct: false`，可加 `fiction` 一类旗。
2. 选中后走单独失败演出（收起、旁白），**不**写进度。
3. 正则兜底：流行话换了几个字仍算陷阱。
4. 正确项必须是简报指定的那句。通关把证据和文艺分成两条，不要混成一条升级线。

**反例:** 选陷阱仍 `mark`；陷阱当幽默彩蛋但进度给了。

**实例:** 简报点名的那句流行话，选中不得 `mark`。
