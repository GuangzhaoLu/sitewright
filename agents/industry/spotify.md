# Spotify · 小队、支部、行当

公开来源：Henrik Kniberg & Anders Ivarsson, *Scaling Agile @ Spotify*（2012）[PDF](https://blog.crisp.se/wp-content/uploads/2012/11/SpotifyScaling.pdf)。Kniberg 事后多次说：**不要复制「Spotify 模型」**，那是当时的走法，不是框架。

## 原文四个单元

| 单元 | 大约规模 | 作用 |
|---|---|---|
| Squad 小队 | 6–12 | 跨职能，长期使命，自己选工作方式，能独立交付 |
| Tribe 部落 | <100 | 相关小队的孵化器 |
| Chapter 支部 | 同职能 | 同一工种的「小家庭」，带手艺和人事 |
| Guild 行当 | 自愿、跨组织 | 分享工具和做法（测试行当、Web 行当……） |

原则口头禅：松耦合、紧对齐。后来 Spotify 自己也改了组织，还把独立发布做成技术目标。

## 网页小站能用的

| 拿走 | Sitewright 里的落点 |
|---|---|
| 小队跨职能交付 | 发现波 / 交付波，不是按部门接力 |
| 支部 = 同一工种的标准 | 任务全文在 `agents/prompts/*.md`；`seats/` 只记边界 |
| 行当 = 共享做法 | `library/`，不是再雇一个「游戏经理」 |
| 松耦合 | 席位禁止越权（游戏设计不写生产 JS） |

## 不要用的

- 部落、100 人上限、部落长。
- 为每个 Guild 派常驻 agent。
- 「独立部署微服务」——和单目录静态站相反。
