# digital-human

可持续进化的数字人 Skill 工程（本地优先）。

## 功能
- 多源采集：IM、Wiki、本地文件
- 定时采集与本地归档
- 基础处理：解析、清洗、切分、去重、元数据
- Skill 蒸馏、版本化、加载、回滚
- CLI 调用 Skill
- FastAPI 对外服务

## 快速开始
```bash
cd digital-human
pip install -e .[dev]
cp .env.example .env
python -m digital_human.main
```

### CLI
```bash
digital-human list-skills
digital-human run-skill darwin "请总结最近素材"
digital-human collect
```

### API
```bash
uvicorn digital_human.api.server:app --reload
```

## 目录
工程目录按需求约定组织于 `digital-human/` 下。
