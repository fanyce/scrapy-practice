# Scrapy Practice

[![CI](https://github.com/fanyce/scrapy-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/fanyce/scrapy-practice/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个用于学习 Scrapy、编写和调试爬虫的轻量示例项目。项目保留接近 Scrapy 官方模板的结构，适合作为练习和小型爬虫的起点。

## 功能

- 提供可直接运行的 Scrapy 项目骨架
- 包含基础爬虫示例
- 默认遵守 `robots.txt`
- 对单个域名限速，减少对目标站点的压力
- 通过 GitHub Actions 自动进行基础项目检查

## 内置爬虫

| 名称 | 目标 | 运行命令 |
| --- | --- | --- |
| `quote` | `quotes.toscrape.com` 教学站点 | `scrapy crawl quote` |
| `xidian` | 西安电子科技大学就业信息页 | `scrapy crawl xidian` |

目前示例爬虫主要用于演示请求和日志输出，后续可以逐步加入选择器、Item、Pipeline 和持久化逻辑。

## 快速开始

要求 Python 3.10 或更高版本。仓库使用 Python 3.13 作为本地开发版本。

```bash
git clone https://github.com/fanyce/scrapy-practice.git
cd scrapy-practice
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Windows PowerShell 激活虚拟环境：

```powershell
.venv\Scripts\Activate.ps1
```

确认项目可以正常加载：

```bash
scrapy list
scrapy check
```

## 常用命令

```bash
# 创建爬虫
scrapy genspider example example.com

# 运行爬虫
scrapy crawl quote

# 导出为 JSON
scrapy crawl quote -O output.json

# 交互式调试选择器
scrapy shell https://example.com

# 查看当前配置
scrapy settings --get BOT_NAME
```

## 项目结构

```text
scrapy-practice/
├── .github/workflows/ci.yml      # 持续集成检查
├── scrapy.cfg                    # Scrapy 项目入口
├── pyproject.toml                # 项目元数据与依赖
└── scrapy_practice/
    ├── items.py                  # 结构化数据模型
    ├── middlewares.py            # 请求和响应中间件
    ├── pipelines.py              # 数据处理与持久化流程
    ├── settings.py               # 全局配置
    └── spiders/                  # 爬虫代码
```

## 合规使用

本项目仅用于学习和技术研究。运行爬虫前，请确认目标网站允许自动访问，并遵守其 `robots.txt`、服务条款、访问频率限制以及适用法律。请勿采集个人敏感信息、绕过访问控制或对服务造成压力。

## 参与贡献

欢迎提交 Issue 和 Pull Request。开始前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

本项目使用 [MIT License](LICENSE)。
