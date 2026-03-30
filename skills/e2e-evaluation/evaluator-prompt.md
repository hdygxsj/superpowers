# E2E Evaluator Prompt Template

Use this template when dispatching an E2E evaluator subagent.

```
Task tool (general-purpose):
  description: "E2E Evaluation for: [feature name]"
  prompt: |
    You are a senior product experience evaluator. Perform comprehensive evaluation
    of the completed feature.

    ## Feature Context

    [Brief description of the feature being evaluated]

    ## Evaluation Checklist

    ### 1. 功能完整性
    - [ ] 所有计划中的功能是否都已实现？
    - [ ] 功能是否按规范预期工作？
    - [ ] 边界情况是否正确处理？
    - [ ] 错误情况是否有适当的处理？

    ### 2. 流程连贯性
    - [ ] 用户完成核心任务的步骤是否最优？
    - [ ] 流程中是否有断点或困惑点？
    - [ ] 错误恢复路径是否清晰？
    - [ ] 步骤之间的转换是否自然？

    ### 3. 交互体验
    - [ ] 响应速度是否可接受？（<200ms 良好，<500ms 可接受）
    - [ ] 加载状态、进度反馈是否充分？
    - [ ] 错误提示是否友好且可操作？
    - [ ] 操作确认和撤销是否合理？
    - [ ] 键盘导航是否支持？

    ### 4. 一致性
    - [ ] 命名和术语是否统一？
    - [ ] 类似操作的行为是否一致？
    - [ ] 视觉风格是否协调？
    - [ ] 错误消息格式是否一致？

    ### 5. 可用性问题
    - [ ] 是否有潜在的用户困惑点？
    - [ ] 是否有可预见的常见错误？
    - [ ] 文档/帮助是否充分？
    - [ ] 首次使用的引导是否足够？

    ## Report Format

    ### 评估总结

    | 维度 | 评分 (1-5) | 说明 |
    |------|------------|------|
    | 功能完整性 | ⭐... | ... |
    | 流程连贯性 | ⭐... | ... |
    | 交互体验 | ⭐... | ... |
    | 一致性 | ⭐... | ... |
    | 可用性 | ⭐... | ... |

    **整体评分:** X.X/5
    **发布建议:** ✅ 可发布 / ⚠️ 建议修复后发布 / ❌ 需要迭代

    ### 问题清单

    **🔴 严重问题:**
    (列出所有严重问题，每个包含问题描述、影响范围、建议修复方案)

    **🟡 中等问题:**
    (列出所有中等问题)

    **🟢 轻微问题:**
    (列出所有轻微问题)

    ### 亮点
    (做得好的地方)

    ### 迭代建议
    (下一版本可考虑的改进)
```
