# Awesome Skill Optimization for LLM Agents

**English** | [简体中文](README_zh.md)

A curated collection of work on **optimizing agent skills**: reusable, text-space procedural artifacts (for example `SKILL.md` packages) that are loaded by a frozen LLM agent at inference time. The list follows a skill through its lifecycle: how it is induced from experience, evolved under feedback, moved across models and harnesses, selected and exposed at run time, and evaluated.

**Last literature check: 2026-10-11 · 28 papers.**

Most entries are recent preprints. Entries labeled *ICLR 2027 submission* are anonymous papers under review, described from their public abstracts only; the label does not indicate acceptance. Contributions are summarized from abstracts and are not independent reproductions. Reported results remain specific to each paper's models, harnesses, and benchmarks.

## Contents

- [Skill evolution and optimization](#optimization)
- [Skill induction from experience](#induction)
- [Cross-model and cross-harness transfer](#transfer)
- [Retrieval, selection, and exposure](#routing)
- [Benchmarks and empirical studies](#evaluation)
- [Adjacent work](#adjacent)
- [Scope](#scope)
- [Machine-readable catalog](data/papers.json) · [Contributing](CONTRIBUTING.md)

<!-- GENERATED CATALOG:START -->
<a id="optimization"></a>

## Skill evolution and optimization

| Date | Work | Contribution | Resources |
| --- | --- | --- | --- |
| 2026-10 | **COBRA-Skills** — COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization | Formulates skill optimization as budgeted sequential optimization over an evolving candidate space, using contextual-bandit prioritization to decide which candidates receive costly execution-based evaluation. | [paper](https://openreview.net/forum?id=6XFoqlavXz) · ICLR 2027 submission |
| 2026-10 | **SkillNEO** — SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills | Argues that a partially repaired skill can stay low-scoring until later edits land, and introduces non-elitist evolutionary optimization that keeps developing intermediate versions using comparative execution evidence. | [paper](https://openreview.net/forum?id=DScGkPg0NR) · ICLR 2027 submission |
| 2026-09-18 | **GraphSkillEvo** — GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills | Represents skills as graph-structured natural-language artifacts to give explicit workflow-level guidance and to constrain the search space, and optimizes them with evolutionary search. | [paper](https://arxiv.org/abs/2609.21749) · [ICLR 2027 submission](https://openreview.net/forum?id=FrghfkhvZh) |
| 2026-09-08 | **SkillAdam** — SkillAdam: Stable and Efficient Skill Evolution for Agents | Targets unstable and inefficient skill self-evolution through two principles: direction stability (effective corrections accumulate across iterations) and update adaptivity (the scope of a revision follows the consistency of feedback). | [paper](https://arxiv.org/abs/2609.08944) · [ICLR 2027 submission](https://openreview.net/forum?id=PQv8PT4UGn) |
| 2026-07-29 | **SkillMentor** — SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis | Studies blind-spot diagnosis as a learnable capability separate from execution by training a Mentor policy while excluding executor updates and human supervision as sources of improvement. | [paper](https://arxiv.org/abs/2607.27360) |
| 2026-07-06 | **MetaSkill-Evolve** — MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution | Makes skill self-improvement recursive with a two-timescale design in which the improvement procedure itself is evolved alongside the task skill instead of being authored once and held fixed. | [paper](https://arxiv.org/abs/2607.05297) |
| 2026-05-31 | **SkillAdaptor** — SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories | Training-free, step-level skill adaptation: for a failed trajectory it locates the first actionable fault step, attributes it to candidate skills, and applies targeted updates under explicit acceptance checks with a frozen backbone. | [paper](https://arxiv.org/abs/2606.01311) |
| 2026-05-22 | **SkillOpt** — SkillOpt: Executive Strategy for Self-Evolving Agent Skills | Treats a skill as the trainable external state of a frozen agent: a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on one skill document and accepts an edit only if a held-out validation score strictly improves. | [paper](https://arxiv.org/abs/2605.23904) |

<a id="induction"></a>

## Skill induction from experience

| Date | Work | Contribution | Resources |
| --- | --- | --- | --- |
| 2026-09-04 | **Trace2Tower** — Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents | Abstracts step-level interactions into canonical events, builds a graph from semantic compatibility, transition dynamics, and outcome evidence, and applies a contrastive spectral decomposition to distill a multi-level skill hierarchy. | [paper](https://arxiv.org/abs/2609.05261) |
| 2026-08-27 | **WikiSkill** — WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution | Co-evolves agent skills with a persistent wiki, separating raw execution experience, accumulated knowledge, and executable skills so that later skill updates can build on consolidated insights. | [paper](https://arxiv.org/abs/2608.27454) · [ICLR 2027 submission](https://openreview.net/forum?id=eENzccuqfn) |
| 2026-03-26 | **Trace2Skill** — Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills | Consolidates many execution trajectories in parallel into a unified skill directory through inductive reasoning, either deepening human-written skills or building skills from weak LLM-generated drafts. | [paper](https://arxiv.org/abs/2603.25158) |

<a id="transfer"></a>

## Cross-model and cross-harness transfer

| Date | Work | Contribution | Resources |
| --- | --- | --- | --- |
| 2026-10 | **SkillProbe** — One Skill, Many Models: Learning Representation Compatibility from Sparse Behavioral Tests | A budgeted framework that diagnoses model-specific preferences over semantically equivalent skill representations before adaptation, using a bank of 156 matched probes over 14 instruction and executable factors and a hierarchical Bayesian profile to choose the next probe. | [paper](https://openreview.net/forum?id=wRCOe7Vsp1) · ICLR 2027 submission |
| 2026-10 | **Skill Transfer** — Skill Transfer: Adapting Agent Skills from Strong to Weak Agents | Hypothesizes that a strong model silently supplies procedural steps that a skill leaves implicit and that a weak model omits, and formalizes closing this gap when adapting skills from strong to weak agents. | [paper](https://openreview.net/forum?id=LD4Zo7u7Jr) · ICLR 2027 submission |
| 2026-10 | **CMRF** — Cross-Model Reproductive Fitness: Evolving Transferable Skills across Model Hosts | A transfer-aware evolutionary framework that evaluates skills on heterogeneous model–harness configurations during evolution, instead of optimizing on one primary host and measuring transfer afterwards. | [paper](https://openreview.net/forum?id=L18vEjanZr) · ICLR 2027 submission |
| 2026-10 | **HEIRS** — Beyond the Final Skill: Revaluing Skill Evolution History After Executor Replacement | Keeps the history of skill versions produced by evolution and, when the executor model is replaced, selects one unchanged archived version through target-side screening and confirmation. | [paper](https://openreview.net/forum?id=Ds8Nz1GuuQ) · ICLR 2027 submission |
| 2026-05-29 | **MASA** — Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents | Shows in controlled experiments that a skill helping one backbone can harm another, and adapts skills to each target backbone without changing agent weights, starting from a hierarchical skill evolution pipeline. | [paper](https://arxiv.org/abs/2605.30723) · [ICLR 2027 submission](https://openreview.net/forum?id=W0XuwkomQP) |
| 2026-05-05 | **SkCC** — SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents | A skill compiler built around SkIR, a strongly typed intermediate representation that separates skill semantics from framework-specific formatting to address cross-framework portability and security. | [paper](https://arxiv.org/abs/2605.03353) |
| 2026-04-03 | **SkVM** — SkVM: Revisiting Language VM for Skills across Heterogenous LLMs and Harnesses | Treats skills as code and LLMs as heterogeneous processors: decomposes a skill's requirements into primitive capabilities, measures how well each model–harness pair supports them, and compiles skills against these capability profiles. | [paper](https://arxiv.org/abs/2604.03088) |

<a id="routing"></a>

## Retrieval, selection, and exposure

| Date | Work | Contribution | Resources |
| --- | --- | --- | --- |
| 2026-09-07 | **SkillAlign** — SkillAlign: Aligning Skill Interfaces for LLM-based Agents | Represents candidate skills as multi-view procedural cards and renders them through alternative exposure interfaces (full instructions, hints, compressed summaries, workflows, or no exposure), enabling counterfactual evaluation of how a skill is shown to the agent. | [paper](https://arxiv.org/abs/2609.07255) |
| 2026-08-07 | **SkillAligner** — SkillAligner: Treating Retrieved Skills as Adaptable Drafts at Execution Time | Formalizes the skill–execution misfit and treats retrieved skills as adaptable drafts: a one-time, training-free joint adaptation before execution specializes skill fragments to the task and aligns their assumptions with the execution interface. | [paper](https://arxiv.org/abs/2608.06880) |

<a id="evaluation"></a>

## Benchmarks and empirical studies

| Date | Work | Contribution | Resources |
| --- | --- | --- | --- |
| 2026-10 | **Understanding Agent Skills** — Understanding Agent Skills: How Well Do They Transfer to Smaller Models? | An empirical study across skill-generation frameworks and model families of whether skills developed by frontier models help much smaller agents; strong-model skills do not consistently improve them. | [paper](https://openreview.net/forum?id=HupVHeskZE) · ICLR 2027 submission |
| 2026-10 | **SkillsBench-Compose** — When Skills Fail to Compose: Benchmarking and Compiling Agent Skills | A benchmark of 20 human-authored tasks that scores component requirements and cross-component relationships separately to expose failures in combining individually successful skills, with SkillCompiler compiling the supplied skills into one task-specific package. | [paper](https://openreview.net/forum?id=mJyF7aM0bc) · ICLR 2027 submission |
| 2026-06-16 | **A Framework for Evaluating Agentic Skills at Scale** | An evaluation framework in which a skill author builds realistic tasks to estimate a skill's utility, applied to 500 real-world skills with 1,000 generated tasks and instruction-following and goal-completion rubrics. | [paper](https://arxiv.org/abs/2606.17819) |
| 2026-05-22 | **From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills** | A systematic study of model-generated, domain-level skills across the full lifecycle of experience generation, skill extraction, and skill consumption, asking whether, when, and why such skills work. | [paper](https://arxiv.org/abs/2605.23899) |
| 2026-03-16 | **SWE-Skills-Bench** — SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering? | A requirement-driven benchmark that isolates the marginal utility of agent skills in software engineering by pairing 49 public skills with GitHub repositories pinned at fixed commits and execution-based acceptance tests. | [paper](https://arxiv.org/abs/2603.15401) · [ICLR 2027 submission](https://openreview.net/forum?id=kCYXuqBxmm) |
| 2026-02-18 | **Agent Skill Framework: Perspectives on the Potential of Small to Medium Language Models in Industrial Environments** | Studies the skill paradigm for open-source models from 270M to 80B parameters on two open tasks and an insurance-claims task; very small models struggle with reliable skill selection, while models around 30B–80B benefit substantially. | [paper](https://arxiv.org/abs/2602.16653) |
| 2026-02-13 | **SkillsBench** — SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks | A benchmark of 87 tasks across 8 domains with curated skills and deterministic verifiers, evaluated under matched no-skill and curated-skill conditions for 18 model–harness configurations. | [paper](https://arxiv.org/abs/2602.12670) |

<a id="adjacent"></a>

## Adjacent work

| Date | Work | Contribution | Resources |
| --- | --- | --- | --- |
| 2026-09-07 | **AgentLeak** — AgentLeak: Cloning Stronger LLM Agent Capabilities onto Weaker Agents Beyond Skill Stealing | A security study showing that leaking explicit skill artifacts does not by itself transfer capability to a weaker agent, because the stronger agent also relies on implicit procedural behaviors; relevant as evidence on the limits of skill-text transfer. | [paper](https://arxiv.org/abs/2609.07131) |

<!-- GENERATED CATALOG:END -->

## Scope

Included: methods that create, revise, compile, select, or evaluate **explicit skill artifacts** for LLM agents while the agent's weights stay frozen, and empirical studies of when such skills help, fail, or transfer. Work that trains skills into model weights is kept in its own section.

Not included: skill discovery in hierarchical or robotic reinforcement learning where a skill is a latent policy, general prompt optimization without a reusable skill artifact, and tool-use or memory papers that do not treat skills as the optimized object.

## Related resources

- [Awesome-Gradient-Free-LLMOpt](https://github.com/zz1358m/Awesome-Gradient-Free-LLMOpt) — ES and zeroth-order optimization of LLM parameters; its related section also tracks gradient-free search over prompts and agent artifacts.
- [Awesome-Edge-Cloud-LLM](https://github.com/zz1358m/Awesome-Edge-Cloud-LLM) — edge–cloud collaboration for LLMs and agents, including skill exchange.

## Maintenance

Edit `data/papers.json`, then run `python scripts/render.py`; validate with `python scripts/render.py --check`. Issues and PRs for papers, author code, and corrections are welcome.

This collection uses the [MIT License](LICENSE). Linked papers, code, and datasets retain their own licenses.
