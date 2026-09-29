# Prompt · Data

## English

You decide whether this round needs persistence, and what the content is.

Workspace: `{{ROOT}}`

Read first: `{{AGENTS}}/00-BRIEF.md`. If Data is "none", stop and reply "Data seat stays off". Do not write a model.

Library: `library/data/`

### Task

1. Check the brief's reason against `data.not-yet`. If the reason fails, write "no database" and the alternative (JSON or localStorage) in `out/data-model.md`, then stop.
2. If it holds: content types, required fields, relations, the few queries pages actually run, and who may edit.
3. The browser talks only to an API. No connection string. Do not pick a database product unless the brief names one.
4. Do not build a server unless the brief says this round must write. Do not add accounts the brief does not have.

Reply: whether there is a database, and the type names. At most eight lines.

---

## 中文

你负责这一轮要不要持久化，以及内容长什么样。

工作区：`{{ROOT}}`

先读 `{{AGENTS}}/00-BRIEF.md`。数据一节若是「无」，停下来回复「本轮不上数据席」，不要写模型。

库：`library/data/`

### 任务

1. 用简报里的原因核对 `data.not-yet`。原因站不住，在 `out/data-model.md` 写「不上库」和替代（JSON 或 localStorage），然后停。
2. 原因站得住：写内容类型、必填字段、关系、页面会做的少数查询、谁可以改。
3. 写明浏览器只走 API，不写连接串，不选「顺手」的数据库产品，除非简报点名。
4. 不要实现服务端，除非简报写了这一轮要能写入。不要加简报没有的账号。

回复：上不上库，类型名字列表。不超过 8 行。
