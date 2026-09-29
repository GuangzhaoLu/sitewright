## data.not-yet

## English

**Do not add a database yet.** Problem: A four-page about site is set up as a database someone has to operate.

**When:** Someone says it is time for a database. Start with this card.

**When not:** The brief already says several people must edit the same data after signing in, or filter and sort cannot finish in the browser, or records keep growing and must be stored on a server.

**Steps:**

1. Write one sentence: what breaks if there is no database. If you cannot write it, do not add one.
2. Progress that lives only on this device: use `web.progress-localstorage`.
3. Content we write ourselves, and do not change often: JSON or Markdown in the repo.
4. If a database is really required, write the reason in the brief, then seat Data. Do not let the frontend seat pick a database product on the way.

**Don't:** Install a database and accounts for four static articles.

**Example:** Owned content in JSON or Markdown, and progress on this device in `localStorage`, are not a database yet.

---

## 中文

**先别上库.** 问题：四页介绍站被配成要运维的数据库。

**何时用:** 有人说「该上数据库了」。先走这张。

**何时不用:** 简报已经写明：多人登录后要改同一份数据，或筛选排序无法在浏览器里做完，或记录会持续增长且要在服务端保存。

**步骤:**

1. 写一句「如果没有数据库，什么会坏」。写不出来就不上。
2. 只是这台设备上的进度：用 `web.progress-localstorage`。
3. 内容是我们自己写的、改得不频：用仓库里的 JSON 或 Markdown。
4. 真要上库：在简报里写原因，再开数据席。不要由前端席位顺便选一个数据库产品。

**反例:** 为四篇静态文章装一套数据库和账号。

**实例:** 自有内容放 JSON 或 Markdown，本机进度放 `localStorage`，都还不是数据库。
