# Algorithm Source References

All claims in this skill are derived from reading the open-source code at [github.com/xai-org/x-algorithm](https://github.com/xai-org/x-algorithm).

## Scoring Weights
- **File**: `phoenix/run_pipeline.py` (~L80-100)
- **Weights**: Like=1.0, Reply=0.5, Retweet=0.3, Dwell=0.2
- **Details**: The scoring equation used in the demo pipeline

## Author Diversity Decay
- **File**: `home-mixer/scorers/ranking_scorer.rs`
- **Mechanism**: Exponential decay per additional post from same author
- **Effect**: 1st post=1.0x, 2nd=~0.65x, 3rd=~0.48x

## Out-of-Network (OON) Penalty
- **File**: `home-mixer/scorers/ranking_scorer.rs`
- **Mechanism**: Out-of-network score multiplied by OON_WEIGHT_FACTOR (< 1.0)

## Filter Pipeline
- **Directory**: `home-mixer/filters/`
- **Filters**: AgeFilter, SelfTweetFilter, MutedKeywordFilter, AuthorSocialgraphFilter, PreviouslySeenPostsFilter, PreviouslyServedPostsFilter, DropDuplicatesFilter, VideoFilter, TopicIdsFilter, etc.

## Post-Selection Filters
- **Directory**: `home-mixer/filters/`
- **Filters**: VFFilter (visibility), AncillaryVFFilter, DedupConversationFilter

## Grox Content Understanding
- **File**: `grox/classifiers/content/banger_initial_screen.py`
- **Signal**: `quality_score >= 0.4` = flagged as banger/high-quality

## Phoenix Transformer (Ranking Model)
- **Files**: `phoenix/grok.py`, `phoenix/recsys_model.py`
- **Architecture**: Grok-1 derived, Grouped Query Attention, SwiGLU gated FFN, double RMSNorm pre-norm, RoPE, zero-initialized params

## Phoenix Retrieval Model
- **File**: `phoenix/recsys_retrieval_model.py`
- **Architecture**: Two-tower model (user tower + candidate tower), dot product similarity, L2-normalized embeddings

## Action Types
- **File**: `phoenix/run_pipeline.py`
- **Signals**: 14+ discrete actions predicted per candidate: favorite(1.0x), reply(0.5x), retweet(0.3x), dwell(0.2x), quote, video_quality_view, click, profile_click, photo_expand, share, follow_author, and negative heads (not_interested, block, mute, report)

## Home Mixer Pipeline
- **File**: `home-mixer/server.rs`
- **Role**: Orchestration layer, runs all pipeline stages via `CandidatePipeline::execute()`

## Home Mixer Query Hydrators
- **Directory**: `home-mixer/query_hydrators/`
- **Hydrators**: 21 parallel hydrators for following lists, blocked users, action sequences, bloom filters, Geo-IP, topics, etc.

## Candidate Pipeline Framework
- **File**: `candidate-pipeline/candidate_pipeline.rs`
- **Role**: Generic trait-based pipeline framework with Source, Hydrator, Filter, Scorer, Selector, SideEffect traits
