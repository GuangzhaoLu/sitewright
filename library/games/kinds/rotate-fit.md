## game.rotate-fit

## English

**Rotate until it fits.** Problem: The shape is right and the orientation is wrong, and a text choice cannot show that.

**When:** One piece, and two to four orientations. One of them matches a fixed outline.
**When not:** The difference is a word, not a direction.

**Steps:**

1. Show the outline and the piece. A Rotate button turns the piece by a fixed step (90 degrees, or the steps named in the brief).
2. A second button, Fit, checks the current orientation. Do not require a drag-to-spin.
3. Wrong orientation: say which way it still needs to turn. Right orientation: it locks.
4. `mark` only on the orientation the spec names.

**Don't:** A free spin that must stop on an exact degree. No timer.

**Example:** A plan, an arrow, a tool, or a letterform that is not a word to choose. The correct step index is in JSON.

---

## 中文

**转到合适的方向.** 问题：形状对了，方向错了。文字选项表现不了这一点。

**何时用:** 一块零件，两到四个方向，其中一个对准固定的轮廓。
**何时不用:** 差别是一个词，不是一个方向。

**步骤:**

1. 出示轮廓和零件。「旋转」按钮按固定步长转动（90 度，或简报写明的步长）。
2. 第二个按钮「合上」检查当前方向。不要只能靠拖着转。
3. 方向不对：说还要往哪边转。方向对了：锁住。
4. 只有规格里的那个方向才 `mark`。

**反例:** 自由旋转，必须停在精确的度数上。不要计时。

**实例:** 一张平面、一个箭头、一件工具，或不是用来选词的字形。正确的步数写在 JSON 里。
