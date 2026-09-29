# Data

## English

When a database is actually needed, and how to shape it after that. The default is still a static file, or one progress record in the browser (see [web](../web/README.md)).

Chris Coyier, “The Moment You Need a Database” (Frontend Masters, 2026): you need a database when signed-in people keep writing, when you must search, filter, and sort, or when the material no longer fits in static files. A database does not arrive alone; an API sits in front of it. The OWASP Database Security Cheat Sheet: an untrusted client does not connect to the database. It goes through an API that can enforce access control, and the database account has the least privilege that works. Model the real reads and writes. Normalize first; add a controlled copy only after you have measured the cost of reading (Exasol’s design notes).

Suggested search words: database, content model, reads and writes, API, normalize, migration, secrets.

List the cards:

```bash
python3 scripts/match.py --guild data --list
```

---

## 中文

什么时候才用数据库，以及用了之后怎么建。默认仍然是静态文件或浏览器里的一份进度（见 [web](../web/README.md)）。

依据：Chris Coyier，《The Moment You Need a Database》（Frontend Masters，2026）：登录后要持续写入、要检索筛选排序、东西多到静态文件撑不住时，才需要库；库不会单独出现，前面还有一层后端。OWASP Database Security Cheat Sheet：不可信的客户端不要直接连数据库，要经过能做访问控制的 API，数据库账号取最小权限。模式按真实读写来，而不是先把表拆到自己都查不动（Exasol 的设计说明：先规范化，只有测到读的代价之后才有控制地冗余）。

检索词：数据库、内容模型、读写、API、规范化、迁移、密钥。

列出卡片：

```bash
python3 scripts/match.py --guild data --list
```
