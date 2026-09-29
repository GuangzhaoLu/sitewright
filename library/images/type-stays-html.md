## img.type-stays-html

## English

**Type stays in HTML.** Problem: Words that must be read are painted into a raster and become fake letters or mush.

**When:** A title, a caption, a term, or an axis name.

**When not:** An ink mark in the paper texture that is not there to be read.

**Steps:**

1. Do not put readable words in the image. Axis names and captions use HTML or SVG `<text>`.
2. In the constraints for generation, write "no text, no fake letters, no watermark."
3. When grading, enlarge the image and look at the corners. If there are words, generate again.

**Don't:** A cover headline baked into the JPG, so a copy change means a redraw.

**Example:** Use it with `img.svg-vs-raster` and `img.gen-then-grade`. Words that must be read are real text.

---

## 中文

**字不进图.** 问题：必须读的字被画进栅格，变成假字或糊字。

**何时用:** 标题、图注、术语、轴名。

**何时不用:** 纸纹里不承担阅读的墨迹。

**步骤:**

1. 图里不要可阅读的字。轴名、图注用 HTML 或 SVG `<text>`。
2. 生成时在约束里写「无文字、无假字、无水印」。
3. 评级时把图放大看角落。有字就重抽。

**反例:** 封面大标题做进 JPG，换文案还得重画。

**实例:** 和 `img.svg-vs-raster`、`img.gen-then-grade` 一起用。必须读的字用真文字。
