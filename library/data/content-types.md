## data.content-types

## English

**Name the content types first.** Problem: Tables get built before anyone has said what kinds of things exist.

**When:** There is more than one kind of record (articles, entries, people, orders).

**When not:** One list, fixed fields, and a single JSON file is enough.

**Steps:**

1. For each type: name, required fields, optional fields, and what it relates to.
2. Write that in the project's `out/data-model.md`. Do not write migrations or pick a vendor before freeze.
3. Name the relation in words (an article has one author). Do not start with many-to-many.
4. Domain words stay in the project brief. This card does not prescribe fields for any industry.

**Don't:** One JSON that can hold anything, with every field optional.

**Example:** Sitewright has not used this yet. One list in one JSON file is not yet a reason to build tables.

---

## 中文

**先写内容类型.** 问题：还没说清有哪几种东西，就开始建表。

**何时用:** 不止一种记录（文章、条目、人、订单）。

**何时不用:** 一种列表，字段固定，放一个 JSON 就够。

**步骤:**

1. 每种类型：名字、必填字段、可选字段、和谁有关。
2. 写在项目 `out/data-model.md`。冻结前不写迁移、不选厂商。
3. 关系用名字说清（一篇文章有一个作者），不要先上多对多。
4. 领域词留在项目简报。这张卡不规定任何行业的字段。

**反例:** 一个什么都能塞的 JSON，字段全是可选。

**实例:** Sitewright 尚未用过。一种列表放一个 JSON，还没到要建表。
