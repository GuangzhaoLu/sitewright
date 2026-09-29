# How to fill a prompt

## English

Copy a prompt into the **project** at `agents/sitewright/prompts/`, then fill it. Do not edit the masters in this repo unless you are changing Sitewright itself.

| Placeholder | Replace with |
|---|---|
| `{{ROOT}}` | site root |
| `{{AGENTS}}` | project archive: `{ROOT}/agents/sitewright` |
| `{{QUERY}}` | this round's search, for the librarian |
| `{{NAME}}` | product name, templates only |

Send the filled text, plus: read the project's `00-BRIEF.md` first.

---

## 中文

复制到**项目**的 `agents/sitewright/prompts/` 再填。不要改 Sitewright 仓库里的母本，除非你正在改 Sitewright 本身。

| 占位 | 换成 |
|---|---|
| `{{ROOT}}` | 站点根目录 |
| `{{AGENTS}}` | 项目内存档：`{ROOT}/agents/sitewright` |
| `{{QUERY}}` | Librarian 这一轮的检索句 |
| `{{NAME}}` | 只出现在 templates 里，产品名 |

发给 agent 的是填好的全文，外加一句：先读项目的 `00-BRIEF.md`。
