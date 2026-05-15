# X Algorithm Growth Guide

An evidence-based skill for Claude Code / OpenCode that reveals exactly how the X "For You" algorithm works — and what content strategies actually drive more views — based on the actual open-source code at [github.com/xai-org/x-algorithm](https://github.com/xai-org/x-algorithm).

## What This Skill Does

When you ask about growing on X, understanding the algorithm, or optimizing content, this skill provides **code-backed answers** — not speculation. It knows:

- The exact scoring weights: **Like (1.0x)**, Reply (0.5x), Retweet (0.3x), Dwell Time (0.2x)
- The **author diversity penalty** (exponential decay: 1.0x -> 0.65x -> 0.48x)
- The **OON (Out-of-Network) penalty** for non-followed content
- The **14+ filter types** that remove content before it ever reaches the scorer
- The **Grox banger classifier** (quality threshold >= 0.4)
- The **Phoenix Grok-based transformer** and candidate isolation masking
- All **14+ action prediction heads** (positive and negative signals)

No guesswork. Everything is traced to a specific file and line in the x-algorithm codebase.

## How to Use

### Option 1: Directory install (recommended for development)

Clone this repo and point your AI tool at the SKILL.md:

```bash
git clone https://github.com/mandarwagh9/x-algorithm-growth-guide.git
```

Then in Claude Code / OpenCode, use the skill tool:
```
/skill path/to/x-algorithm-growth-guide
```

### Option 2: Install the .skill file (easiest)

Download the latest `.skill` file from [Releases](https://github.com/mandarwagh9/x-algorithm-growth-guide/releases) and place it in your skills directory:

```bash
cp x-algorithm-growth-guide.skill ~/.claude/skills/
```

### Option 3: Reference in AGENTS.md

```markdown
## Skills
- **x-algorithm-growth-guide**: Located at `path/to/x-algorithm-growth-guide/SKILL.md`
```

## Example Prompts

- "How does the X algorithm actually work? I want specific weights and signals."
- "Why are my posts stuck at 50-100 impressions? What should I change?"
- "Is it better to optimize for likes or replies? What does the code say?"
- "How often should I post? Does the algorithm penalize frequency?"
- "What's the OON penalty and how do I overcome it?"

## Evaluation Results

This skill was tested against a baseline (no skill) across 3 real-world scenarios:

| Metric | With Skill | Without Skill | Delta |
|--------|-----------|---------------|-------|
| Pass Rate | 100% (30/30) | 6.7% (2/30) | **+93%** |

Without the skill, AI agents default to the old 2023 Twitter algorithm (MaskNet, SimClusters, "replies > likes"). With this skill, they correctly reference the 2026 x-algorithm (Grok transformer, correct Like=1.0x weight).

[Full evaluation details](evals/README.md)

## Project Structure

```
x-algorithm-growth-guide/
├── SKILL.md                    # The skill (load this)
├── README.md                   # This file
├── LICENSE                     # Apache 2.0
├── repo-docs/
│   └── INSTALL.md              # Detailed install guide
├── evals/
│   ├── evals.json              # Test prompts and assertions
│   └── README.md               # Evaluation methodology
└── references/
    └── algorithm-sources.md    # Key files in x-algorithm repo
```

## License

Apache 2.0 — same as the x-algorithm project this derives from.
