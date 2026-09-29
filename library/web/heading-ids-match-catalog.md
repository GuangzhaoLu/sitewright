## web.heading-ids-match-catalog

## English

**Headings follow frozen hashes.** Problem: The catalog was published with `#some-section` first, the body was written later, and the slug does not match.

**When:** A tree, a glossary, or an old link is already public.

**When not:** A brand-new site, and the hashes have not left the building.

**Steps:** Pull every `pages/*.html#…` out of the JSON. A section `##` must `slugify` to that same string. After the build, scan that every `id="…"` is present. Do not reword a heading for style and break the link.

**Example:** A published catalog JSON and the headings in the body must share one set of slugs. Before you change the wording of a heading, check the old links.

---

## 中文

**标题迁就已冻的 hash.** 问题：目录先写了 `#某节`，正文后写，slug 对不上。

**何时用:** 树、术语或旧链接已经发布。

**何时不用:** 全新站点，hash 还没外流。

**步骤:** 从 JSON 抽出所有 `pages/*.html#…`，章节 `##` 必须 `slugify` 成同一串。构建后扫 `id="…"` 是否齐全。不要为了文采改标题用字导致断链。

**实例:** 已发布的目录 JSON 与正文标题必须是同一套 slug。改标题用字之前，先查旧链接。
