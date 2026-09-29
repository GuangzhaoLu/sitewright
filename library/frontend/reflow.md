## fe.reflow

## English

**Reflow, do not shrink.** Problem: The desktop layout is scaled down, so type and buttons shrink together.

**When:** Any page that will be opened on a phone.

**When not:** The brief says large screens on an internal network only, and acceptance does not use a phone.

**Steps:**

1. Narrower than about `40rem`, become one column. Reading order stays the same.
2. Do not require horizontal scrolling to read the body or press the primary button.
3. Keep the primary button about 44px tall (see `web.tap-44`). WCAG's 24px is a floor, not the target.
4. Crop images with `img.safe-crop`. Do not shrink the whole page with `transform: scale`.

**Don't:** A desktop three-column layout squeezed into three columns of tiny type on a phone.

**Example:** Sitewright game cards already require large enough slots on a narrow screen, and hotspots become buttons under the image.

---

## 中文

**窄屏重排.** 问题：把桌面版缩小，字和按钮一起变小。

**何时用:** 任何会在手机上打开的页。

**何时不用:** 简报写明只给大屏内网，且验收也不用手机。

**步骤:**

1. 窄于约 `40rem` 时改成一列，阅读顺序不变。
2. 不出现横向滚动来读正文或点主按钮。
3. 主按钮保持约 44px 高（见 `web.tap-44`）。WCAG 的 24px 是下限，不是目标。
4. 图按 `img.safe-crop` 裁，不靠把整页 `transform: scale` 缩小。

**反例:** 桌面三栏在手机上挤成三列小字。

**实例:** Sitewright 游戏卡已要求窄屏槽够大、热点改成图下按钮。
