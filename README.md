# Awesome Skill Optimization for LLM Agents

**English** | [简体中文](README_zh.md)

A curated collection of work on **optimizing agent skills**: reusable, text-space procedural artifacts (for example `SKILL.md` packages) that are loaded by a frozen LLM agent at inference time. The list follows a skill through its lifecycle: how it is induced from experience, evolved under feedback, moved across models and harnesses, selected and exposed at run time, and evaluated.

**Last literature check: 2026-10-15 · 58 papers.**

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
| 2026-10-14 | **AtomSearch** — AtomSearch: Evidence-Grounded Tree Search for Agent Skill Optimization | Revises skills through atomic rule edits, each tied to contrasting failed and successful executions, a behavioral hypothesis, and an intended scope, and searches a tree of skill states that keeps short edit compositions revisitable, with an outcome memory of past repairs and regressions. | [paper](https://arxiv.org/abs/2610.19951) |
| 2026-10-09 | **Cortex** — Cortex: Measurement-Gated Evolution and Pruning of Coding-Agent Skills and Rules | Turns developer corrections to a coding agent into replayable tasks and adds or deletes one skill or rule at a time, keeping a change only if repeated runs with and without it show a net gain and no task gets noticeably worse; evaluated with Claude Haiku 4.5 on a purpose-built repository. | [paper](https://arxiv.org/abs/2610.14216) · [code](https://github.com/samugit83/cortex) |
| 2026-10-08 | **SkillMorph** — Trajectory-Guided Fault Localization for Agent Skill Evolution | Links execution evidence to specific skill content before revising it: contrasts failure and success evidence in abstracted trajectories across repeated runs and tasks to identify suspicious actions, then uses them to localize edit sites in the skill and generate revisions; evaluated on SWE-Skills-Bench and CannBot. | [paper](https://arxiv.org/abs/2610.11858) |
| 2026-10-08 | **Skill-V** — Skill-V: Verifiable Self-Evolving Skill Library for Interactive Agents | Represents skills as versioned, falsifiable contracts that tie semantic intent to observable behavioral criteria: task failures trigger skill addition, disagreements between contract evaluations and task outcomes trigger revisions of skill boundaries, and revisions must pass non-regression checks on replayed historical evidence. | [paper](https://arxiv.org/abs/2610.11781) · [ICLR 2027 submission](https://openreview.net/forum?id=FANt1TYG1p) |
| 2026-10-04 | **TeleTune** — TeleTune: Evolving Agent Skills From Offline Telemetry | Learns a textual skill library from offline usage logs that record no goals, cannot be replayed, and may interleave tasks: action-prediction errors on logged trajectories propose library edits, and an edit is kept only if it improves held-out action-prediction accuracy. | [paper](https://arxiv.org/abs/2610.05437) · [ICLR 2027 submission](https://openreview.net/forum?id=4Idj4dQE5E) |
| 2026-10-01 | **SkillEvoLean** — SkillEvoLean: Mutation-enhanced skill evolution for Lean provers | Skill self-evolution for Lean theorem provers that jointly evolves a high-level solving policy and its reference knowledge: progressive updates draw on successful and failed trajectories, and when no complete proof can be generated a mutation step samples mathematical concepts to produce and select new skill candidates under verifier feedback. | [paper](https://arxiv.org/abs/2610.01799) |
| 2026-10 | **COBRA-Skills** — COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization | Formulates skill optimization as budgeted sequential optimization over an evolving candidate space, using contextual-bandit prioritization to decide which candidates receive costly execution-based evaluation. | [paper](https://openreview.net/forum?id=6XFoqlavXz) · ICLR 2027 submission |
| 2026-10 | **SkillNEO** — SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills | Argues that a partially repaired skill can stay low-scoring until later edits land, and introduces non-elitist evolutionary optimization that keeps developing intermediate versions using comparative execution evidence. | [paper](https://openreview.net/forum?id=DScGkPg0NR) · ICLR 2027 submission |
| 2026-09-18 | **GraphSkillEvo** — GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills | Represents skills as graph-structured natural-language artifacts to give explicit workflow-level guidance and to constrain the search space, and optimizes them with evolutionary search. | [paper](https://arxiv.org/abs/2609.21749) · [code](https://github.com/ruisun7/GraphSkillEvo) · [ICLR 2027 submission](https://openreview.net/forum?id=FrghfkhvZh) |
| 2026-09-08 | **SkillAdam** — SkillAdam: Stable and Efficient Skill Evolution for Agents | Targets unstable and inefficient skill self-evolution through two principles: direction stability (effective corrections accumulate across iterations) and update adaptivity (the scope of a revision follows the consistency of feedback). | [paper](https://arxiv.org/abs/2609.08944) · [code](https://github.com/ruc-datalab/SkillAdam) · [ICLR 2027 submission](https://openreview.net/forum?id=PQv8PT4UGn) |
| 2026-08-18 | **WER** — Write, Execute, Refine: From Skill Follower to Skill Optimizer via Reinforcement Learning from Execution Feedback | Trains a skill optimizer outside a frozen executor with group-relative rewards from verified repeated executions, turning matched successful and failed trajectories into the next phase's refinement states; evaluated on BFCL v4 multi-turn and tau2-bench. | [paper](https://arxiv.org/abs/2608.17587) · [code](https://github.com/littlepkk/wer-training) |
| 2026-07-29 | **SkillMentor** — SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis | Studies blind-spot diagnosis as a learnable capability separate from execution by training a Mentor policy while excluding executor updates and human supervision as sources of improvement. | [paper](https://arxiv.org/abs/2607.27360) |
| 2026-07-06 | **MetaSkill-Evolve** — MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution | Makes skill self-improvement recursive with a two-timescale design in which the improvement procedure itself is evolved alongside the task skill instead of being authored once and held fixed. | [paper](https://arxiv.org/abs/2607.05297) |
| 2026-05-31 | **SkillAdaptor** — SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories | Training-free, step-level skill adaptation: for a failed trajectory it locates the first actionable fault step, attributes it to candidate skills, and applies targeted updates under explicit acceptance checks with a frozen backbone. | [paper](https://arxiv.org/abs/2606.01311) · [code](https://github.com/zjunlp/SkillAdaptor) |
| 2026-05-22 | **SkillOpt** — SkillOpt: Executive Strategy for Self-Evolving Agent Skills | Treats a skill as the trainable external state of a frozen agent: a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on one skill document and accepts an edit only if a held-out validation score strictly improves. | [paper](https://arxiv.org/abs/2605.23904) |
| 2026-05-19 | **MOCHA** — MOCHA: Multi-Objective Chebyshev Annealing for Agent Skill Optimization | Treats skill optimization as multi-objective (accuracy and the context cost of fields such as the description and instruction body), selecting skills to improve by Chebyshev scalarization with random weights and accepting edits that expand the Pareto front while annealing from exploration to exploitation. | [paper](https://arxiv.org/abs/2605.19330) |
| 2026-05-10 | **Skill-R1** — Skill-R1: Agent Skill Evolution via Reinforcement Learning | Trains a lightweight skill generator, conditioned on task context, prior rollouts, and verified outcomes, to revise skills for a frozen task LLM over several generations, using a bi-level GRPO objective with intra- and inter-generation advantages. | [paper](https://arxiv.org/abs/2605.09359) · [ICLR 2027 submission](https://openreview.net/forum?id=1b8Jj09JxE) |

<a id="induction"></a>

## Skill induction from experience

| Date | Work | Contribution | Resources |
| --- | --- | --- | --- |
| 2026-10-13 | **Socratic Skill Learning** — Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills | Interleaves an Educator's guidance with a Student's own practice, with the Student remaining the only environment operator and skill author, and introduces SkillTransferBench to test whether learned skills hold up in fresh solver sessions on held-out variations. | [paper](https://arxiv.org/abs/2610.17860) · [code](https://github.com/NJU-LINK/Socratic-Skill-Learning) · [ICLR 2027 submission](https://openreview.net/forum?id=MVaW9iL9CL) |
| 2026-10-09 | **Work2Skill** — Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction | Captures human desktop GUI demonstrations with a recorder that aligns screen video, mouse and keyboard events, and accessibility-tree information, releases a dataset of 350 demonstrations, and induces reusable skills (workflow rules, step dependencies, completion checks) with an agent that inspects the evidence on demand. | [paper](https://arxiv.org/abs/2610.12984) · [code](https://github.com/china-qijizhifeng/Work2Skill) · [ICLR 2027 submission](https://openreview.net/forum?id=yJpMXl0CY4) |
| 2026-10-05 | **Mining Agent Skills from Production Traces** | Holding the mining pipeline fixed, compares three levels of mining evidence (successful trajectories only, successes and failures with outcome labels, the same mix with labels withheld) and two skill forms (ordered workflow plan, declarative ontology) on two enterprise benchmarks; which combination helps depends on the domain. | [paper](https://arxiv.org/abs/2610.05777) · [ICLR 2027 submission](https://openreview.net/forum?id=PWml1Dhee7) |
| 2026-09-04 | **Trace2Tower** — Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents | Abstracts step-level interactions into canonical events, builds a graph from semantic compatibility, transition dynamics, and outcome evidence, and applies a contrastive spectral decomposition to distill a multi-level skill hierarchy. | [paper](https://arxiv.org/abs/2609.05261) |
| 2026-08-27 | **WikiSkill** — WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution | Co-evolves agent skills with a persistent wiki, separating raw execution experience, accumulated knowledge, and executable skills so that later skill updates can build on consolidated insights. | [paper](https://arxiv.org/abs/2608.27454) · [ICLR 2027 submission](https://openreview.net/forum?id=eENzccuqfn) |
| 2026-08-15 | **SkillCommit** — SkillCommit: Evolving Agent Skills through Behaviorally Validated Scope Expansion | Stores each experience first as an instance-specific patch and abstracts patches into a higher-level skill only when cross-instance replay and an LLM mechanism check show a shared behavioral mechanism and the abstraction preserves every constituent's validated behavior. | [paper](https://arxiv.org/abs/2608.15165) |
| 2026-08-03 | **Skill-α** — Progressive Agent Skill Generation via Reinforcement Learning | Learns one RL policy that builds a skill by editing it step by step over successive source evidence, from documents or experience, rewarding each edit by comparing downstream execution under the original and edited skill on an anchored query. | [paper](https://arxiv.org/abs/2608.01678) · [code](https://github.com/ejhshen/skill-alpha) · [ICLR 2027 submission](https://openreview.net/forum?id=V1zG5WErz2) |
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
| 2026-05-05 | **SkCC** — SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents | A skill compiler built around SkIR, a strongly typed intermediate representation that separates skill semantics from framework-specific formatting to address cross-framework portability and security. | [paper](https://arxiv.org/abs/2605.03353) · [code](https://github.com/Nexa-Language/Skill-Compiler) |
| 2026-04-03 | **SkVM** — SkVM: Revisiting Language VM for Skills across Heterogenous LLMs and Harnesses | Treats skills as code and LLMs as heterogeneous processors: decomposes a skill's requirements into primitive capabilities, measures how well each model–harness pair supports them, and compiles skills against these capability profiles. | [paper](https://arxiv.org/abs/2604.03088) |

<a id="routing"></a>

## Retrieval, selection, and exposure

| Date | Work | Contribution | Resources |
| --- | --- | --- | --- |
| 2026-10-08 | **SkillContrast** — SkillContrast: Difference-Guided Text Selection for Agent Skill Reranking | A training-free text selector for skill reranking that compares the retrieved skills with one another and passes the passages where they differ, with local context, to a pretrained reranker, so that similar skills with different conditions of use stay distinguishable under a short input budget. | [paper](https://arxiv.org/abs/2610.11650) |
| 2026-10 | **SkillCraft** — SkillCraft: Skill-Set Retrieval Beyond Ranking for LLM Agents | Recasts post-retrieval skill selection as set resolution rather than ranking, estimating non-monotonic membership probabilities from list-relative evidence so that high-ranked distractors can be skipped, with set-level calibration deciding how many skills to admit. | [paper](https://openreview.net/forum?id=0HwdIddQeM) · ICLR 2027 submission |
| 2026-09-07 | **SkillAlign** — SkillAlign: Aligning Skill Interfaces for LLM-based Agents | Represents candidate skills as multi-view procedural cards and renders them through alternative exposure interfaces (full instructions, hints, compressed summaries, workflows, or no exposure), enabling counterfactual evaluation of how a skill is shown to the agent. | [paper](https://arxiv.org/abs/2609.07255) |
| 2026-08-28 | **SkillDreamer** — Imagine Before Acting: Prospective Skill Identification for LLM Agents | Observes that task descriptions state objectives while skill documents describe capabilities and procedures, a mismatch that causes useful skills to be missed in retrieval or invocation; it first imagines the required capabilities as pseudo skills to guide retrieval, then re-evaluates which skills to invoke as subtasks emerge during execution. | [paper](https://arxiv.org/abs/2609.01642) · [ICLR 2027 submission](https://openreview.net/forum?id=zhLjwy8Fig) |
| 2026-08-10 | **Emotion2Skill** — Emotion2Skill: Model-Internal Emotion Signals for Adaptive Skill Selection and Evolution | Extracts emotion vectors from the LLM's internal representations and uses them both to choose skills and to flag problematic invocations for targeted skill refinement; evaluated on WebShop and ALFWorld. | [paper](https://arxiv.org/abs/2608.09248) · [code](https://github.com/BoHan-LIN04/Emotion2Skill) |
| 2026-08-07 | **SkillAligner** — SkillAligner: Treating Retrieved Skills as Adaptable Drafts at Execution Time | Formalizes the skill–execution misfit and treats retrieved skills as adaptable drafts: a one-time, training-free joint adaptation before execution specializes skill fragments to the task and aligns their assumptions with the execution interface. | [paper](https://arxiv.org/abs/2608.06880) |

<a id="evaluation"></a>

## Benchmarks and empirical studies

| Date | Work | Contribution | Resources |
| --- | --- | --- | --- |
| 2026-10-13 | **Skill Inconsistencies at Runtime** — Why Static Skill Inconsistencies Do Not Equate to Runtime Risks: A Behavioral Analysis of LLM Agent Execution | Audits community and benchmark skill packages for conflicts among documentation, scripts, and configuration files, then compares no-skill, original-skill, and fixed-skill runs to measure how much these static defects actually change agent behavior. | [paper](https://arxiv.org/abs/2610.18927) |
| 2026-10-08 | **One Skill Too Many** — One Skill Too Many: How Co-Installed Skills Conflict in Coding Agents | An empirical study of conflicts between co-installed skills that do the same job in coding agents, mined from snapshots of 20,947 repositories and run on 312 confirmed pairs across three models: a similar skill can run in place of the installed one and drop its core functions while the task still passes. | [paper](https://arxiv.org/abs/2610.11647) |
| 2026-10-06 | **An Empirical Study of Agent Skills' Downstream Utility** | Defines downstream utility as the pass-rate difference from a no-skill run under the same model–harness configuration and measures it on the 87 SkillsBench tasks across nine configurations, also examining alternative marketplace skills and multi-skill organization; the same skills help some configurations and hurt others on 36.78% of tasks. | [paper](https://arxiv.org/abs/2610.08875) |
| 2026-10 | **Understanding Agent Skills** — Understanding Agent Skills: How Well Do They Transfer to Smaller Models? | An empirical study across skill-generation frameworks and model families of whether skills developed by frontier models help much smaller agents; strong-model skills do not consistently improve them. | [paper](https://openreview.net/forum?id=HupVHeskZE) · ICLR 2027 submission |
| 2026-10 | **SkillsBench-Compose** — When Skills Fail to Compose: Benchmarking and Compiling Agent Skills | A benchmark of 20 human-authored tasks that scores component requirements and cross-component relationships separately to expose failures in combining individually successful skills, with SkillCompiler compiling the supplied skills into one task-specific package. | [paper](https://openreview.net/forum?id=mJyF7aM0bc) · ICLR 2027 submission |
| 2026-09-30 | **Do Self-Evolving Skills Generalize to Held-Out Tasks?** | Tests five self-evolving skill methods and a one-shot skill on six benchmarks with the same model, agent, and train/test split: of the 21 skills that improve on their training tasks, 5 keep all of that improvement on test tasks, 13 keep part, and 3 keep none; also describes GSO, which keeps only a skill-writing guide and writes a new skill for each task. | [paper](https://arxiv.org/abs/2609.39148) · [ICLR 2027 submission](https://openreview.net/forum?id=rM2eQio3e3) |
| 2026-09-17 | **EconSkills** — EconSkills: Studying Skill Transfer and Retrieval for Web Agents on Live Economic Data | A skill library and evaluation framework that distills verified EconWebArena trajectories into parameterized standard operating procedures, and separates two questions: whether a known relevant procedure transfers to a held-out task, and whether that benefit survives when the agent selects from a 50-skill library. | [paper](https://arxiv.org/abs/2609.19523) |
| 2026-08-07 | **SkillEval** — SkillEval: Decomposing Agent Skill Quality into Interpretable Signals | Scores general properties of a SKILL.md document along fixed, interpretable directions while reducing the influence of unrelated document features, and uses the scores as an early signal of downstream effectiveness and to guide targeted revisions. | [paper](https://arxiv.org/abs/2608.06891) |
| 2026-08-04 | **ContinualSkillBench** — ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities? | A benchmark for in-context continual skill learning with five domains of difficulty-ordered tasks; it finds that keeping context and feedback without explicit skill maintenance performs about as well on average as maintaining a skill library, with selective benefits for reusable procedures or precise outputs. | [paper](https://arxiv.org/abs/2608.03874) |
| 2026-06-16 | **A Framework for Evaluating Agentic Skills at Scale** | An evaluation framework in which a skill author builds realistic tasks to estimate a skill's utility, applied to 500 real-world skills with 1,000 generated tasks and instruction-following and goal-completion rubrics. | [paper](https://arxiv.org/abs/2606.17819) |
| 2026-06-09 | **SameCapRisk-Bench** — Right Family, Wrong Skill: Evaluating Risk Exposure in Agent Skill Retrieval | A skill-retrieval benchmark of 890 units and 1,314 query cases in which each unit pairs a skill that meets a query requirement with a same-capability skill that violates it, scoring retrievers and rerankers on both helpful hits and exposure of the conflicting sibling. | [paper](https://arxiv.org/abs/2606.10388) |
| 2026-05-22 | **From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills** | A systematic study of model-generated, domain-level skills across the full lifecycle of experience generation, skill extraction, and skill consumption, asking whether, when, and why such skills work. | [paper](https://arxiv.org/abs/2605.23899) |
| 2026-03-16 | **SWE-Skills-Bench** — SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering? | A requirement-driven benchmark that isolates the marginal utility of agent skills in software engineering by pairing 49 public skills with GitHub repositories pinned at fixed commits and execution-based acceptance tests. | [paper](https://arxiv.org/abs/2603.15401) · [code](https://github.com/GeniusHTX/SWE-Skills-Bench) · [ICLR 2027 submission](https://openreview.net/forum?id=kCYXuqBxmm) |
| 2026-02-18 | **Agent Skill Framework: Perspectives on the Potential of Small to Medium Language Models in Industrial Environments** | Studies the skill paradigm for open-source models from 270M to 80B parameters on two open tasks and an insurance-claims task; very small models struggle with reliable skill selection, while models around 30B–80B benefit substantially. | [paper](https://arxiv.org/abs/2602.16653) |
| 2026-02-13 | **SkillsBench** — SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks | A benchmark of 87 tasks across 8 domains with curated skills and deterministic verifiers, evaluated under matched no-skill and curated-skill conditions for 18 model–harness configurations. | [paper](https://arxiv.org/abs/2602.12670) |

<a id="internalization"></a>

## Internalizing skills into weights

| Date | Work | Contribution | Resources |
| --- | --- | --- | --- |
| 2026-10-11 | **RSIPO** — RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution | Co-evolves skills and the policy model during agentic RL: the policy extracts skills from its own completed trajectories and is trained on that ability through trajectory replay, while empirical Bayes shrinkage calibrates how much the student trusts skill-conditioned teacher scores. | [paper](https://arxiv.org/abs/2610.15772) |
| 2026-08-03 | **SKT** — SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation | A verified data-synthesis pipeline that builds single- and multi-skill tasks from public agent skills and keeps only executable trajectories that substantially use every required skill, for supervised fine-tuning of skill use; it also releases a held-out skill-use benchmark. | [paper](https://arxiv.org/abs/2608.02287) |

<a id="adjacent"></a>

## Adjacent work

| Date | Work | Contribution | Resources |
| --- | --- | --- | --- |
| 2026-09-07 | **AgentLeak** — AgentLeak: Cloning Stronger LLM Agent Capabilities onto Weaker Agents Beyond Skill Stealing | A security study showing that leaking explicit skill artifacts does not by itself transfer capability to a weaker agent, because the stronger agent also relies on implicit procedural behaviors; relevant as evidence on the limits of skill-text transfer. | [paper](https://arxiv.org/abs/2609.07131) |
| 2026-09-01 | **Defense-as-Skill** — Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents | Implements a runtime guard against malicious skills as an installable, editable skill that checks sensitive actions against the user's task boundary, and improves the guard skill with a Monte-Carlo tree search driven by rollout feedback; listed here as a case of evolving a skill toward a safety objective. | [paper](https://arxiv.org/abs/2609.01487) |
| 2026-08-13 | **Skill Misevolution** — Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents | Shows that skill evolution can keep an unsafe procedure inside an otherwise useful skill so that later benign tasks repeat the harm, builds a gym and a 525-task benchmark that check the writing and retrieval steps separately, and proposes SafeEvolve, which checks a skill both when it is written and when a later task retrieves it. | [paper](https://arxiv.org/abs/2608.12851) · [code](https://github.com/henrymao2004/misevolve) |

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
