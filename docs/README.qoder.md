# Superpowers for Qoder

Complete guide for using Superpowers with [Qoder](https://qoder.com).

## Quick Install

### Step 1: Clone the repository

```bash
git clone https://github.com/obra/superpowers.git ~/.qoder/superpowers
```

### Step 2: Create symlinks

```bash
# Skills (each skill as a separate symlink)
for skill in ~/.qoder/superpowers/skills/*/; do
  ln -s "$skill" ~/.qoder/skills/$(basename "$skill")
done

# Agents
for agent in ~/.qoder/superpowers/agents/*.md; do
  ln -sf "$agent" ~/.qoder/agents/
done
```

### Step 3: Configure Hooks (Required)

Create a hook script to inject Superpowers context:

```bash
mkdir -p ~/.qoder/hooks
cat > ~/.qoder/hooks/superpowers-context.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail

SUPERPOWERS_ROOT=~/.qoder/superpowers

# Escape string for JSON embedding
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

### Step 4: Restart Qoder IDE

### Method 2: Project-Level Installation

For project-specific installation:

```bash
git clone https://github.com/hdygxsj/superpowers.git /tmp/superpowers

# In your project root
mkdir -p .qoder/skills .qoder/agents .qoder/hooks

# Skills (each skill as a separate symlink)
for skill in /tmp/superpowers/skills/*/; do
  ln -s "$skill" .qoder/skills/$(basename "$skill")
done

# Agents (use .qoder/agents/ for Qoder-optimized descriptions)
for agent in /tmp/superpowers/.qoder/agents/*.md; do
  ln -sf "$agent" .qoder/agents/
done

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

### Method 3: Using create-skill (Qoder Built-in)

Qoder provides a built-in `create-skill` tool. While you can use it to create new skills, the recommended approach is to symlink the entire Superpowers skills directory as described above.

## Usage

### Activating Skills

Skills are activated automatically when:
- You mention a skill by name (e.g., "use brainstorming")
- The task matches a skill's description
- The `using-superpowers` skill directs Qoder to use one

### Manual Skill Invocation

```
/brainstorming
```

### Using Custom Agents

Custom agents are invoked with:

```
/code-reviewer
```

## Available Skills

| Skill | Description |
|-------|-------------|
| brainstorming | Socratic design refinement |
| writing-plans | Detailed implementation plans |
| executing-plans | Batch execution with checkpoints |
| subagent-driven-development | Fast iteration with two-stage review |
| test-driven-development | RED-GREEN-REFACTOR cycle |
| systematic-debugging | 4-phase root cause process |
| requesting-code-review | Pre-review checklist |
| receiving-code-review | Responding to feedback |
| finishing-a-development-branch | Merge/PR decision workflow |
| using-git-worktrees | Parallel development branches |
| writing-skills | Create new skills following best practices |

## Available Agents

| Agent | Description |
|-------|-------------|
| code-reviewer | Senior Code Reviewer for plan compliance and code quality |

## Hooks (Required)

Superpowers includes hooks to inject context into every conversation. Create a hook script:

```bash
mkdir -p ~/.qoder/hooks
cat > ~/.qoder/hooks/superpowers-context.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail

SUPERPOWERS_ROOT=~/.qoder/superpowers

# Escape string for JSON embedding
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

Add to your settings:

**User-level** (`~/.qoder/settings.json`):
```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{"type": "command", "command": "~/.qoder/hooks/superpowers-context.sh"}]
    }]
  }
}
```

**Project-level** (`.qoder/settings.json`):
```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{"type": "command", "command": "$(pwd)/.qoder/hooks/superpowers-context.sh"}]
    }]
  }
}
```

## Configuration

### Skills Configuration

Skills are discovered from:
- **User-level**: `~/.qoder/skills/{skill-name}/SKILL.md`
- **Project-level**: `.qoder/skills/{skill-name}/SKILL.md`

### Agents Configuration

Agents are loaded from:
- **User-level**: `~/.qoder/agents/{agentName}.md`
- **Project-level**: `.qoder/agents/{agentName}.md`

### Priority

When user-level and project-level have the same skill/agent, **project-level takes precedence**.

## Updating

```bash
cd ~/.qoder/superpowers && git pull
```

Skills and agents are loaded from the symlink, so updates take effect immediately.

## Uninstalling

```bash
# Remove symlinks
rm ~/.qoder/skills/superpowers
rm ~/.qoder/agents/code-reviewer.md

# Optionally remove the clone
rm -rf ~/.qoder/superpowers
```

## Troubleshooting

### Skills not showing up

1. Verify the symlink: `ls -la ~/.qoder/skills/superpowers`
2. Check skills exist: `ls ~/.qoder/superpowers/skills`
3. Restart Qoder — skills are discovered at startup

### Hooks not working

1. Ensure the hook script is executable:
   ```bash
   chmod +x ~/.qoder/hooks/superpowers-context.sh
   ```
2. Verify settings.json is valid JSON
3. Restart Qoder after config changes

### Windows Installation

On Windows, use junctions instead of symlinks:

```powershell
# Create directories
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.qoder\superpowers"
cmd /c mklink /J "$env:USERPROFILE\.qoder\skills\superpowers" "$env:USERPROFILE\.qoder\superpowers\skills"
cmd /c mklink /J "$env:USERPROFILE\.qoder\agents\code-reviewer" "$env:USERPROFILE\.qoder\superpowers\agents\code-reviewer"
```

## Getting Help

- Report issues: https://github.com/obra/superpowers/issues
- Qoder documentation: https://docs.qoder.com
- Main documentation: https://github.com/obra/superpowers
