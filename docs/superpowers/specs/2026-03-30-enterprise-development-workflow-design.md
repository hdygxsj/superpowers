# Enterprise Development Workflow Design

企业级开发工作流增强设计规范

## 概述

为 Superpowers 添加企业级开发能力，包括：
1. **文档沉淀** — 每个功能开发和测试形成完整文档记录
2. **角色分离** — 开发、测试、代码审查由独立 Agent 执行
3. **端到端评估** — 全方位评估功能、流程、交互体验
4. **规范记录** — 自动记录讨论中产生的项目规范
5. **知识索引** — AGENTS.md 作为项目知识唯一入口

## 目标

- 让 AI IDE 能够系统化地完成企业级项目开发
- 形成可追溯的开发文档和知识沉淀
- 通过角色分离提高代码质量
- 建立完整的开发闭环（设计 → 计划 → 开发 → 测试 → 评估 → 迭代）

---

## 设计详情

### 1. 文档沉淀机制

#### 1.1 报告目录结构

每个功能开发完成后，生成以下结构：

```
docs/superpowers/reports/YYYY-MM-DD-<feature-name>/
├── decisions.md      # 决策日志（实时追加）
├── implementation.md # 实现报告（完成时生成）
├── tests.md          # 测试文档（完成时生成）
├── evaluation.md     # E2E 评估报告（完成时生成）
└── summary.md        # 汇总报告（完成时生成）
```

#### 1.2 命名规范

- 日期格式：`YYYY-MM-DD`
- 功能名：从对应的 plan 文件名提取

#### 1.3 文档关联

```
docs/superpowers/
├── specs/YYYY-MM-DD-<feature>-design.md   ← 设计规范
├── plans/YYYY-MM-DD-<feature>.md          ← 实现计划
└── reports/YYYY-MM-DD-<feature>/          ← 开发报告
```

#### 1.4 各文档内容

**decisions.md（实时追加）**
- 触发时机：DONE_WITH_CONCERNS、BLOCKED 后重新调度、调试完成、人工决策
- 内容：问题/背景、考虑的选项、最终决策、影响

**tests.md（完成时生成）**
- 测试覆盖率表格
- 单元测试和集成测试用例清单
- E2E 测试部分
- 测试命令和输出

**implementation.md（完成时生成）**
- 变更文件清单
- 关键实现说明
- 与计划的偏差
- 后续建议

**evaluation.md（E2E 评估后生成）**
- 五维度评分（功能完整性、流程连贯性、交互体验、一致性、可用性）
- 问题清单（按严重程度分类）
- 迭代决策

**summary.md（完成时生成）**
- 文档索引
- 功能摘要
- 关键指标
- 学习要点

---

### 2. 多角色协作（严格 TDD）

#### 2.1 角色定义

| 角色 | 职责 | Prompt 模板 |
|------|------|-------------|
| **Tester** | 编写失败测试、验证测试通过、补充边界测试 | `tester-prompt.md` |
| **Developer** | 写最小代码使测试通过 | `developer-prompt.md` |
| **Code Reviewer** | 审查代码质量和规范合规性 | `code-quality-reviewer-prompt.md` |
| **E2E Evaluator** | 全面评估功能、流程、体验 | `evaluator-prompt.md` |

#### 2.2 严格 TDD 流程

```
1. Tester 编写失败测试
      ↓
2. 运行测试，确认失败（RED）
      ↓
3. Developer 写最小代码
      ↓
4. 运行测试，确认通过（GREEN）
      ↓
5. Tester 验证并补充边界测试
      ↓
6. Code Reviewer 审查代码质量
      ↓
7. 记录决策，标记任务完成
```

#### 2.3 角色隔离原则

- 每个角色是独立的子代理
- 上下文由控制器精确策划
- 角色之间不继承会话历史

---

### 3. 端到端评估

#### 3.1 评估维度

| 维度 | 评估内容 |
|------|----------|
| 功能完整性 | 所有功能是否按预期工作 |
| 流程连贯性 | 用户旅程是否顺畅 |
| 交互体验 | 响应速度、错误提示、边界处理 |
| 一致性 | UI 风格、命名、行为一致性 |
| 可用性 | 潜在困惑点、常见错误预防 |

#### 3.2 评估流程

1. 检查 Playwright 安装（如无则安装）
2. 运行自动化 E2E 测试
3. 分派 E2E Evaluator 进行全面评估
4. 生成评估报告
5. 迭代决策点：
   - 进入迭代（修复问题后重评）
   - 接受当前状态（继续完成）
   - 只修复严重问题

#### 3.3 问题严重程度

| 级别 | 定义 | 处理方式 |
|------|------|----------|
| 🔴 严重 | 影响核心功能 | 必须修复 |
| 🟡 中等 | 影响用户体验 | 建议修复 |
| 🟢 轻微 | 优化建议 | 可选修复 |

---

### 4. 规范记录（convention-tracking）

#### 4.1 触发时机

- 用户明确表达偏好
- 讨论确定技术选型
- 约定命名规范、代码风格
- 确定流程或工作方式

#### 4.2 规范分类

| 类别 | 存放位置 |
|------|----------|
| 代码规范 | `docs/conventions/code-style.md` |
| 命名约定 | `docs/conventions/naming.md` |
| Git 工作流 | `docs/conventions/git-workflow.md` |
| 测试规范 | `docs/conventions/testing.md` |
| API 设计 | `docs/conventions/api-design.md` |

#### 4.3 规范格式

```markdown
## [规范名称]

**来源:** [日期] / [功能名称]
**状态:** 生效中 / 已废弃

### 规范内容
<具体描述>

### 背景
<为什么确定这个规范>

### 示例
<正确/错误示例>
```

---

### 5. AGENTS.md 索引机制

#### 5.1 位置与作用

- **位置：** 项目根目录 `AGENTS.md`
- **作用：** 项目知识的唯一入口，AI Agent 启动时必须读取

#### 5.2 结构

```markdown
# Project Knowledge Index

## 项目规范
| 规范 | 位置 | 说明 |
|------|------|------|
| ... | ... | ... |

## 设计文档
| 功能 | 规范 | 计划 | 报告 |
|------|------|------|------|
| ... | ... | ... | ... |

## 快速链接
- Superpowers 技能: `skills/`
- 开发报告: `docs/superpowers/reports/`
- 项目规范: `docs/conventions/`
```

#### 5.3 启动检查

`using-superpowers` 在项目启动时：
1. 检查 `AGENTS.md` 是否存在
2. 如存在：读取并遵循已记录的规范
3. 如不存在：提示用户创建

#### 5.4 自动维护

| 事件 | 更新内容 |
|------|----------|
| brainstorming 完成 | 添加 spec 链接 |
| writing-plans 完成 | 添加 plan 链接 |
| finishing-a-development-branch 完成 | 添加 report 链接 |
| convention-tracking 记录新规范 | 添加规范链接 |

---

## 技能改造清单

### 新增 Skills

| 文件 | 说明 |
|------|------|
| `skills/convention-tracking/SKILL.md` | 规范记录技能 |
| `skills/e2e-evaluation/SKILL.md` | 端到端评估技能 |
| `skills/e2e-evaluation/evaluator-prompt.md` | E2E 评估者 Prompt |
| `skills/development-documentation/report-templates.md` | 报告模板参考 |

### 新增 Prompts

| 文件 | 说明 |
|------|------|
| `skills/subagent-driven-development/tester-prompt.md` | Tester 角色 Prompt |
| `skills/subagent-driven-development/developer-prompt.md` | Developer 角色 Prompt（原 implementer-prompt.md 重命名） |

### 修改 Skills

| 文件 | 改动 |
|------|------|
| `skills/using-superpowers/SKILL.md` | 新增 AGENTS.md 启动检查 |
| `skills/subagent-driven-development/SKILL.md` | 新增严格 TDD 流程 + 文档记录 |
| `skills/executing-plans/SKILL.md` | 新增文档记录 |
| `skills/systematic-debugging/SKILL.md` | 新增调试记录 |
| `skills/finishing-a-development-branch/SKILL.md` | 新增 E2E 评估 + 报告生成 + AGENTS.md 更新 |
| `skills/brainstorming/SKILL.md` | 新增 AGENTS.md 更新 |
| `skills/writing-plans/SKILL.md` | 新增 AGENTS.md 更新 |

### 新增目录结构

| 路径 | 说明 |
|------|------|
| `docs/conventions/` | 项目规范目录 |
| `docs/superpowers/reports/` | 开发报告目录 |
| `AGENTS.md` | 项目知识索引（模板） |

---

## 完整工作流

```
项目启动
└─ using-superpowers：检查并读取 AGENTS.md
        │
        ▼
brainstorming
├─ 产出：spec 文档
├─ 更新：AGENTS.md
└─ 触发：convention-tracking（如有规范讨论）
        │
        ▼
writing-plans
├─ 产出：plan 文档
└─ 更新：AGENTS.md
        │
        ▼
subagent-driven-development
├─ 初始化：reports 目录
├─ 实时记录：decisions.md
├─ 严格 TDD：Tester → Developer → Code Reviewer
└─ 触发：convention-tracking（如有规范讨论）
        │
        ▼
e2e-evaluation
├─ 产出：evaluation.md
└─ 决策：是否迭代
        │
        ▼
finishing-a-development-branch
├─ 产出：implementation.md, tests.md, summary.md
└─ 更新：AGENTS.md
```

---

## 设计决策记录

| 决策 | 选择 | 理由 |
|------|------|------|
| 文档组织方式 | 按功能分离的目录结构 | 清晰、易于追溯 |
| 实现方式 | 扩展现有 Skill（方案 B 全面覆盖） | 所有执行路径都有文档沉淀 |
| 文档生成时机 | 混合模式 | 实时记录关键决策，完成时汇总 |
| TDD 协作模式 | 严格 TDD 分工 | 完全符合 TDD 精神，角色职责清晰 |
| E2E 评估范围 | 全面评估（功能+流程+体验） | 不仅是自动化测试，需要迭代决策 |
