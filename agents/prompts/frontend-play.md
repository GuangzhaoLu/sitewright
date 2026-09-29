# Prompt · Frontend play

## English

You implement every round in `01-GAMES.md`. Add none.

Workspace: `{{ROOT}}`

Read first: `01-GAMES.md`, `out/game-beats.md`, the play CSS, and the progress script. If the script is missing, add it to the roster contract first.

### Task

For each round id:

- one HTML page
- one JS file
- `fetch` the matching JSON (an array, or `{rounds|items|questions}`)

Rules:

- Tap first, including phones. Success and failure use **words**, not color alone.
- Call `mark(id)` only for the win the spec names.
- A frozen trap must not pass.
- Exits: the next page in the brief, replay, and back to the hub.
- Do not add a framework if the project has none.

Do not change right and wrong inside JSON. If JSON is missing, stop and say so.

---

## 中文

你实现 `01-GAMES.md` 里的每一局。不加局。

工作区：`{{ROOT}}`

先读 `01-GAMES.md`、`out/game-beats.md`、玩法 CSS、进度脚本。进度脚本若还没有，先按花名册合同补上。

### 任务

每一局 id：

- 一页 HTML
- 一份 JS
- `fetch` 对应 JSON（数组，或 `{rounds|items|questions}`）

规则：

- 点按优先，包括手机。成功失败用**文字**，不只靠颜色。
- 只有规格写明的赢法才 `mark(id)`。
- 冻结陷阱不得通关。
- 出口：简报写的下一页、再来、回枢纽。
- 项目没有框架就不要上框架。

不要改 JSON 的对错。JSON 缺失就停下来说明。
