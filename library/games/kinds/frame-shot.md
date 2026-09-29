## game.frame-shot

## English

**Place the frame.** Problem: What matters is which part of the picture you keep, and a caption cannot make the reader frame it.

**When:** One image and a few frame positions (two to four). The brief names the position that keeps the subject.
**When not:** You are only cropping for export (`img.safe-crop`), with no player. Or any frame would do.

**Steps:**

1. The image stays still. Frame choices are buttons: each shows that crop, or moves a rectangle to a preset.
2. The player picks a frame, then confirms. The chosen crop is obvious.
3. A wrong frame says what got cut off or what extra got in. The right frame locks.
4. `mark` only for the position in the spec. Tap presets. Do not require drawing a rectangle.

**Don't:** A tiny drag handle as the only control.

**Example:** One photograph, four preset crops in JSON, one of them keeps the subject. A section on the page.

---

## 中文

**把取景框放上去.** 问题：要紧的是画面里留下哪一部分。一句说明不会让读者自己去取景。

**何时用:** 一张图，两到四个取景位置，简报写明哪一个留下了主体。
**何时不用:** 只是导出时的裁切（`img.safe-crop`），没有玩家。或随便哪个框都可以。

**步骤:**

1. 图不动。取景是按钮：每个按钮出示一种裁切，或把矩形移到一个预设位置。
2. 玩家选一个框，再确认。选中的裁切要看得出来。
3. 框错了就说切掉了什么，或多收进了什么。框对了就锁住。
4. 只有规格里的位置才 `mark`。点预设。不要让人自己画矩形。

**反例:** 只能拖一个很小的手柄。

**实例:** 一张照片，JSON 里四个预设裁切，其中一个留下主体。页面上一节。
