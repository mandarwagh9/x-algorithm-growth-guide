# Evaluation Methodology

This skill was tested against a baseline (no skill) across 3 real-world scenarios to verify it improves accuracy.

## Scenarios

| ID | Scenario | What It Tests |
|----|----------|---------------|
| 1 | **Creator seeking growth advice** | Practical strategy recommendations tied to algorithm weights |
| 2 | **Social media manager seeking technical explanation** | Depth of algorithm knowledge (pipeline, scoring, filtering) |
| 3 | **User asking to settle conflicting advice** | Myth-busting with code evidence (frequency, likes vs replies, etc.) |

## Methodology

Each scenario was run **twice**: once **with the skill** loaded, and once as a **baseline** (no skill). Each run was graded on 10 binary assertions covering:

- Correct engagement weights (Like=1.0, Reply=0.5, Retweet=0.3, Dwell=0.2)
- Author diversity decay mechanism
- OON (out-of-network) penalty
- Code file references to the x-algorithm repo
- Negative signal awareness
- Actionable advice quality
- Pipeline stage accuracy

## Results

| Scenario | With Skill | Without Skill |
|----------|-----------|---------------|
| Creator Growth Advice | 10/10 | 1/10 |
| Technical Explanation | 10/10 | 0/10 |
| Debunking Myths | 10/10 | 1/10 |
| **Total** | **30/30 (100%)** | **2/30 (6.7%)** |

Without the skill, AI agents default to the old 2023 Twitter algorithm knowledge (MaskNet, SimClusters, "replies > likes is highest weight"). With this skill, they correctly reference the current 2026 x-algorithm (Grok-based transformer with Like=1.0x as the highest signal).

## Reproducibility

The full evaluation artifacts are in `iteration-1/`:

```
iteration-1/
├── benchmark.json              # Aggregate benchmark statistics
├── benchmark.md                # Human-readable benchmark summary
├── review.html                 # Interactive review viewer
├── eval-1/
│   ├── with_skill/run-1/       # Creator growth advice with skill
│   └── without_skill/run-1/    # Creator growth advice baseline
├── eval-2/
│   ├── with_skill/run-1/       # Technical explanation with skill
│   └── without_skill/run-1/    # Technical explanation baseline
└── eval-3/
    ├── with_skill/run-1/       # Debunking myths with skill
    └── without_skill/run-1/    # Debunking myths baseline
```
