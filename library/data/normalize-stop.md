## data.normalize-stop

## English

**One fact, one place.** Problem: The same title is copied into five tables, and a change in one place misses the other four.

**When:** The data will be updated. It is not a static draft published once.

**When not:** Static JSON. Edit it and publish again.

**Steps:**

1. Store each fact that can change in one place. Follow a relation to read it. Do not copy it first.
2. Keep a second copy only when a particular read is actually too slow, and you can say who refreshes that copy.
3. For the extra copy, write where it comes from, when it updates, and which copy wins if they disagree.
4. Do not add redundancy on day one because it might be slow later.

**Don't:** Copy the name into every table before any data exists.

**Example:** Sitewright has not used this yet.

---

## 中文

**一件事实放一处.** 问题：同一标题抄在五张表里，改一处漏四处。

**何时用:** 数据会被更新，不只是发布一次的静态稿。

**何时不用:** 静态 JSON，改完重新发布即可。

**步骤:**

1. 每个会改的事实只存一处。用关联去取，不先抄一份。
2. 只有某个读取确实太慢、而且你写得清谁负责刷新副本时，才多存一份。
3. 多存的那份要写明：从哪来、何时更新、不一致时以谁为准。
4. 不要在第一天为了「以后可能慢」做冗余。

**反例:** 还没有数据，就把名字复制进每一张表。

**实例:** Sitewright 尚未用过。
