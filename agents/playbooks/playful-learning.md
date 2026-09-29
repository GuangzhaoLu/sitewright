# Playbook · 寓教于乐

学习站、科普站、学院站：先玩一局再读。题库和红线只属于当前项目，不要从别的站拷过来。

## 何时用

用户说要游戏 + 知识、寓教于乐、互动小游戏、academy。

## 冻结物

必须有 `00-BRIEF.md` + `01-GAMES.md`。局数 3–5。路径：**枢纽 → 一局 → 当场解释 → 深读**。

默认栈：静态 HTML/CSS/JS，进度 `localStorage`。项目已有栈则跟项目。

## 席位

发现波：PM、视觉、游戏设计、内容。交付波：枢纽、玩法、插图。验收：QA。数据默认不上，除非简报写了持久化。人数上限见 [FLOW.md](../FLOW.md)。

Librarian 在 S1 先匹配 `game.sort-trays` / `game.parallel-place` / `game.myth-trap` / `game.term-match` 等，不要默认再发明第五种循环。

档案在项目的 `agents/sitewright/`。提示词用 Sitewright 的 `agents/prompts/`，填好后拷进项目。不要另建 `agents/playful/`。

## 硬教训（本 playbook 加的）

- 一局一个观念
- 流行误解写进规格当陷阱
- 无账号、无惩罚计时、无抽奖

个人 Skill `playful-learning-site` 只加这几条学习站规则。流程、席位和提示词以 Sitewright 为准。
