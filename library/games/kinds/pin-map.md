## game.pin-map

## English

**Pin the place.** Problem: The answer is a place, and a list of place names lets the reader skip looking.

**When:** One map or plan, and the brief names one point (or up to three) that must be tapped.
**When not:** The reader only needs to pick a name from a menu. That is `game.choice-round`.

**Steps:**

1. The picture is the board. Divide it into tappable zones of about 44px, or snap a tap to the nearest zone. Do not require a pixel-perfect click.
2. The prompt says what to find, in one sentence, without listing the zone names as the answers.
3. A hit locks and says what this place is. A miss says which way to look, not only "wrong."
4. `mark` when every point named in the spec is pinned.

**Don't:** A tiny crosshair on a decorative wide shot. Do not bake the answer pin into the image.

**Example:** A floor plan or a simple map in JSON: zone id, rectangle, and the one-line reason. The page is one section under the article.

---

## 中文

**在图上钉一点.** 问题：答案是一个位置。若给一份地名菜单，读者就不用看图。

**何时用:** 一张地图或平面图，简报写明必须点中的一个点（最多三个）。
**何时不用:** 读者只要从菜单里挑一个名字。那是 `game.choice-round`。

**步骤:**

1. 图就是棋盘。分成大约 44px 的可点区域，或把一次点击吸到最近的区域。不要要求点中精确像素。
2. 题干用一句话说要找什么，不要把区域名字列成答案。
3. 点中就锁住，并说明这里是什么。点偏就说该往哪边看，不要只说「错了」。
4. 规格里的每个点都钉上才 `mark`。

**反例:** 在装饰性的大图上找一个极小的十字。不要把答案钉画进图里。

**实例:** JSON 里写区域 id、矩形和一句理由。放在文章下面的一节。
