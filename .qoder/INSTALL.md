# Installing Superpowers for Qoder

## Prerequisites

- [Qoder](https://qoder.com) installed

## Step 1: 确认安装位置

**在开始安装前，请先询问用户：**

> Superpowers 可以安装到两个位置：
>
> 1. **用户目录** (`~/.qoder/`) — 全局生效，所有项目可用
> 2. **项目目录** (`.qoder/`) — 仅当前项目可用，可提交到版本控制
>
> 你想安装到哪里？

根据用户选择，执行下方对应的安装步骤。

---

## 选项 1: 用户目录安装 (`~/.qoder/`)

### Step 2: Clone the repository

```bash
git clone https://github.com/hdygxsj/superpowers.git ~/.qoder/superpowers
```

### Step 3: Create symlinks

**创建以下目录：**
- `~/.qoder/skills/` — Skills 安装目录
- `~/.qoder/agents/` — Agents 安装目录
- `~/.qoder/scripts/` — Scripts 安装目录

**安装 Skills：**
1. 将 `skills/` 目录下的所有技能 symlink 到 `~/.qoder/skills/`
2. 将 `.qoder/skills/` 目录下的 Qoder 专用技能 symlink 到 `~/.qoder/skills/`
3. **重要：** 如果 Qoder 专用技能与通用技能同名，先删除通用技能的 symlink，再创建 Qoder 专用技能的 symlink

**安装 Agents：**
- 将 `.qoder/agents/` 目录下的所有 agent 文件 symlink 到 `~/.qoder/agents/`

**安装 Scripts：**
- 将 `.qoder/scripts/` 目录下的所有脚本 symlink 到 `~/.qoder/scripts/`

### Step 4: Configure Hooks

Create hook script:

```bash
mkdir -p ~/.qoder/hooks
cat > ~/.qoder/hooks/superpowers-context.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail

SUPERPOWERS_ROOT=~/.qoder/superpowers

escape_for_json() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\n'/\\n}"
  s="${s//$'\r'/\\r}"
  s="${s//$'\t'/\\t}"
  printf '%s' "$s"
}

using_superpowers_content=$(cat "${SUPERPOWERS_ROOT}/skills/using-superpowers/SKILL.md" 2>&1 || echo "")
using_superpowers_escaped=$(escape_for_json "$using_superpowers_content")

cat << JSONEOF
{"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","additionalContext":"You have superpowers.\\n\\n**Below is the content of your 'superpowers:using-superpowers' skill:**\\n\\n${using_superpowers_escaped}"}}
JSONEOF
exit 0
EOF
chmod +x ~/.qoder/hooks/superpowers-context.sh
```

Add to `~/.qoder/settings.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{"type": "command", "command": "~/.qoder/hooks/superpowers-context.sh"}]
    }]
  }
}
```

### Step 5: Restart Qoder

用户目录安装完成！

---

## 选项 2: 项目目录安装 (`.qoder/`)

### Step 2: Clone to temporary location

```bash
git clone https://github.com/hdygxsj/superpowers.git /tmp/superpowers
```

### Step 3: Create project structure and symlinks

在项目根目录执行：

```bash
mkdir -p .qoder/skills .qoder/agents .qoder/hooks .qoder/scripts

# Core Skills (先安装通用技能)
for skill in /tmp/superpowers/skills/*/; do
  ln -sf "$skill" .qoder/skills/$(basename "$skill")
done

# Qoder-specific Skills (后安装，覆盖通用版本中的同名 skill)
for skill in /tmp/superpowers/.qoder/skills/*/; do
  name=$(basename "$skill")
  rm -rf .qoder/skills/"$name"  # 删除通用版本
  ln -sf "$skill" .qoder/skills/"$name"  # 安装 Qoder 版本
done

# Agents (use .qoder/agents/ for Qoder-optimized descriptions)
for agent in /tmp/superpowers/.qoder/agents/*.md; do
  ln -sf "$agent" .qoder/agents/
done

# Scripts (sandbox proxy, etc.)
for script in /tmp/superpowers/.qoder/scripts/*; do
  ln -sf "$script" .qoder/scripts/
done
```

### Step 4: Configure Hooks

Create hook script:

```bash
cat > .qoder/hooks/superpowers-context.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail

SUPERPOWERS_ROOT="/tmp/superpowers"

escape_for_json() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\n'/\\n}"
  s="${s//$'\r'/\\r}"
  s="${s//$'\t'/\\t}"
  printf '%s' "$s"
}

using_superpowers_content=$(cat "${SUPERPOWERS_ROOT}/skills/using-superpowers/SKILL.md" 2>&1 || echo "")
using_superpowers_escaped=$(escape_for_json "$using_superpowers_content")

cat << JSONEOF
{"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","additionalContext":"You have superpowers.\\n\\n**Below is the content of your 'superpowers:using-superpowers' skill:**\\n\\n${using_superpowers_escaped}"}}
JSONEOF
exit 0
EOF
chmod +x .qoder/hooks/superpowers-context.sh
```

Create `.qoder/settings.json`:

```bash
cat > .qoder/settings.json << 'EOF'
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{"type": "command", "command": ".qoder/hooks/superpowers-context.sh"}]
    }]
  }
}
EOF
```

### Step 5: Restart Qoder

项目目录安装完成！

---

## Updating

**用户目录安装：**
```bash
cd ~/.qoder/superpowers && git pull
```

**项目目录安装：**
```bash
cd /tmp/superpowers && git pull
```

## Usage

### Skills

```
/brainstorming
/writing-plans
/subagent-driven-development
```

### Agents

```
/developer
/tester
/spec-reviewer
/code-quality-reviewer
```

## Getting Help

- Full documentation: https://github.com/hdygxsj/superpowers/blob/main/docs/README.qoder.md
- Report issues: https://github.com/hdygxsj/superpowers/issues
