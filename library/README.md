# Craft library

## English

Sitewright's method library: matchable methods, not an asset pack. Each guild is a directory. One method is one file. To add a method, create a file in that directory and register it in `catalog.json`. The guild README is not a third index. List cards with `match.py`.

```bash
python3 scripts/match.py "分层 传说 史料"
python3 scripts/match.py --guild images 氛围 风格帧
python3 scripts/match.py --guild video 循环 无声
python3 scripts/match.py --list
```

On a hit, open the card file and write the id into `00-BRIEF` under adopted craft cards. On a miss, search as [research](research/README.md) says. At cool-down, add a card using [SCHEMA.md](SCHEMA.md) and update [catalog.json](catalog.json).

| Directory | Guild |
|---|---|
| [games](games/README.md) | Mini-game kinds for a page, and how to make a round feel good |
| [images](images/README.md) | How to make and export stills |
| [video](video/README.md) | When to use video, boards, and formats |
| [frontend](frontend/README.md) | One job per page, outline, type, narrow screens, forms |
| [data](data/README.md) | When to add a database, content model, API, migrations |
| [research](research/README.md) | How to search for mechanics and references |
| [web](web/README.md) | Engineering contract for a small site |

Id prefixes are shorter than the directory names. The map is in [SCHEMA.md](SCHEMA.md). Do not rename ids to the full directory name.

---

## 中文

Sitewright 的做法库：可匹配的方法，不是素材包。每个行当是一个目录，一张卡片一个文件。加做法时在该目录新建文件，并在 `catalog.json` 登记。行当 README 不是第三份索引。卡片名单用 `match.py` 列。

```bash
python3 scripts/match.py "分层 传说 史料"
python3 scripts/match.py --guild images 氛围 风格帧
python3 scripts/match.py --guild video 循环 无声
python3 scripts/match.py --list
```

命中后打开卡片文件，把 id 写进 `00-BRIEF`「采用的工艺卡片」。没命中：按 [research](research/README.md) 外出搜。收工时按 [SCHEMA.md](SCHEMA.md) 追加卡片并更新 [catalog.json](catalog.json)。

| 目录 | 行当 |
|---|---|
| [games](games/README.md) | 能放进页面的小游戏种类，以及怎样让一局好玩 |
| [images](images/README.md) | 静帧怎么做、怎么导出 |
| [video](video/README.md) | 何时上视频、分镜与格式 |
| [frontend](frontend/README.md) | 页面一事、大纲、字号、窄屏、表单 |
| [data](data/README.md) | 何时上库、内容模型、API、迁移 |
| [research](research/README.md) | 怎么搜玩法与参考 |
| [web](web/README.md) | 小站工程约定 |

卡片 id 的前缀比目录名短。对照表在 [SCHEMA.md](SCHEMA.md)。不要把 id 改成目录全名。
