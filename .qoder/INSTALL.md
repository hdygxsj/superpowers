# Installing Superpowers for Qoder

## Prerequisites

- [Qoder](https://qoder.com) installed

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/hdygxsj/superpowers.git ~/.qoder/superpowers
```

### Step 2: Create symlinks

```bash
# Skills
mkdir -p ~/.qoder/skills
ln -s ~/.qoder/superpowers/skills ~/.qoder/skills/superpowers

# Agents
mkdir -p ~/.qoder/agents
ln -s ~/.qoder/superpowers/agents/*.md ~/.qoder/agents/

# Hooks (optional but recommended)
chmod +x ~/.qoder/superpowers/hooks/session-start
```

### Step 3: Configure Hooks (Required)

This injects Superpowers context into every conversation. Create a hook script:

```bash
mkdir -p ~/.qoder/hooks
cat > ~/.qoder/hooks/superpowers-context.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SUPERPOWERS_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)/superpowers"

# Read using-superpowers content
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

### Step 4: Restart Qoder

## Project-Level Installation

For project-specific installation:

```bash
git clone https://github.com/hdygxsj/superpowers.git /tmp/superpowers

# In your project root
mkdir -p .qoder/skills .qoder/agents .qoder/hooks
cp -r /tmp/superpowers/skills/* .qoder/skills/
cp -r /tmp/superpowers/agents/* .qoder/agents/

# Create hook script
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

# Configure hooks
cat > .qoder/settings.json << 'EOF'
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{"type": "command", "command": "$(pwd)/.qoder/hooks/superpowers-context.sh"}]
    }]
  }
}
EOF
```

## Updating

```bash
cd ~/.qoder/superpowers && git pull
```

## Usage

Skills activate automatically based on context. Or invoke manually:

```
/brainstorming
/writing-plans
/subagent-driven-development
```

## Getting Help

- Full documentation: https://github.com/hdygxsj/superpowers/blob/main/docs/README.qoder.md
- Report issues: https://github.com/hdygxsj/superpowers/issues
