# Games

## English

Two shelves. Match a **kind** when you know the job. Then match **make** so the round is fun and can sit on a page. The questions, labels, and bans come from the brief. The card does not carry a subject's content.

| Shelf | What it is |
|---|---|
| [kinds](kinds/README.md) | A mini-game you can put on a page. Includes rounds that are not a text menu: pin a map, find something in a picture, assemble, rotate, walk a path, balance, turn a dial, frame a shot, complete a pattern, stack |
| [make](make/README.md) | How that round opens, answers, fails, ends, and lands in the page |

```bash
python3 scripts/match.py --guild games "配对 页面"
python3 scripts/match.py --guild games "fun feedback"
python3 scripts/match.py --guild games --list
```

A hit is one round: one verb, content in JSON, feedback in words, then a link onward. Do not invent a second game after the brief is frozen.

Do not add these unless the brief makes an exception:

- How-to steps the brief bans, combat stats, gacha, stamina, shame leaderboards
- A round that can be won only by dragging
- A timer that punishes learning

---

## 中文

两层架子。知道要完成的事，就匹配一种**种类**。再匹配**做法**，让这一局好玩，并且能放进页面。题目、标签和禁区来自简报。卡片本身不带某个题材的内容。

| 架子 | 是什么 |
|---|---|
| [kinds](kinds/README.md) | 能放进页面的小游戏。不只有文字菜单：在图上钉点、在画面里找、拼零件、旋转、沿路走、调秤、转刻度、取景、补图案、搭层 |
| [make](make/README.md) | 这一局怎么开场、怎么回应、点错怎么办、怎么收束、怎么放进页面 |

```bash
python3 scripts/match.py --guild games "配对 页面"
python3 scripts/match.py --guild games "fun feedback"
python3 scripts/match.py --guild games --list
```

命中之后就是一局：一个动作，内容在 JSON 里，反馈用文字，然后链到下一页。简报冻结之后不要再发明第二局。

除非简报破例，不做这些类型：

- 简报禁止的操作步骤、战斗数值、抽卡、体力、排行榜羞辱
- 仅靠拖拽过关
- 计时惩罚学习
