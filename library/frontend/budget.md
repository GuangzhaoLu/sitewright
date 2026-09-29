## fe.budget

## English

**Text before weight.** Problem: The first screen is a large image, heavy type, and a pile of scripts. The text has not arrived.

**When:** Any public page.

**When not:** Never.

**Steps:**

1. Without scripts, the words and captions on the main path are still there.
2. Images follow `img.export-web`. Video passes `vid.when-not` first.
3. At most one custom font. Otherwise use the system font.
4. A four-page static site does not take a bundler for a component library (see `web.static-html-first`). Change the stack only if the brief changes it.

**Don't:** An autoplaying video with sound as the first screen, with the text underneath.

**Example:** A static page does not take a heavy runtime for four pages of content. If the weight is too high, cut images and scripts.

---

## 中文

**先给字，再给重量.** 问题：首屏是大片、粗字体和一堆脚本，正文还没到。

**何时用:** 任何公开页。

**何时不用:** 从未。

**步骤:**

1. 没有脚本时，主路径的字和图注仍然在。
2. 图走 `img.export-web`。视频先过 `vid.when-not`。
3. 自定义字体最多一种；没有就用系统字体。
4. 四页静态站不要为了组件库上打包器（见 `web.static-html-first`）。简报改了栈再换。

**反例:** 自动播放有声片当首屏，正文在片下面。

**实例:** 静态页不要为了四页内容上重运行时。重量超了就减图、减脚本。
