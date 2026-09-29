## game.find-in-scene

## English

**Find it in the picture.** Problem: The thing to notice is in the picture, and a text list of options gives it away.

**When:** One scene, three to six findable things, each large enough to tap.
**When not:** There is no picture yet, or the "find" is a sentence inside a paragraph (`game.highlight-span`).

**Steps:**

1. Show the scene. The prompt names the kind of thing, not a multiple-choice list.
2. Each target is a button over the picture, about 44px, with a visible focus.
3. A hit gets one sentence. A tap on empty space does nothing punitive.
4. On a narrow screen, keep the same targets. Do not shrink them into specks. `mark` when every target is found.

**Don't:** A hidden-object collage of dozens of tiny items, or a timer.

**Example:** A workshop photo or an illustration. Target ids and captions live in JSON. Words stay beside the picture, not inside it.

---

## 中文

**在画面里找.** 问题：要看见的东西在画面里。文字选项会把答案送掉。

**何时用:** 一个场面，三到六件找得到的东西，每一件都大到能点。
**何时不用:** 还没有图，或要找的是段落里的一句话（用 `game.highlight-span`）。

**步骤:**

1. 出示场面。题干说要找的是哪一类，不给选择题清单。
2. 每个目标是叠在图上的按钮，大约 44px，焦点可见。
3. 点中给一句说明。点在空白处没有惩罚。
4. 窄屏仍用同样的目标，不要缩成小点。每个目标都找到才 `mark`。

**反例:** 几十件极小物品的找茬拼贴，或计时。

**实例:** 一张工作场景的照片或插图。目标 id 和说明在 JSON 里。字留在图旁边，不画进图里。
