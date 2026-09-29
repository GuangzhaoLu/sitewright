# Card format

## English

Each card has one row in `catalog.json`. The body is one file in that guild's directory. The filename is the part of the id after the dot. The heading is the full id.

The body is two blocks: English, then Chinese. They say the same thing.

```json
{
  "id": "game.sort-trays",
  "guild": "games",
  "title": "分层托盘 / Sort trays",
  "problem": "Materials of different reliability are spread out as if they were the same",
  "teaches": ["classification", "source-criticism"],
  "interaction": ["tap", "trays"],
  "tags": ["分层", "托盘", "点按", "史料", "传说"],
  "when": "The reader has to sort the materials by hand",
  "when_not": "There are only two piles and the right answer is already printed on them",
  "effort": "M",
  "mobile": "tap",
  "file": "games/kinds/sort-trays.md"
}
```

| Key | Meaning |
|---|---|
| id | Stable short prefix plus filename, cited from the brief. The prefix is not the directory name: `game`→`games`, `img`→`images`, `vid`→`video`, `fe`→`frontend`, `res`→`research`, `data`→`data`, `web`→`web`. Do not rename ids to the full directory name |
| guild | `games` `images` `video` `frontend` `data` `research` `web` |
| title | Chinese name, then English name |
| problem | The trouble on the reader's side |
| teaches / interaction | Short English tags for search |
| tags | Chinese or English; `match.py` scans them |
| when / when_not | Use it, or do not |
| effort | S a few hours / M one round / L more than one round |
| mobile | `tap` `tap+place` `keyboard-ok` `avoid-drag-only` |
| file | Path relative to `library/`, such as `games/kinds/sort-trays.md` |

A body has steps, a counterexample, and an example. The example is a general situation, or it says Sitewright has not used this yet. Do not put a domain's proper names into `when` as if they were a general rule.

---

## 中文

每张卡片在 `catalog.json` 有一条。正文是该行当目录里的一个文件，文件名是 id 点号后面的那段，标题用完整 id。

正文先是一整块英文，再是一整块中文，说的是同一件事。

```json
{
  "id": "game.sort-trays",
  "guild": "games",
  "title": "分层托盘 / Sort trays",
  "problem": "材料可靠度不同，读者却平铺在同一眼",
  "teaches": ["classification", "source-criticism"],
  "interaction": ["tap", "trays"],
  "tags": ["分层", "托盘", "点按", "史料", "传说"],
  "when": "必须亲手把材料分开",
  "when_not": "只有两堆且对错已写在脸上",
  "effort": "M",
  "mobile": "tap",
  "file": "games/kinds/sort-trays.md"
}
```

| 键 | 含义 |
|---|---|
| id | 稳定短前缀 + 文件名，简报里引用。前缀不是目录名：`game`→`games`，`img`→`images`，`vid`→`video`，`fe`→`frontend`，`res`→`research`，`data`→`data`，`web`→`web`。不要改成目录全名 |
| guild | `games` `images` `video` `frontend` `data` `research` `web` |
| title | 中文名，再加英文名 |
| problem | 玩家侧的麻烦 |
| teaches / interaction | 英文短标签，便于检索 |
| tags | 中文或英文都行，`match.py` 会扫 |
| when / when_not | 采用与否 |
| effort | S 数小时 / M 一轮 / L 不止一轮 |
| mobile | `tap` `tap+place` `keyboard-ok` `avoid-drag-only` |
| file | 相对 `library/` 的路径，如 `games/kinds/sort-trays.md` |

正文至少有：步骤、反例、实例。实例写通用情景，或写「Sitewright 尚未用过」。不要把领域专名写进 `when` 当作通用条件。
