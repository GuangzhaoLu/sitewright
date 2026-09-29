## data.api-wall

## English

**The browser does not touch the database.** Problem: The connection string is written in a frontend script.

**When:** Any database that lives on a server.

**When not:** There is no server database (static files or `localStorage`).

**Steps:**

1. The page talks only to your own API. The database account, password, and host never enter the browser or git.
2. Who may read and who may edit is decided on the server. Hiding a button is not access control.
3. The database user has only the privileges the product needs. Do not run the site as an admin account.
4. Development and production use different databases and accounts.

**Don't:** Put the database address and password in a page script.

**Example:** Sitewright has not connected a production database. This card is here to stop the first person who wants to.

---

## 中文

**浏览器不连库.** 问题：连接串写在前端脚本里。

**何时用:** 任何放在服务端的库。

**何时不用:** 没有服务端库（静态文件或 `localStorage`）。

**步骤:**

1. 页面只请求你自己的 API。数据库账号、密码、主机不进浏览器，不进 git。
2. 谁能读、谁能改，在服务端判断。前端藏按钮不算数。
3. 数据库用户只有业务需要的权限，不用管理员账号跑网站。
4. 开发、线上用不同的库和账号。

**反例:** 在页面脚本里写数据库地址和密码。

**实例:** Sitewright 尚未接过线上库。这张卡用来拦住第一次有人要接的时候。
