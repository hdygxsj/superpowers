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

This injects Superpowers context into every conversation. Add to `~/.qoder/settings.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{"type": "command", "command": "~/.qoder/superpowers/hooks/session-start"}]
    }]
  }
}
```

Make sure the hook script is executable:
```bash
chmod +x ~/.qoder/superpowers/hooks/session-start
```

### Step 4: Restart Qoder

## Project-Level Installation

For project-specific installation, copy skills and agents to your project:

```bash
git clone https://github.com/hdygxsj/superpowers.git /tmp/superpowers

# In your project root
mkdir -p .qoder/skills .qoder/agents
cp -r /tmp/superpowers/skills/* .qoder/skills/
cp -r /tmp/superpowers/agents/* .qoder/agents/

# Configure hooks (use absolute path)
cat >> .qoder/settings.json << 'EOF'
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{"type": "command", "command": "/tmp/superpowers/hooks/session-start"}]
    }]
  }
}
EOF
```

> **Note:** Project-level hooks use absolute paths. Team members should adjust the path to their local clone location.

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
