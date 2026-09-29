## game.walk-path

## English

**Walk the path.** Problem: A route is a shape on a board, and choosing "the correct route" from three sentences does not make anyone walk it.

**When:** A small grid or a few connected nodes, at most about sixteen cells, and the brief names the path.
**When not:** The lesson is a date order with no space (`game.sequence-order`), or the board is a maze large enough to need a map.

**Steps:**

1. Cells or nodes are buttons. The player taps a neighbor of the current cell to step.
2. A legal step moves the marker. An illegal step stays put and says why that way is closed.
3. Keyboard: arrow-like buttons or the same neighbors in a list, so it is not drag-only.
4. `mark` when the marker reaches the end along the path in the spec. Wandering off does not reset the whole round.

**Don't:** A dead maze whose only lesson is patience. No combat, no lives.

**Example:** A six-by-four grid of a room, a street, or a process. Passable cells are ids in JSON.

---

## 中文

**沿着路走.** 问题：路线是棋盘上的形状。从三句话里选「正确路线」并没有让人走过去。

**何时用:** 小网格或不多的连通节点，大约十六格以内，简报写明那条路。
**何时不用:** 只是没有空间的年代先后（用 `game.sequence-order`），或迷宫大到还要一张地图。

**步骤:**

1. 格子或节点是按钮。玩家点当前格的邻居，走一步。
2. 走得通，标记就过去。走不通，人留在原地，并说明这边为什么关着。
3. 键盘可以用方向按钮，或把邻居列出来点。不能只有拖拽。
4. 沿规格的路走到终点才 `mark`。走偏不把整局清掉。

**反例:** 只考耐心的死迷宫。不要战斗，不要生命条。

**实例:** 六乘四的房间、街道或流程。能走的格子 id 写在 JSON 里。
