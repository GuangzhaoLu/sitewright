# Sitewright

## English

A standing crew for making websites. Brand pages, documentation, products that store data, and play-then-learn sites share one roster, one flow, and one craft library. Names, bans, and question banks that belong to a subject stay in that project's brief.

The folder is `sitewright`: who is on the job, in what order, and which method to match before inventing one. The old name Gongfang is retired.

Say to Cursor:

> Use Sitewright: …… (what this round must ship)

```
What to ship
    │
    ▼
1. Roster     who is seated, and who is not
2. Flow       write, then build (S0–S7)
3. Library    match a method, then invent one
```

### Roster

Seats are in [`agents/ROSTER.md`](agents/ROSTER.md). Product, project, review, art, and engineering map onto seats that already exist. There is no extra manager. The conductor, product, and visual seats decide together.

### Flow

[`agents/FLOW.md`](agents/FLOW.md): freeze the brief before writing pages. Pick one site kind first, in [`agents/playbooks/site-kinds.md`](agents/playbooks/site-kinds.md). Hard rules are in [`agents/RULES.md`](agents/RULES.md).

### Library

[`library/`](library/README.md) is split by guild. One method is one card. Guilds: games, images, video, frontend, data, research, and web engineering. `scripts/match.py` searches Chinese and English.

```bash
python3 scripts/match.py "表单 窄屏"
python3 scripts/match.py "form reflow"
python3 scripts/match.py --guild data database
python3 scripts/match.py --list
```

### What this is not

- Not Scrum. No standups, story points, or burndown charts.
- Not another manager stacked on the product trio.
- Not an asset pack. The library stores methods: when to use them, when not to, steps, and counterexamples.
- Not a default of databases, accounts, or frameworks.

### Sources

- Product trio: Teresa Torres, [The Product Trio](https://www.producttalk.org/product-trio/)
- Write the release before you build: [About Amazon](https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes)
- Appetite, betting, circuit breaker, cool-down: [Shape Up](https://basecamp.com/shapeup/2.2-chapter-08)
- Ask what the page must answer, then prototype: New York Times graphics desk (`agents/industry/nyt-graphics.md`)
- When a database is actually needed: [The Moment You Need a Database](https://frontendmasters.com/blog/the-moment-you-need-a-database/)
- The browser does not connect to the database: [OWASP Database Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html)

Notes in [`agents/industry/`](agents/industry/README.md) keep the methods, not the headcount.

---

## 中文

做网页的常设班组。品牌页、文档、带数据的产品、寓教于乐，都用同一套分工、流程和技能库。领域专名、禁区和题库只写在那个项目的简报里。

目录名是 `sitewright`。它是造网站的班子：谁上场、按什么顺序做、做法从库里匹配。旧名工坊 Gongfang 不再使用。

对 Cursor 说：

> 按 Sitewright 做：……（这一轮要交付什么）

```
需要做什么
    │
    ▼
1. 分工      谁上场、谁不上场
2. 流程      先写再做（S0–S7）
3. 技能库    先匹配，再发明
```

### 分工

席位在 [`agents/ROSTER.md`](agents/ROSTER.md)。产品、项目、审核、美工、程序员都映射到已有席位。不另设经理。决策是指挥、产品、视觉三个人一起负责。

### 流程

[`agents/FLOW.md`](agents/FLOW.md)：简报冻结之后才写页面。一轮先选站型，见 [`agents/playbooks/site-kinds.md`](agents/playbooks/site-kinds.md)。硬规则在 [`agents/RULES.md`](agents/RULES.md)。

### 技能库

[`library/`](library/README.md) 按行当分目录，一个做法一张卡片。行当：游戏、图像、视频、前端、数据、检索、网页工程。`scripts/match.py` 用中文或英文都能搜。

```bash
python3 scripts/match.py "表单 窄屏"
python3 scripts/match.py "form reflow"
python3 scripts/match.py --guild data database
python3 scripts/match.py --list
```

### 不是什么

- 不是 Scrum。没有站会、故事点、燃尽图。
- 不是在三人组外面再加一层经理。
- 不是素材站。库存的是做法：何时用、何时不用、步骤、反例。
- 不是默认上数据库、上账号、上框架。

### 依据

- 产品三人组：Teresa Torres，[The Product Trio](https://www.producttalk.org/product-trio/)
- 先写发布稿再决定做不做：[About Amazon](https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes)
- 胃口、下注、熔断、冷却：[Shape Up](https://basecamp.com/shapeup/2.2-chapter-08)
- 先问这一页回答什么，再做原型：纽约时报图形组（`agents/industry/nyt-graphics.md`）
- 何时才需要数据库：[The Moment You Need a Database](https://frontendmasters.com/blog/the-moment-you-need-a-database/)
- 浏览器不直连数据库：[OWASP Database Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html)

对照笔记在 [`agents/industry/`](agents/industry/README.md)。只借做法，不借大厂人数。
