## vid.web-export

## English

**Compress for the web.** Problem: A master file of tens of megabytes goes onto the page.

**When:** You are sure a `<video>` will go live.

**When not:** You have not decided to ship a video. An internal screen recording may be a bit larger, and it is still not 4K.

**Steps:**

1. The short edge is at most 720. H.264 with faststart, or also a WebM.
2. If there is no audio, do not embed an empty audio track.
3. The poster frame is its own JPG. Try to keep a loop under about 1.5MB. If it is over, switch to a still or to CSS.
4. The master does not enter git.

**Don't:** Use the edit project's highest quality directly as `src`.

**Example:** Sitewright has not used this yet. It pairs with `img.export-web` for images.

---

## 中文

**片怎么压.** 问题：原片几十兆进页面。

**何时用:** 确定有 `<video>` 要上线。

**何时不用:** 还没决定上片。内部录屏可以稍大，仍不要 4K。

**步骤:**

1. 短边不超过 720。H.264 加 faststart，或再给一个 WebM。
2. 无声轨就不要嵌一条空音频。
3. 海报帧单独 JPG。循环片尽量压到约 1.5MB 以内；超了就改静帧或 CSS。
4. 母带不进 git。

**反例:** 把剪辑工程的最高质量直接当 `src`。

**实例:** Sitewright 尚未用过。和图的 `img.export-web` 成对。
