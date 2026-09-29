## fe.semantic-outline

## English

**Outline before decoration.** Problem: The page is a pile of color blocks with no hierarchy.

**When:** A page that is read or that contains a form.

**When not:** Pure decoration, with no information.

**Steps:**

1. One `h1` per page. Sections use `h2`. Do not skip a level.
2. Put the main content in `main`. Put repeated navigation in `nav`.
3. Something you can activate is a `button` or an `a`. State uses words, not color alone (see `web.a11y-buttons`).
4. Outline order is reading order. Do not use absolute positioning to twist visual order away from DOM order.

**Don't:** Everything is a `div`, and the heading is an enlarged `span`.

**Example:** Sitewright has not used this card on its own yet. Check it together with tap targets and state in words.

---

## 中文

**先有大纲.** 问题：页面是一堆没有层级的色块。

**何时用:** 有阅读或表单的页。

**何时不用:** 纯装饰、没有信息。

**步骤:**

1. 一页一个 `h1`。小节用 `h2`，不跳级。
2. 主内容放在 `main`，重复的导航放在 `nav`。
3. 能点的用 `button` 或 `a`。状态用文字，不只用颜色（见 `web.a11y-buttons`）。
4. 大纲顺序就是阅读顺序。不要靠绝对定位把视觉顺序和 DOM 顺序拧开。

**反例:** 全是 `div`，标题用放大的 `span`。

**实例:** Sitewright 尚未单独用过。和点按热区、状态文字一起检查。
