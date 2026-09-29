# Frontend

## English

How a page is arranged, how it is read, and how it can be finished on a narrow screen. The engineering contract (static first, progress, tap targets, questions in JSON) stays in [web](../web/README.md). Whether to add a database is in [data](../data/README.md).

WCAG 2.2 success criterion 2.5.8 asks for a target of at least 24×24 CSS pixels, or enough space beside it. The stricter 2.5.5 is 44×44. Sitewright still sizes primary controls at about 44px (`web.tap-44`). The New York Times graphics desk asks what question the page must answer, then draws.

Suggested search words: one job per page, outline, type size, measure, narrow screen, form, performance.

List the cards:

```bash
python3 scripts/match.py --guild frontend --list
```

---

## 中文

页面怎么排、怎么读、怎么在窄屏上完成。工程合同（静态优先、进度、点按热区、题在 JSON）仍在 [web](../web/README.md)。要不要数据库在 [data](../data/README.md)。

依据：WCAG 2.2 的 2.5.8 要求可点目标至少 24×24 CSS 像素（或与邻项有足够间距）；更严的 2.5.5 是 44×44。Sitewright 主按钮仍按约 44px（见 `web.tap-44`）。《纽约时报》图形组先问这一页要回答的问题，再画。

检索词：一页一事、大纲、字号、行长、窄屏、表单、性能。

列出卡片：

```bash
python3 scripts/match.py --guild frontend --list
```
