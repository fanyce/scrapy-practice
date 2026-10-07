# 贡献指南

感谢你愿意改进 Scrapy Practice。

## 开始开发

1. Fork 仓库并创建功能分支。
2. 创建虚拟环境并运行 `python -m pip install -e .`。
3. 保持改动小而清晰，并沿用现有项目结构和命名方式。
4. 提交前运行 `scrapy check` 和 `python -m compileall -q scrapy_practice`。
5. 在 Pull Request 中说明改动目的、验证方式和可能影响。

## 爬虫贡献要求

- 仅为允许自动访问的网站添加示例。
- 保持 `ROBOTSTXT_OBEY = True`，除非有明确且合法的理由。
- 设置合理的并发和下载间隔。
- 不提交 Cookie、Token、账号、个人信息或抓取结果。
- 尽量使用稳定、语义明确的选择器。

## 提交信息

建议使用简洁的 Conventional Commits 风格，例如：

```text
feat: add article spider
fix: handle missing publication date
docs: clarify local setup
```
