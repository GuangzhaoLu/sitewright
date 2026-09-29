## data.access-first

## English

**Model the reads and writes.** Problem: The tables look correct, but the few queries the page needs cannot be done.

**When:** You have already decided to persist data.

**When not:** You are still on the static plan in `data.not-yet`.

**Steps:**

1. List the few things the interface actually does: a list, fetch one by id, filter by one condition, and who may edit.
2. Shape storage around those. Do not build a table for a report nobody asked for.
3. If a filter is only a few dozen rows, do it in the browser first. A database is not required.
4. Show the model to the conductor. If a query does not fit in S5, record the risk. Do not add a table in private.

**Don't:** Fifteen tables for an about site, when the page only uses the title.

**Example:** Sitewright has not used this yet.

---

## 中文

**按读写来建模.** 问题：表结构很「正确」，页面上的那几个查询却做不到。

**何时用:** 已经决定要持久化。

**何时不用:** 还停在 `data.not-yet` 的静态方案。

**步骤:**

1. 列出界面真正会做的少数几件事：列表、按 id 取一条、按一个条件筛选、谁可以改。
2. 存储按这几件事来。没人要的报表不建表。
3. 筛选若只有几十条，可以先在浏览器里做，不必上库。
4. 模型写完给指挥看。S5 发现查询对不上，记风险，不私下加表。

**反例:** 介绍站十五张表，页面只用到标题。

**实例:** Sitewright 尚未用过。
