## data.migrate-forward

## English

**Migrations only move forward.** Problem: After launch someone alters the live tables, and the model in the repo no longer matches.

**When:** Saved data already exists, and the shape still has to change.

**When not:** No user or content data has been stored yet. Edit `out/data-model.md` and freeze again.

**Steps:**

1. Each structural change is a new migration, run in order. Do not edit one that has already run.
2. Keep migrations and seed data apart. Seed data can be replayed. User data cannot.
3. If a field will be dropped or its meaning will change, write one sentence about what the old data becomes.
4. Do not put secrets or connection strings in a migration file (see `data.api-wall`).

**Don't:** Alter a column by hand in production and leave it out of the repo.

**Example:** Sitewright has not used this yet.

---

## 中文

**迁移只向前.** 问题：上线后有人直接改线上表，仓库里的模型对不上。

**何时用:** 已经有存下来的数据，结构还要变。

**何时不用:** 还没有存任何用户或内容数据。那时改 `out/data-model.md` 再冻结即可。

**步骤:**

1. 每次结构变化是一份新的迁移，按顺序执行，不改已经跑过的那一份。
2. 迁移和种子数据分开。种子可以重来，用户数据不能。
3. 会丢字段或改含义时，写一句旧数据变成什么。
4. 密钥和连接串不写进迁移文件（见 `data.api-wall`）。

**反例:** 在线上手工改列，不记进仓库。

**实例:** Sitewright 尚未用过。
