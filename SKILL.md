---
name: x-algorithm-growth-guide
description: >-
  Analyzes the open-source X/Twitter recommendation algorithm (github.com/xai-org/x-algorithm) to give creators and developers actionable, evidence-backed advice on getting more views, engagement, and reach on X. Use this whenever the user asks about growing on X, understanding the X algorithm, optimizing posts for X, getting more impressions/views/followers on X, how X ranks content, or what drives reach on the For You feed. Also use when the user mentions tweet/post performance, engagement signals, or virality on X. This skill provides both practical growth strategies AND the technical code-level reasoning behind them.
---

# X Algorithm Growth Guide

## Overview

This skill translates the open-source X "For You" algorithm (github.com/xai-org/x-algorithm) into practical, actionable advice. It reveals **exactly what the algorithm rewards and penalizes** based on the actual production code — not speculation.

The core insight: X's algorithm is a **weighted scoring system** driven by a Grok-based transformer that predicts 19 engagement actions. Final relevance score = Σ(weight × P(action)). Every recommendation is the output of a deterministic pipeline: sources → hydrators → filters → scorers → selector.

## What the Algorithm Rewards (Ranked by Signal Strength)

### Primary Signals (Direct Score Impact)

These are the actions the model predicts and weights. Higher engagement on your posts directly increases their score.

| Action | Weight | Why It Matters |
|--------|--------|----------------|
| **Like (Favorite)** | **1.0×** | Highest individual weight. Single most powerful engagement signal. |
| **Reply** | **0.5×** | Drives conversation. High value because replies signal deep engagement. |
| **Retweet** | **0.3×** | Amplification signal. Less weight than reply — the algorithm values conversation over distribution. |
| **Dwell time** | **0.2×** | How long someone pauses on your post. Rewards content that holds attention. |
| **Share (DM / copy link)** | Positive | High-intent organic distribution. |
| **Video Quality View** | Thresholded | Only counts if video watched past minimum duration. |
| **Profile click** | Positive | Clicking your name/avatar to visit your profile. |
| **Photo expand** | Positive | Clicking to expand an image in your post. |
| **Link click** | Positive | Clicking a link in your post. |
| **Follow from post** | Strong implicit | If someone follows you after seeing a post, it's a strong quality signal. |

### Structural Advantages

These aren't scored directly but shape whether your content gets seen at all.

- **Being in-network (followed)**: Out-of-network (OON) candidates get multiplied by a penalty factor < 1.0. Posts from accounts you follow always have a structural scoring advantage.
- **Novelty**: The `PreviouslySeenPostsFilter` and `PreviouslyServedPostsFilter` remove already-seen content. Each post gets one shot at the feed.
- **Author diversity**: Multiple posts from the same author in a single feed are penalized by exponential decay (1.0× → ~0.65× → ~0.48×). Quality over frequency.
- **Freshness**: The `AgeFilter` removes posts older than a configurable threshold (likely 24-48h). Old posts are not shown at all, not just downranked.
- **"Banger" quality**: Grox runs a VLM classifier — posts with `quality_score ≥ 0.4` get flagged as high-quality. This feeds into the Grok side of content understanding.

### The OON (Out-of-Network) Discovery Path

The critical path for growth: how the algorithm shows your content to people who don't follow you.

```
User engages with Topic X → PhoenixRetrieval finds similar content → 
User's action sequence trains the model → Your content on Topic X gets retrieved →
PhoenixScorer scores it → If score is high enough, it appears in For You feed
```

Your content reaches non-followers when:
1. You post about topics consistent with your profile's engagement history
2. Your content gets quick engagement from followers (training the model)
3. The engagement signals on your post are strong enough to overcome the OON penalty

## What the Algorithm Penalizes (Suppression Signals)

### Direct Negative Signals

The model has **dedicated prediction heads** for these. High probability = actively pushed down.

| Signal | Impact |
|--------|--------|
| **"Not interested"** | Strong negative. If users mark your content as not interested, reach drops. |
| **Block** | Very strong negative. Full disconnection. |
| **Mute** | Very strong negative. Users opting out of your content. |
| **Report** | Very strong negative + potential policy review. |
| **No dwell (scrolled past)** | Implicit rejection. If people scroll past your post without pausing, it signals low relevance. |

### What Gets Filtered Out Entirely

These posts never reach the scorer — they're removed before scoring:

- **Self-tweets** — Your own posts don't appear in your own For You feed
- **Old content** — Past the age threshold
- **Already seen / served** — Deduplicated across sessions
- **Spam / slop** — Classified by Grox's VLM spam detection
- **Safety violations** — Visibility filtered for Violence, Adult, Hate, etc.
- **Muted keywords** — Content matching what the user has muted
- **Blocked/muted authors** — Either direction (you block them or they block you)

### Implicit Penalties

- **Low follower count replies** — Skipped entirely ("low blast radius"). Replies where both the replier and the target have low follower counts don't get ranked.
- **Protected accounts** — Excluded from content understanding pipelines (embeddings, spam detection, etc.)
- **Out-of-network**: Always penalized by OON weight factor (< 1.0) compared to in-network content.

## Actionable Growth Strategies (Code-Backed)

### 1. Optimize for Likes (1.0× weight)

The simplest, highest-impact action. Like is the single heaviest weight in the scoring equation. Posts that get likes get the most algorithmic boost.

**Strategy**: Ask questions, make relatable statements, create shareable reactions. The like prediction head is the primary scoring signal.

### 2. Drive Replies, Not Just Retweets (0.5× vs 0.3×)

Replies carry 67% more weight than retweets. The algorithm values conversation over amplification. Content that sparks debate, questions, or discussion outperforms content that just spreads.

**Strategy**: End posts with a question or call for opinions. Use polls. Create content that invites response. Avoid "broadcast-only" content.

### 3. Hold Attention (Dwell Time, 0.2×)

Dwell time is explicitly weighted. Content where people pause and read gets a direct scoring boost. The longer someone dwells, the stronger the signal.

**Strategy**: Write engaging hooks. Use formatting (line breaks, bullet points) that makes text scannable but substantive. Avoid content so short it's consumed instantly.

### 4. Quality Over Frequency

The author diversity mechanism applies exponential decay per additional post from the same author. First post: 1.0×. Second: ~0.65×. Third: ~0.48×. Posting 3x in rapid succession means each subsequent post gets half the score.

**Strategy**: Space out your posts. Each post competes independently — posting too frequently cannibalizes your own reach. One high-quality post outperforms three mediocre ones.

### 5. Avoid Negative Signals At All Costs

The model has dedicated negative prediction heads. A single "not interested" click on a post has more impact than multiple likes, because negative signals are sparse and therefore highly informative.

**Strategy**: Don't bait-and-switch. Don't post misleading content that causes people to react negatively. If your content generates blocks/mutes/reports, the algorithm learns to never show it. Stay authentic to your audience.

### 6. Topic Consistency for Discovery

The out-of-network retrieval (Phoenix) finds content based on your engagement history's topic distribution. The model retrieves posts from your understood topic areas.

**Strategy**: Consistently post within 1-3 topic areas that define your presence. The retrieval system needs stable topic signals to surface your content to non-followers who engage with those topics. Topic-hopping confuses the retrieval model.

### 7. Post Fresh Content

The `AgeFilter` removes old posts. And `PreviouslySeenPostsFilter` removes already-seen content. You can't coast on old posts — each post gets its moment.

**Strategy**: Regular posting cadence matters. Old content won't resurface organically to the same audience. If something performed well, create a follow-up rather than resharing.

### 8. Early Engagement Matters Most

The engagement sequence used by the Phoenix model weights recent interactions more heavily. Early engagement trains the model that your content is relevant now.

**Strategy**: Post when your followers are active. Respond quickly to replies (which drives more replies). Early engagement velocity signals relevance to the retrieval and ranking stages.

### 9. Video Quality Over Quantity

Video Quality View (VQV) is thresholded — only counts if watched past `min_video_duration_ms`. Short, low-retention videos don't get the video signal.

**Strategy**: Make videos that hold attention past the threshold. Hook viewers in the first seconds. Longer watch time = stronger VQV signal = higher score.

### 10. The "Not Interested" Trap

The biggest reach killer is accumulating "not interested" clicks. Unlike blocks/mutes which are absolute, "not interested" subtly informs the model to suppress your content type.

**Strategy**: Read the room. If a certain content type consistently gets negative feedback, pivot. The algorithm is telling you something about audience-content fit.

## Technical Architecture Reference

### Pipeline (from code)

```
gRPC request → HomeMixerServer
  → QueryHydrators (21 parallel): user history, following, blocked, muted, topics, etc.
  → Sources (6 parallel): Thunder (in-network), Phoenix (OON retrieval), Topics, MOE, etc.
  → Hydrators (18 parallel): core data, author info, engagement counts, brand safety, etc.
  → Filters (14 sequential): duplicates, age, self-post, muted keywords, blocked, etc.
  → Scorers (3 sequential):
      1. PhoenixScorer — Grok transformer predicts 14+ action probabilities per candidate
      2. RankingScorer — weighted linear combination + author diversity + OON penalty
      3. VMRanker (optional) — DPP-based diversity reranking
  → Selector — sort by final score, top-K
  → PostSelectionFilters — visibility, safety, conversation dedup
```

### Grox Content Understanding

Runs alongside the ranking pipeline to classify content quality:

- **Banger classifier** — VLM scores posts 0–1 (threshold ≥ 0.4)
- **Spam detection** — VLM evaluates reply spam probability
- **Safety/PTOS** — Two-stage: category detection → policy-specific assessment (7 policy categories)
- **Multimodal embeddings** — Text + image + video embeddings for semantic search

## Evidence Sources

All claims in this skill are derived from reading the actual open-source code at github.com/xai-org/x-algorithm. Key files:

- `phoenix/run_pipeline.py` — Scoring weights (line ~80-100: FAV_WEIGHT=1.0, REPLY_WEIGHT=0.5, RT_WEIGHT=0.3, DWELL_WEIGHT=0.2)
- `home-mixer/candidate_pipeline/phoenix_candidate_pipeline.rs` — Full pipeline implementation with filters, scorers, hydrators
- `home-mixer/scorers/ranking_scorer.rs` — Scoring weights with positive/negative signals, OON factors, author diversity decay
- `grox/classifiers/content/banger_initial_screen.py` — Quality classification (threshold ≥ 0.4)
- `grox/classifiers/content/spam.py` — Spam detection via VLM
- `grox/classifiers/content/safety_ptos.py` — Safety policy classification
- `home-mixer/filters/` — All filter implementations
