---
name: subagent-driven-development
description: |
  使用 Qoder 预置的 subagent (/developer, /tester, /spec-reviewer, /code-quality-reviewer) 执行计划任务。
  触发：<example>开始执行计划</example><example>分派 subagent 执行任务</example><example>多角色协作开发</example>
---

# Qoder Subagent-Driven Development

本技能专门为 Qoder 设计，使用预置的 subagent 执行任务。

## 架构

```
主控 (Main)
    ├── /tester (Step 1: 写失败测试)
    ├── /developer (Step 2: 实现最小代码)
    ├── /spec-reviewer (Step 3: 验证规范合规)
    └── /code-quality-reviewer (Step 4: 审查代码质量)
```

## 角色定义

| 角色 | 调用命令 | 职责 |
|------|----------|------|
| **Tester** | `/tester` | 编写失败的测试用例 |
| **Developer** | `/developer` | 实现最小代码让测试通过 |
| **Spec Reviewer** | `/spec-reviewer` | 验证实现是否符合计划规范 |
| **Code Quality Reviewer** | `/code-quality-reviewer` | 审查代码质量和最佳实践 |

## 工作流程

### Step 1: 准备计划

1. 读取实现计划（`docs/superpowers/plans/`）
2. 列出所有任务
3. 确定任务执行顺序

### Step 2: 任务循环

对每个任务执行以下流程：

```
┌─────────────────────────────────────────────────────────────┐
│                    任务 N: <任务名称>                         │
├─────────────────────────────────────────────────────────────┤
│  1. Tester: /tester                                        │
│     → 编写会失败的测试                                        │
│     → 运行确认测试失败 (RED)                                  │
│                                                             │
│  2. Developer: /developer                                  │
│     → 阅读测试要求                                           │
│     → 实现最小代码让测试通过                                   │
│     → 运行确认测试通过 (GREEN)                                │
│     → 必要时重构 (REFACTOR)                                  │
│                                                             │
│  3. Spec Reviewer: /spec-reviewer                           │
│     → 读取实际代码                                           │
│     → 与任务要求逐项对比                                      │
│     → 报告合规性                                             │
│     → 如有问题 → Developer 修复 → 重新审查                    │
│                                                             │
│  4. Code Quality Reviewer: /code-quality-reviewer           │
│     → 仅在规范审查通过后进行                                   │
│     → 审查代码组织、可读性、健壮性                             │
│     → 如有问题 → Developer 修复 → 重新审查                    │
│                                                             │
│  5. 提交代码                                                │
│     git add <files>                                         │
│     git commit -m "feat: <任务描述>"                         │
└─────────────────────────────────────────────────────────────┘
```

### Step 3: 任务间检查点

每个任务完成后，向用户报告：

```
## 任务 N 完成

**状态:** ✅ 通过 | ❌ 需修复

**测试:** [通过数量]/[总数]
**规范审查:** ✅ 合规 / ❌ 有问题
**代码质量:** ✅ 通过 / ❌ 需改进

[详细报告]
```

询问用户是否继续下一个任务。

### Step 4: 全部完成

所有任务完成后：

1. 汇总所有任务的测试结果
2. 确认测试覆盖率
3. 报告整体完成状态
4. 询问用户下一步操作（合并/PR/保持分支）

## 调用示例

```
用户: 开始执行计划 task-3

主控: 开始执行任务 3...

主控: Step 1 - 调用 /tester 编写测试
→ Tester 编写失败测试
→ 运行测试确认失败

主控: Step 2 - 调用 /developer 实现
→ Developer 阅读测试
→ Developer 实现最小代码
→ 运行测试确认通过

主控: Step 3 - 调用 /spec-reviewer 验证
→ Spec Reviewer 读取代码
→ Spec Reviewer 对比任务要求
→ 报告: ✅ 规范合规

主控: Step 4 - 调用 /code-quality-reviewer 审查
→ Code Quality Reviewer 检查代码
→ 报告: ✅ 质量通过

主控: 提交代码
→ git commit

任务 3 完成。是否继续任务 4？
```

## 报告格式

每个 agent 完成后应报告：

```
## <Agent> 报告

**状态:** DONE | DONE_WITH_CONCERNS | BLOCKED

**做了什么:**
- 具体行动列表

**结果:**
- 测试结果/审查结果

**修改文件:**
- 文件列表

**问题/建议:**
- 如有
```

## 注意事项

- **严格顺序:** Tester → Developer → Spec Reviewer → Code Quality Reviewer
- **不跳过审查:** 即使时间紧迫，规范审查和质量审查不能省略
- **自我审查:** Developer 在报告前应自我检查代码
- **可以 Block:** 任何 agent 遇到无法解决的问题可以报告 BLOCKED
- **小步提交:** 每个任务完成后立即提交
