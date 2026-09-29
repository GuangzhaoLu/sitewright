# 执行流程 Flow

一条链，七个阶段。名字借自 Amazon、Shape Up、游戏制作、新闻图形组；Sitewright 里只保留能在 agent 上执行的部分。

```
S0  往后写     指挥 + PM     PR/FAQ 口吻的简报
S1  塑形       三人组 + 库   匹配工艺，定胃口
S2  下注冻结   用户点头      00-BRIEF / 01-GAMES 锁死
S3  发现波     按站型        至多五席：PM、视觉，加本轮需要的设计 / 内容 / 数据
S4  竖切片     玩法前端      先做通一局（可跳过极小改动）
S5  交付波     至多三席      枢纽 + 玩法 + 插图；视频另开
S6  读稿       QA            对照清单，只修 P0
S7  冷却写回   指挥          新做法进工艺库，P2 另开一轮
```

对 Cursor 说「按 Sitewright 做」时，指挥者自己勾这张表，不要丢给某一个席位。

## S0 · 往后写（Working Backwards）

Amazon：先写发布稿和 FAQ，再决定做不做。Sitewright 里这一页就是 [`templates/00-BRIEF.md`](templates/00-BRIEF.md)，需要对外讲清楚时再填 [`templates/02-PRFAQ.md`](templates/02-PRFAQ.md)。

必须写清：为谁、一句话、成功长什么样、硬禁止、技术底线。没写禁止项，后面的游戏设计就会发明第五局。

这一页由指挥和 PM 在主线程一起起草，不为此另开一个等待中的 PM agent。视觉在 S0–S2 读简报，可以反对，不执笔。PM 和视觉作为平行席位，从 S3 才上场。

## S1 · 塑形（Shape Up shaping + Librarian）

胃口（appetite）：这轮只做「能在一轮里玩通」的东西，不留无底洞。

指挥或 Librarian，在 sitewright 目录里运行：

```bash
python3 scripts/match.py "分层 史料 传说"
python3 scripts/match.py --guild frontend 窄屏 表单
python3 scripts/match.py --guild data 数据库
python3 scripts/match.py --guild images 氛围
python3 scripts/match.py --guild video 循环
```

命中则把卡片 id 写进简报「采用方案」。未命中才外出检索（见 `library/research/`）。若当场要收进库：在对应行当目录新建一个文件，并登记 `catalog.json`。行当 README 不是第三份索引。

## S2 · 下注冻结（betting table）

用户（或指挥代用户）确认简报。有游戏则同时冻结 [`templates/01-GAMES.md`](templates/01-GAMES.md)。

冻结之后：

- 改规则先改规格文件，再重贴提示词。
- 实现席位不得加局、加登录、加惩罚计时。
- 对应 Shape Up 的 circuit breaker：做不完就收口，不把下一轮当延期。

把填好的提示词拷进**项目**的 `agents/sitewright/`，用户以后要审核原文。

## S3 · 发现波（dual-track discovery）

人数上限只写在这里：发现波同时不超过五席。PM 和视觉属于决策核，发现波也写东西。无游戏不上游戏设计。无持久化不上数据。无文案任务不上内容。**原文**粘贴项目里填好的提示词：

| 席位 | 提示词 | 产出 |
|---|---|---|
| PM | `prompts/pm.md` | `out/ia.md`、`out/qa-checklist.md` |
| 游戏设计 | `prompts/game-design.md` | `out/game-beats.md` |
| 视觉 | `prompts/visual.md` | `out/visual-notes.md`、玩法 CSS |
| 内容 | `prompts/content.md` | `data/play-*.json` 或简报指定的文案文件 |
| 数据 | `prompts/data.md` | `out/data-model.md`（仅当简报的数据不是「无」） |

无游戏：游戏设计不上场。内容只写文案和结构，不发明题库。无持久化：数据不上场。

若有人要再开子 agent 并等待：打断，指挥自己开。

## S4 · 竖切片（游戏制作 / NYT prototype）

先让**一局**在真页面上可玩，验证冻结的陷阱（错的流行说法不得通关）。竖切片失败，不要铺开做完所有局。

极小改动（改文案、补链）可跳过本步。没有游戏也跳过。

## S5 · 交付波（delivery）

| 席位 | 提示词 | 产出 |
|---|---|---|
| 枢纽 | `prompts/frontend-hub.md` | 首页、壳；有游戏才做枢纽和进度 |
| 玩法 | `prompts/frontend-play.md` | 每局一页一脚本（无游戏不上场） |
| 插图 | `prompts/art.md` | 封面 / 氛围图入槽（无新图不上场） |

要视频时**另开** `prompts/motion.md`，不要塞进插图席位。数据模型在 S3 已冻结，这一波不改表；对不上只记风险。简报若写「这一轮要能写入」，由枢纽按模型接 API，禁止浏览器直连数据库。

## S6 · 读稿（copy desk + QA）

粘贴 `prompts/qa.md`。对照的是 PM 在 S3 写好的 `out/qa-checklist.md`。空表在 [`templates/qa-checklist.md`](templates/qa-checklist.md)，不在简报旁边再留一份填好的清单。验收可修 P0。指挥复查：手机可点、无死链、冻结陷阱仍在。

## S7 · 冷却（cool-down）

- P2 记在报告里，**不**在本轮做完。
- 本轮新验证的玩法、出图、出片、页面或数据步骤：在对应行当目录新建一张卡片，并更新 `catalog.json`。不要改行当 README 里的卡片名单；名单以 `match.py --list` 为准。
- 下一轮从 S0 再走，不把本轮未完成项自动滚进「待办无限队列」（Shape Up：不养 backlog）。

## 这一轮怎么裁

先选主站型：[playbooks/site-kinds.md](playbooks/site-kinds.md)。

| 活 | Playbook | 裁剪 |
|---|---|---|
| 新站 | [playbooks/new-site.md](playbooks/new-site.md) | 全流程，但先选站型 |
| 改现站 | [playbooks/site-improve.md](playbooks/site-improve.md) | 简报写「改什么、不改什么」；可跳过竖切片 |
| 寓教于乐 | [playbooks/playful-learning.md](playbooks/playful-learning.md) | 必须有枢纽→一局→解释→深读 |
| 带数据的产品 | [playbooks/product-data.md](playbooks/product-data.md) | S3 冻模型；浏览器不直连库 |

## 归档位置（项目内）

```
{项目}/agents/sitewright/
  00-BRIEF.md
  01-GAMES.md          # 若有游戏
  prompts/*.md         # 填好的副本
  out/                 # IA、节拍、视觉、QA、library-hits
```

每个项目用自己的 `agents/sitewright/`。不要把别的站的简报和题库拷进来。
