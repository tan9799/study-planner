# 学习规划助手 Skill

## 简介
基于 AI Agent Skills 规范的学习规划工具。通过自然语言交互，自动生成个性化学习计划，支持：
- 难度标记（🔴高 / 🟡中 / 🟢低）
- 优先级排序（考试 > 作业 > 复习 > 预习）
- iCal 日历导出
- 学习进度追踪
- 遗忘曲线复习提醒

## 安装方法
1. 将本文件夹复制到：  
   - Claude Code: `~/.claude/skills/`  
   - Cursor: `.cursor/skills/`  
   - Trae: `~/.trae/skills/`
2. 重启 IDE 或重新打开 AI 对话。

## 使用示例
帮我规划学习，每天晚7-9点有空，课程：数学、英语，下周二数学考试（难）。导出日历。

text

## 文件结构
- `SKILL.md`：AI 执行指令（核心）
- `references/`：学习科学参考资料
- `assets/`：模板文件
- `examples/`：示例对话
- `scripts/`：辅助脚本

## 许可证
MIT