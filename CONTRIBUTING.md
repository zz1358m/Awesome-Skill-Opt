# Contributing

Add papers whose optimized, selected, or evaluated object is an explicit, reusable **agent skill artifact** used by a frozen LLM agent. See the Scope section of the README for what is out of range.

1. Edit `data/papers.json`; do not edit the tables between the `GENERATED CATALOG` markers.
2. Use the exact title from a primary source (arXiv, OpenReview, proceedings). Give exactly one primary source per record: `arxiv_id`, or `openreview_id` for an anonymous submission without a public preprint.
3. Choose one category: `optimization`, `induction`, `transfer`, `routing`, `evaluation`, `internalization`, or `adjacent`.
4. Write one factual sentence in English and one in Chinese, based on the paper's own abstract. Do not copy abstracts, and do not report numbers you have not read in a primary source.
5. `date` is the first public date (`YYYY-MM-DD` for arXiv, `YYYY-MM` otherwise).
6. Link author-associated code only. Otherwise set `code_url` to `null` and `code_status` to `not located` (searched, none found) or `not checked`.
7. Set `venue` only for a confirmed venue, or to `ICLR 2027 submission` style labels for anonymous papers under review. Do not link a signed preprint to an anonymous submission of the same paper while it is under double-blind review.
8. Advance `last_checked`, then run `python scripts/render.py` and `python scripts/render.py --check` (Python 3.10+, no dependencies).
