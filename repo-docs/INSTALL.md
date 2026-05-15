# Installation Guide

## Prerequisites

- **Claude Code**, **OpenCode**, or any AI coding tool that supports loading skills from SKILL.md files
- **git** (for cloning the repo)
- **curl** or **wget** (for downloading the .skill file)

## Method 1: Clone the Repo (Recommended for Development)

```bash
git clone https://github.com/mandarwagh9/x-algorithm-growth-guide.git
```

Then in your AI tool, load the skill:
- **Claude Code:** Use the `/skill` command pointing to the SKILL.md path
- **OpenCode:** Reference it in your `AGENTS.md` or use the skill tool
- **Cursor/Other:** Check your tool's documentation for skill loading

## Method 2: Download the .skill File (Easiest)

1. Go to the [Releases page](https://github.com/mandarwagh9/x-algorithm-growth-guide/releases)
2. Download the latest `x-algorithm-growth-guide.skill`
3. Copy it to your skills directory:
   ```bash
   cp ~/Downloads/x-algorithm-growth-guide.skill ~/.claude/skills/
   ```
4. Restart your AI tool — the skill will be available automatically

## Method 3: Manual Copy

If you prefer not to clone the entire repo:

```bash
# Download just the SKILL.md
curl -O https://raw.githubusercontent.com/mandarwagh9/x-algorithm-growth-guide/main/SKILL.md
```

Then reference `SKILL.md` directly in your tool.

## Verification

To verify the skill is loaded correctly, ask your AI tool:

> "What does the X algorithm weight more — likes or replies? Cite your source."

Expected response should mention:
- Like weight: 1.0x (highest signal)
- Reply weight: 0.5x
- Reference to `phoenix/run_pipeline.py` from the x-algorithm repo

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Skill doesn't load | Ensure the SKILL.md path is correct and readable |
| Wrong weights given | Verify you're using the latest version of the skill |
| .skill file not recognized | Check that your AI tool supports the `.skill` format |
