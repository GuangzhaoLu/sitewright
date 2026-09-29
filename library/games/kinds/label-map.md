## game.label-map

## English

**Label the diagram.** Problem: A diagram has parts, and the reader never has to name them.

**When:** One picture, at most six regions, each with one correct label from a short list.
**When not:** Tapping a region only needs to show a caption (`game.hotspot`), or the regions cannot be about 44px.

**Steps:**

1. Labels are buttons under the image. Regions are buttons on the image. Tap a label, then a region.
2. On a narrow screen, the regions become a list under the image, same ids.
3. A wrong pair says what that region is. A right pair locks.
4. `mark` when every region has its label.

**Don't:** Tiny pins on a decorative wide shot. Do not bake the labels into the image.

**Example:** A process diagram on a product page. Region ids and label strings live in JSON.

---

## 中文

**图上贴标签.** 问题：图上有部件，读者从不用自己叫出名字。

**何时用:** 一张图，最多六个区域，每个区域在一份短名单里有一个正确标签。
**何时不用:** 点区域只要弹出说明（用 `game.hotspot`），或区域做不到大约 44px。

**步骤:**

1. 标签是图下的按钮。区域是图上的按钮。先点标签，再点区域。
2. 窄屏时区域改成图下的列表，id 不变。
3. 贴错就说明这个区域是什么。贴对就锁住。
4. 每个区域都有自己的标签才 `mark`。

**反例:** 在装饰性的大图上找极小的针。不要把标签画进图里。

**实例:** 产品页上的流程图。区域 id 和标签文字在 JSON 里。
