## vid.reduced-motion

## English

**Reduced motion.** Problem: Loops and slow pushes make it impossible for some people to read.

**When:** Any automatic motion, including CSS.

**When not:** The page has no motion.

**Steps:**

1. Honor `prefers-reduced-motion: reduce`: a loop becomes the poster still, and CSS transitions collapse to nearly instant.
2. Offer pause. After pause, hold on the poster or the current frame. Do not leave a mask over the buttons.
3. The thing to learn is in the text beside it. Turning motion off does not drop the information.

**Don't:** Only a "skip," and after the skip the thing to learn is gone.

**Example:** Sitewright has not used this yet. The text equivalent in `vid.silent-loop` is the same rule.

---

## 中文

**减少动效.** 问题：循环和缓推让一部分人无法阅读。

**何时用:** 任何自动运动，包括 CSS。

**何时不用:** 页面没有运动。

**步骤:**

1. 尊重 `prefers-reduced-motion: reduce`：循环片改为海报静帧，CSS 过渡收成近乎瞬切。
2. 提供暂停。暂停后停在海报或当前格，不留遮罩挡按钮。
3. 知识点在旁边文字里，关掉运动不丢信息。

**反例:** 只有「跳过」，跳过之后知识点没了。

**实例:** Sitewright 尚未用过。和 `vid.silent-loop` 的文字等价是同一条。
