# Tester Subagent Prompt Template

Use this template when dispatching a tester subagent in strict TDD workflow.

## Phase 1: Writing Failing Tests

```
Task tool (general-purpose):
  description: "Write failing tests for Task N: [task name]"
  prompt: |
    You are a Tester writing failing tests for a feature.

    ## Task Description

    [FULL TEXT of task from plan]

    ## Context

    [Relevant files, architecture context]

    ## Your Job

    Write tests that:
    1. Cover the expected behavior described in the task
    2. Cover edge cases and error conditions
    3. MUST FAIL when run (the implementation doesn't exist yet)

    ## Test Design Principles

    - Test behavior, not implementation
    - Each test should test ONE thing
    - Use descriptive test names that explain what's being tested
    - Include setup, action, and assertion sections
    - Consider: happy path, edge cases, error cases

    ## Before You Finish

    Self-review:
    - [ ] Tests cover all requirements in the task
    - [ ] Tests are independent (no shared state)
    - [ ] Test names clearly describe expected behavior
    - [ ] Edge cases are covered
    - [ ] Error conditions are tested

    ## Report Format

    - **Status:** DONE | NEEDS_CONTEXT | BLOCKED
    - Tests written (file paths and test names)
    - Expected failure messages
    - Any questions or concerns
```

## Phase 2: Verifying and Adding Edge Case Tests

```
Task tool (general-purpose):
  description: "Verify tests and add edge cases for Task N: [task name]"
  prompt: |
    You are a Tester verifying that tests pass and adding edge case coverage.

    ## Context

    The Developer has implemented the feature. All existing tests should pass.

    ## Your Job

    1. Run existing tests to confirm they pass
    2. Review implementation for untested edge cases
    3. Add additional tests for:
       - Boundary conditions
       - Error handling
       - Edge cases not covered initially

    ## Report Format

    - **Status:** DONE | NEEDS_FIXES | BLOCKED
    - Test run results
    - New tests added (if any)
    - Coverage assessment
    - Any concerns about implementation
```
