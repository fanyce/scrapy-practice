# Scrapy Practice

用于学习和编写 Scrapy 爬虫的基础项目。

## 环境

- Python 3.13
- Scrapy 2.19.0
- 项目虚拟环境：`.venv`

## 初始化

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

VS Code 已配置为默认使用 `.venv/bin/python`。

## 创建爬虫

```bash
scrapy genspider example example.com
```

生成的爬虫位于 `scrapy_practice/spiders/`。

## 常用命令

```bash
# 查看爬虫列表
scrapy list

# 运行爬虫
scrapy crawl example

# 导出 JSON
scrapy crawl example -O output.json

# 交互式调试选择器
scrapy shell https://example.com

# 检查项目配置
scrapy settings --get BOT_NAME
```

## 目录说明

```text
scrapy-practice/
├── scrapy.cfg                    # Scrapy 项目入口配置
├── pyproject.toml                # Python 项目与依赖配置
└── scrapy_practice/
    ├── items.py                  # 结构化数据模型
    ├── middlewares.py            # 请求和响应中间件
    ├── pipelines.py              # 数据清洗与持久化流程
    ├── settings.py               # Scrapy 全局配置
    └── spiders/                  # 爬虫业务代码
```

