## web.progress-localstorage

## English

**One progress contract.** Problem: One `localStorage` key, a JSON object, boolean values. Call `mark` only when the spec's win condition is true. `write(false)` does not appear on "play again." When reading, accept only `=== true`.

The home page and the hub paint progress from the same `data-*` attributes, so there are not two counters.

---

## 中文

**一份进度合同.** 问题：单一 `localStorage` 键，JSON 对象，值为布尔。`mark` 只在规格通关时调用。`write(false)` 不要出现在「再来一局」。读的时候只认 `=== true`。

首页和枢纽用同一套 `data-*` 刷进度，避免两套计数。
