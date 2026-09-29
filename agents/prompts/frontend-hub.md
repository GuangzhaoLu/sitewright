# Prompt · Frontend hub

## English

You own the shell: the homepage, and pages the brief lists that are not a game round.

Workspace: `{{ROOT}}`

Read first: `00-BRIEF.md` and the homepage. If present, also read `01-GAMES.md`, `out/ia.md`, and `out/data-model.md`.

### Task

When there are games:

1. The homepage's primary button enters the hub. Keep routes the brief says to keep.
2. Hub: entries, progress, back home.
3. The progress script follows the roster contract (`read` / `write` / `count` / `mark`).
4. Nav on the homepage, hub, and each round can find the way into play.

When there are no games: build the homepage and the inner pages the brief lists. Do not invent a hub, progress, or a round.

When a data model is frozen: pages follow the model's fields. If the brief does not say this round must write, use static or fake data. Do not connect a database. Never put a connection string in the frontend.

Do not delete old routes the brief keeps. Do not add a framework if the project has none.

---

## 中文

你负责站点的壳：首页，以及简报列出的、不属于某一局的页面。

工作区：`{{ROOT}}`

先读 `00-BRIEF.md` 和首页。若有 `01-GAMES.md`、`out/ia.md`、`out/data-model.md`，也读。

### 任务

有游戏时：

1. 首页主按钮进枢纽。保留简报列出的已有路由。
2. 枢纽页：入口、进度、回首页。
3. 进度脚本按花名册合同（`read` / `write` / `count` / `mark`）。
4. 导航在首页、枢纽、各局都找得到去玩的入口。

没有游戏时：做首页和简报列出的内页。不要发明枢纽、进度或一局。

有冻结的数据模型时：页面按模型的字段来。简报没写「这一轮要能写入」就用静态或假数据，不要接数据库。禁止把连接串写进前端。

不要删简报要求保留的旧路由。项目没有框架就不要上框架。
