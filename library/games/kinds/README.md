# Kinds

## English

Playable mini-games. Match one, then put that round on a page. Some kinds are text choices. Others are the board itself: a map, a picture, a path, a scale, a dial, pieces, a stack. Stems, zones, and piece ids come from the project's JSON, not from these files.

Each file is one kind: what problem it solves, when to use it, the taps, and what must not happen.

List them:

```bash
python3 scripts/match.py --guild games --list
```

How the round should feel, and how it sits in the page, is in [make](../make/README.md).

---

## 中文

能玩的小游戏种类。匹配一种，再把这一局放进页面。有的是文字选择。另一些的棋盘就是地图、画面、路、秤、刻度、零件或一摞。题干、区域和零件 id 来自项目自己的 JSON，不写在这些文件里。

每个文件是一种：它解决什么麻烦、何时用、怎么点、什么不能发生。

列出全部游戏卡片：

```bash
python3 scripts/match.py --guild games --list
```

这一局的手感，以及怎么放进页面，在 [make](../make/README.md)。
