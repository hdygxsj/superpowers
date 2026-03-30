---
name: development-documentation
description: Reference templates for development reports - used by subagent-driven-development and finishing-a-development-branch
---

# Development Report Templates

报告模板参考，供 subagent-driven-development、executing-plans、systematic-debugging、finishing-a-development-branch 技能使用。

## 目录结构

```
docs/superpowers/reports/YYYY-MM-DD-<feature-name>/
├── decisions.md      # 实时追加
├── implementation.md # 完成时生成
├── tests.md          # 完成时生成
├── evaluation.md     # E2E 评估后生成
└── summary.md        # 完成时生成
```

## 报告目录命名

从 plan 文件名提取：
- Plan: `docs/superpowers/plans/2026-03-30-user-authentication.md`
- Report: `docs/superpowers/reports/2026-03-30-user-authentication/`

---

## decisions.md 模板

实时追加，每次遇到关键决策、问题或选择时记录。

```markdown
# 决策日志

## [YYYY-MM-DD HH:MM] 任务 N: <任务名称>

### 问题/背景
<遇到了什么问题或需要做什么决策>

### 考虑的选项
1. <选项A> — <优缺点>
2. <选项B> — <优缺点>

### 决策
<最终选择及理由>

### 影响
<这个决策对后续开发的影响>

---
```

**触发时机:**
- 实现者报告 DONE_WITH_CONCERNS
- 任务经历 BLOCKED → 重新调度
- systematic-debugging 完成根因分析
- 任何需要人工介入的决策点

---

## tests.md 模板

完成时生成，记录测试覆盖和结果。

```markdown
# 测试报告

**生成时间:** YYYY-MM-DD HH:MM
**关联计划:** [<plan-name>](../plans/YYYY-MM-DD-<feature>.md)

## 测试覆盖

| 模块 | 测试用例数 | 通过 | 失败 | 覆盖率 |
|------|-----------|------|------|--------|
| ... | ... | ... | ... | ...% |

## 单元测试用例

- [x] `test_xxx` — 验证 xxx 功能
- [x] `test_yyy` — 验证 yyy 功能

## 集成测试用例

- [x] `test_integration_xxx` — 验证 xxx 集成

## 端到端测试

**Playwright 版本:** x.x.x

### E2E 测试用例
- [x] `login-flow.spec.ts` — 用户登录流程
- [x] `checkout.spec.ts` — 购物结账流程

## 测试命令

```bash
<实际运行的测试命令>
```

## 测试输出

```
<测试运行的关键输出>
```
```

---

## implementation.md 模板

完成时生成，记录实现细节。

```markdown
# 实现报告

**完成时间:** YYYY-MM-DD HH:MM
**关联规范:** [<spec-name>](../specs/YYYY-MM-DD-<feature>-design.md)
**关联计划:** [<plan-name>](../plans/YYYY-MM-DD-<feature>.md)

## 变更概览

| 文件 | 变更类型 | 说明 |
|------|----------|------|
| `src/xxx.ts` | 新增 | xxx 实现 |
| `src/yyy.ts` | 修改 | 添加 yyy 功能 |

## 关键实现

### <模块1名称>
<实现要点、核心逻辑说明>

### <模块2名称>
<实现要点、核心逻辑说明>

## 与计划的偏差

<如有偏离计划的地方，说明原因；如无则写"无">

## 后续建议

<未来可能的优化方向>
```

---

## evaluation.md 模板

E2E 评估后生成，记录全面评估结果。

```markdown
# 端到端评估报告

**评估时间:** YYYY-MM-DD HH:MM
**评估者:** E2E Evaluator Agent

## 评估总结

| 维度 | 评分 | 说明 |
|------|------|------|
| 功能完整性 | ⭐⭐⭐⭐⭐ | 所有功能按预期工作 |
| 流程连贯性 | ⭐⭐⭐⭐☆ | ... |
| 交互体验 | ⭐⭐⭐⭐☆ | ... |
| 一致性 | ⭐⭐⭐⭐⭐ | ... |
| 可用性 | ⭐⭐⭐⭐☆ | ... |

**整体评分:** X.X/5
**发布建议:** ✅ 可发布 / ⚠️ 建议修复后发布 / ❌ 需要迭代

## 问题清单

### 🔴 严重问题（必须修复）
<无 / 问题列表>

### 🟡 中等问题（建议修复）
1. **问题:** <问题描述>
   - **影响:** <影响范围>
   - **建议:** <修复建议>

### 🟢 轻微问题（可选修复）
1. **问题:** <问题描述>
   - **建议:** <优化建议>

## 亮点

<做得好的地方>

## 迭代决策

**是否需要迭代:** 是 / 否

**如需迭代，任务清单:**
- [ ] <迭代任务1>
- [ ] <迭代任务2>

**预计迭代工作量:** ~X 小时
```

---

## summary.md 模板

完成时生成，汇总所有文档。

```markdown
# 功能开发总结: <功能名称>

**开发周期:** YYYY-MM-DD ~ YYYY-MM-DD
**状态:** ✅ 完成 / ⚠️ 部分完成

## 文档索引

| 文档 | 说明 |
|------|------|
| [设计规范](../specs/YYYY-MM-DD-<feature>-design.md) | 需求和架构设计 |
| [实现计划](../plans/YYYY-MM-DD-<feature>.md) | 任务分解和执行步骤 |
| [实现报告](./implementation.md) | 代码变更记录 |
| [测试报告](./tests.md) | 测试覆盖和结果 |
| [评估报告](./evaluation.md) | E2E 评估结果 |
| [决策日志](./decisions.md) | 开发过程中的关键决策 |

## 功能摘要

<一段话描述这个功能做了什么>

## 关键指标

| 指标 | 值 |
|------|-----|
| 任务数 | N |
| 修改文件数 | N |
| 新增代码行 | ~N |
| 测试用例数 | N |
| 测试覆盖率 | N% |
| E2E 评分 | X.X/5 |

## 学习要点

<这次开发中值得记录的经验教训>
```

---

## 使用指南

### 何时创建报告目录

- **subagent-driven-development:** 读取 plan 后立即创建
- **executing-plans:** 开始执行前创建

### 何时追加 decisions.md

- 实现者报告 DONE_WITH_CONCERNS
- 任务经历 BLOCKED → 重新调度
- systematic-debugging 完成根因分析
- 任何需要人工介入的决策

### 何时生成完整报告

- **finishing-a-development-branch** Step 1.5
