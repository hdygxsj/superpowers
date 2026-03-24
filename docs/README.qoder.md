# Superpowers for Qoder

Complete guide for using Superpowers with [Qoder](https://qoder.com).

## Quick Install

### Step 1: Clone the repository

```bash
git clone https://github.com/obra/superpowers.git ~/.qoder/superpowers
```

### Step 2: Create symlinks for skills and agents

```bash
# Skills symlink
mkdir -p ~/.qoder/skills
ln -s ~/.qoder/superpowers/skills ~/.qoder/skills/superpowers

# Agents symlink
mkdir -p ~/.qoder/agents
ln -s ~/.qoder/superpowers/agents/*.md ~/.qoder/agents/
```

### Step 3: Configure Hooks (Optional but Recommended)

Add session-start hook to inject Superpowers context on startup:

**User-level** (`~/.qoder/settings.json`):
```json
{
  "hooks": {
    "sessionStart": [
      {
        "matcher": "startup|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "~/.qoder/superpowers/hooks/session-start"
          }
        ]
      }
    ]
  }
}
```

Make sure the hook script is executable:
```bash
chmod +x ~/.qoder/superpowers/hooks/session-start
```

### Step 4: Restart Qoder IDE

### Method 2: Project-Level Installation

For project-specific installation, add skills to your project's `.qoder` directory:

```bash
# In your project root
mkdir -p .qoder/skills .qoder/agents

# Copy skills
cp -r /path/to/superpowers/skills/* .qoder/skills/

# Copy agents
cp -r /path/to/superpowers/agents/* .qoder/agents/
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

## Hooks (Optional)

Superpowers includes session-start hooks. To enable them, add to your Qoder settings:

**User-level** (`~/.qoder/settings.json`):
```json
{
  "hooks": {
    "sessionStart": [
      {
        "matcher": "startup|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "~/.qoder/superpowers/hooks/session-start"
          }
        ]
      }
    ]
  }
}
```

**Project-level** (`.qoder/settings.json`):
```json
{
  "hooks": {
    "sessionStart": [
      {
        "matcher": "startup|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "<absolute-path-to-superpowers>/hooks/session-start"
          }
        ]
      }
    ]
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
   chmod +x ~/.qoder/superpowers/hooks/session-start
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
