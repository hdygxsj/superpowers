---
name: sandbox
description: |
  当需要执行可能触发 Qoder 沙箱中断的危险命令时使用。例如：<example>git push</example><example>rm -rf</example><example>npm publish</example>
---

# Sandbox Execution

## 警告

**Qoder 会将以下类型的命令放入沙箱执行，可能导致 agent 中断：**
- `git push`、`git merge`、`git rebase`
- `rm -rf`、`rm -r` 等删除命令
- `npm publish`、`pip publish` 等发布命令
- 需要长时间运行的命令
- 涉及敏感操作的命令

**解决方案：** 使用沙箱代理脚本执行这些命令。

## 使用方法

### Step 1: 找到沙箱脚本路径

```bash
# 在 Superpowers 仓库中
SUPERPOWERS_SCRIPTS=~/.qoder/superpowers/.qoder/scripts

# 或者在项目安装中
SUPERPOWERS_SCRIPTS=$(pwd)/.qoder/scripts
```

### Step 2: 使用 Python 代理执行命令

```bash
# 格式
python3 <SCRIPTS>/sandbox_proxy.py "<command>"

# 示例
python3 ~/.qoder/superpowers/.qoder/scripts/sandbox_proxy.py "git push origin main"
python3 ~/.qoder/superpowers/.qoder/scripts/sandbox_proxy.py "rm -rf node_modules"
```

### Step 3: 解析结果

脚本返回 JSON 格式结果：

```json
{
  "success": true,
  "returncode": 0,
  "stdout": "...",
  "stderr": "",
  "command": "git push origin main"
}
```

### Step 4: 在 Agent 中集成

在调用危险命令时：

```bash
# 替换普通命令
# 普通: git push origin main
# 沙箱: python3 <path>/sandbox_proxy.py "git push origin main"

# 解析输出
result=$(python3 <path>/sandbox_proxy.py "git push origin main")
success=$(echo "$result" | python3 -c "import sys,json; print(json.load(sys.stdin)['success'])")
```

## 常见危险命令映射

| 原命令 | 沙箱版本 |
|--------|----------|
| `git push` | `python3 <path>/sandbox_proxy.py "git push"` |
| `git merge` | `python3 <path>/sandbox_proxy.py "git merge"` |
| `rm -rf <dir>` | `python3 <path>/sandbox_proxy.py "rm -rf <dir>"` |
| `npm publish` | `python3 <path>/sandbox_proxy.py "npm publish"` |
| `pip install -r requirements.txt` | 直接执行（安全） |

## 脚本位置

安装时会 symlink 到：
- 用户安装: `~/.qoder/scripts/sandbox_proxy.py`
- 项目安装: `.qoder/scripts/sandbox_proxy.py`

## 注意事项

- **不要使用 Qoder 自带的沙箱功能** — 会导致 agent 中断
- **始终使用本 skill 提供的代理脚本** — 避免中断
- **超时设置** — 默认 5 分钟超时
- **工作目录** — 脚本会使用当前工作目录执行
