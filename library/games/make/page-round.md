## game.page-round

## English

**One round on the page.** Problem: A playable idea never becomes a section someone can finish.

**When:** A kind is already matched, and this round is going on the site.
**When not:** You are still choosing which kind.

**Steps:**

1. One round is one page, or one section with its own heading. Do not hide three games in one scroll with no stop.
2. Put the stem, options, and labels in JSON. The page fetches them. Do not leave right and wrong only inside JS.
3. One verb, buttons about 44px, feedback in words.
4. A done state, then a link to the next real page. If the site tracks progress, `mark` only on the win the spec names.

**Don't:** A game in a modal the keyboard cannot reach, or a canvas with no text.

**Example:** `pages/play-{id}.html` and `data/play-{id}.json`, or the same contract inside a section of a page that already exists.

---

## 中文

**一局放进页面.** 问题：能玩的想法没有变成读者可以做完的一节。

**何时用:** 种类已经匹配上，这一局要上站点。
**何时不用:** 还在选哪一种。

**步骤:**

1. 一局是一页，或是带自己标题的一节。不要把三局藏在一段不停的滚动里。
2. 题干、选项、标签放进 JSON。页面去取。不要只把对错写在 JS 里。
3. 一个动作，按钮大约 44px，反馈用文字。
4. 有一个做完的状态，然后链到下一张真页面。站点若记进度，只在规格写明的赢法上 `mark`。

**反例:** 键盘到不了的弹层，或一块没有文字的画布。

**实例:** `pages/play-{id}.html` 加 `data/play-{id}.json`，或在已有页面的一节里用同一份合同。
