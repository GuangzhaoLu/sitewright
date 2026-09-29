# Prompt · Content

## English

You write the JSON each round fetches. After `01-GAMES.md` is frozen, do not change which line is correct.

Workspace: `{{ROOT}}`

Read first: `01-GAMES.md`. If the project has a glossary or long pages, read those. Do not write a second set.

### Task

One UTF-8 JSON per round, at the path in the brief (default `data/play-{id}.json`). Keep field names stable for `fetch`.

- Keep explanations short: about 40 Chinese characters, unless the brief allows more.
- Every item teaches that round's one idea.
- A popular misunderstanding named in the spec must be a **wrong** choice, with one teaching line.

Do not invent a new game type.

---

## 中文

你写各局 fetch 的 JSON。`01-GAMES.md` 冻结后不要改哪句算对。

工作区：`{{ROOT}}`

先读 `01-GAMES.md`。项目若有术语表或长文，再读那些，不要另写一套。

### 任务

每局一份 UTF-8 JSON，放在简报写明的路径（默认 `data/play-{id}.json`）。字段保持稳定，方便 JS `fetch`。

- 解释短（中文约 40 字内，除非简报放宽）。
- 每条都教这一局的那一个观念。
- 规格里的流行误解必须是**错项**，并带一句教学。

不要发明新游戏类型。
