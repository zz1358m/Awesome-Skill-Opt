# Awesome Skill Optimization for LLM Agents

[English](README.md) | **简体中文**

收集 **agent skill 优化** 的论文与代码。这里的 skill 指文本形式、可复用的过程性工件（例如 `SKILL.md` 包），由权重冻结的 LLM agent 在推理时加载。清单按 skill 的生命周期组织：怎么从经验里归纳、怎么根据反馈进化、怎么跨模型和跨 harness 迁移、运行时怎么选择和呈现、怎么评测。

**最近一次文献检查：2026-10-11 · 28 篇。**

多数条目是近期的 preprint。标注 *ICLR 2027 submission* 的是匿名在审投稿，只依据公开摘要描述，这个标注不表示录用。贡献一栏取自摘要，不是独立复现；各论文报告的结果只对它自己的模型、harness 和基准成立。

## 导航

- [Skill 进化与优化](#optimization)
- [从经验中归纳 Skill](#induction)
- [跨模型与跨 harness 迁移](#transfer)
- [检索、选择与呈现](#routing)
- [基准与实证研究](#evaluation)
- [邻近工作](#adjacent)
- [收录范围](#scope)
- [文献数据](data/papers.json) · [贡献指南](CONTRIBUTING.md)

<!-- GENERATED CATALOG:START -->
<a id="optimization"></a>

## Skill 进化与优化

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10 | **COBRA-Skills** — COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization | 把 skill 优化写成在不断变化的候选空间上的有预算序贯优化，用 contextual bandit 决定把代价高的执行评测分配给哪些候选。 | [paper](https://openreview.net/forum?id=6XFoqlavXz) · ICLR 2027 submission |
| 2026-10 | **SkillNEO** — SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills | 指出修到一半的 skill 在后续修改完成之前可能一直得分偏低，因此提出非精英的进化优化，利用对比式的执行证据继续发展中间版本。 | [paper](https://openreview.net/forum?id=DScGkPg0NR) · ICLR 2027 submission |
| 2026-09-18 | **GraphSkillEvo** — GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills | 把 skill 表示成图结构的自然语言工件，提供显式的 workflow 级指导并约束搜索空间，再用进化搜索优化。 | [paper](https://arxiv.org/abs/2609.21749) |
| 2026-09-08 | **SkillAdam** — SkillAdam: Stable and Efficient Skill Evolution for Agents | 针对 skill 自进化不稳定、迭代效率低的问题，提出两条原则：方向稳定（有效的修正跨迭代累积）和更新自适应（修改范围随反馈的一致程度变化）。 | [paper](https://arxiv.org/abs/2609.08944) |
| 2026-07-29 | **SkillMentor** — SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis | 把盲点诊断当作和执行分开的、可学习的能力：训练一个 Mentor 策略，同时排除执行模型更新和人工监督这两个改进来源。 | [paper](https://arxiv.org/abs/2607.27360) |
| 2026-07-06 | **MetaSkill-Evolve** — MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution | 用两个时间尺度让 skill 的自我改进变成递归的：改进流程本身和任务 skill 一起进化，不再是写一次就固定。 | [paper](https://arxiv.org/abs/2607.05297) |
| 2026-05-31 | **SkillAdaptor** — SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories | 免训练的步骤级 skill 适配：在失败轨迹里定位第一个可处理的出错步骤，归因到候选 skill，在显式的接受检查下做针对性修改，backbone 保持冻结。 | [paper](https://arxiv.org/abs/2606.01311) |
| 2026-05-22 | **SkillOpt** — SkillOpt: Executive Strategy for Self-Evolving Agent Skills | 把 skill 当作冻结 agent 的可训练外部状态：由单独的优化器模型把打分后的 rollout 变成对一份 skill 文档的有界增、删、改，只有 held-out 验证分数严格提高时才接受修改。 | [paper](https://arxiv.org/abs/2605.23904) |

<a id="induction"></a>

## 从经验中归纳 Skill

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-09-04 | **Trace2Tower** — Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents | 把步骤级交互抽象成规范事件，按语义相容性、转移动态和结果证据建图，再用对比式谱分解蒸馏出多层的 skill 层级。 | [paper](https://arxiv.org/abs/2609.05261) |
| 2026-08-27 | **WikiSkill** — WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution | 让 agent skill 和一个持久的 wiki 共同进化，把原始执行经验、累积的知识和可执行的 skill 分开，使后续的 skill 更新能建立在已整合的结论上。 | [paper](https://arxiv.org/abs/2608.27454) |
| 2026-03-26 | **Trace2Skill** — Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills | 通过归纳推理，把大量执行轨迹并行地整合成一个统一的 skill 目录；既能加深人写的 skill，也能从较弱的 LLM 草稿出发构建 skill。 | [paper](https://arxiv.org/abs/2603.25158) |

<a id="transfer"></a>

## 跨模型与跨 harness 迁移

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10 | **SkillProbe** — One Skill, Many Models: Learning Representation Compatibility from Sparse Behavioral Tests | 一个有预算约束的框架，在适配之前诊断各模型对语义等价的 skill 写法的偏好：probe 库有 156 个配对的 probe，覆盖 14 个指令和可执行结构的因素，用分层贝叶斯画像挑选下一个 probe。 | [paper](https://openreview.net/forum?id=wRCOe7Vsp1) · ICLR 2027 submission |
| 2026-10 | **Skill Transfer** — Skill Transfer: Adapting Agent Skills from Strong to Weak Agents | 提出假设：强模型会默默补上 skill 里没写明的过程步骤，而弱模型会漏掉；论文把从强 agent 到弱 agent 适配 skill 时补上这一差距的问题形式化。 | [paper](https://openreview.net/forum?id=LD4Zo7u7Jr) · ICLR 2027 submission |
| 2026-10 | **CMRF** — Cross-Model Reproductive Fitness: Evolving Transferable Skills across Model Hosts | 一个考虑迁移的进化框架：在进化过程中就在异构的模型与 harness 组合上评估 skill，而不是先在一个主模型上优化、事后再测迁移。 | [paper](https://openreview.net/forum?id=L18vEjanZr) · ICLR 2027 submission |
| 2026-10 | **HEIRS** — Beyond the Final Skill: Revaluing Skill Evolution History After Executor Replacement | 保留进化过程中产生的各个 skill 版本；执行模型更换之后，通过目标侧的筛选和确认，从存档里原样选出一个版本使用。 | [paper](https://openreview.net/forum?id=Ds8Nz1GuuQ) · ICLR 2027 submission |
| 2026-05-29 | **MASA** — Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents | 用对照实验说明对一个 backbone 有益的 skill 可能伤害另一个，并在不改 agent 权重的前提下按目标 backbone 适配 skill，第一阶段是分层的 skill 进化流程。 | [paper](https://arxiv.org/abs/2605.30723) |
| 2026-05-05 | **SkCC** — SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents | 一个 skill 编译器，核心是强类型的中间表示 SkIR，把 skill 的语义和各框架特有的格式分开，处理跨框架可移植性和安全问题。 | [paper](https://arxiv.org/abs/2605.03353) |
| 2026-04-03 | **SkVM** — SkVM: Revisiting Language VM for Skills across Heterogenous LLMs and Harnesses | 把 skill 当代码、把 LLM 当异构处理器：将 skill 的需求分解成 primitive capability，测量每个模型和 harness 的组合支持到什么程度，再按这份能力画像编译 skill。 | [paper](https://arxiv.org/abs/2604.03088) |

<a id="routing"></a>

## 检索、选择与呈现

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-09-07 | **SkillAlign** — SkillAlign: Aligning Skill Interfaces for LLM-based Agents | 把候选 skill 表示成多视图的过程卡片，并用不同的呈现方式（完整指令、提示、压缩摘要、workflow、不呈现）交给 agent，从而能对“怎么呈现 skill”做反事实评测。 | [paper](https://arxiv.org/abs/2609.07255) |
| 2026-08-07 | **SkillAligner** — SkillAligner: Treating Retrieved Skills as Adaptable Drafts at Execution Time | 形式化了 skill 与执行不匹配的问题，把检索到的 skill 当作可改的草稿：执行前做一次免训练的联合适配，让 skill 片段贴合任务，并让它的假设和执行接口对齐。 | [paper](https://arxiv.org/abs/2608.06880) |

<a id="evaluation"></a>

## 基准与实证研究

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10 | **Understanding Agent Skills** — Understanding Agent Skills: How Well Do They Transfer to Smaller Models? | 一项实证研究，跨多个 skill 生成框架和模型家族，考察前沿模型产出的 skill 能不能帮到小得多的 agent；结论是强模型的 skill 并不能稳定地带来提升。 | [paper](https://openreview.net/forum?id=HupVHeskZE) · ICLR 2027 submission |
| 2026-10 | **SkillsBench-Compose** — When Skills Fail to Compose: Benchmarking and Compiling Agent Skills | 一个包含 20 个人工编写任务的基准，把各组件的要求和组件之间的关系分开打分，暴露出单独可用的 skill 组合起来失败的情况；同时提出 SkillCompiler，把给定的 skill 编译成一份针对任务的包。 | [paper](https://openreview.net/forum?id=mJyF7aM0bc) · ICLR 2027 submission |
| 2026-06-16 | **A Framework for Evaluating Agentic Skills at Scale** | 一个评测框架：skill 的作者可以构造贴近实际的任务来估计 skill 的效用；论文把它用在 500 个真实 skill 上，生成了 1,000 个任务，并配有指令遵从和目标完成两类评分标准。 | [paper](https://arxiv.org/abs/2606.17819) |
| 2026-05-22 | **From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills** | 对模型生成的领域级 skill 做系统研究，覆盖经验生成、skill 提取、skill 使用的完整生命周期，考察这类 skill 是否有用、何时有用以及原因。 | [paper](https://arxiv.org/abs/2605.23899) |
| 2026-03-16 | **SWE-Skills-Bench** — SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering? | 一个由需求驱动的基准，把 49 个公开 skill 和固定 commit 的 GitHub 仓库、基于执行的验收测试配对，用来分离出 agent skill 在软件工程里的边际效用。 | [paper](https://arxiv.org/abs/2603.15401) |
| 2026-02-18 | **Agent Skill Framework: Perspectives on the Potential of Small to Medium Language Models in Industrial Environments** | 在两个公开任务和一个保险理赔任务上，研究 270M 到 80B 的开源模型使用 skill 的效果：很小的模型难以可靠地选对 skill，30B 到 80B 左右的模型收益明显。 | [paper](https://arxiv.org/abs/2602.16653) |
| 2026-02-13 | **SkillsBench** — SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks | 一个基准：8 个领域 87 个任务，配有人工整理的 skill 和确定性验证器，在 18 个模型与 harness 的组合上做了有 skill 和无 skill 的配对评测。 | [paper](https://arxiv.org/abs/2602.12670) |

<a id="adjacent"></a>

## 邻近工作

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-09-07 | **AgentLeak** — AgentLeak: Cloning Stronger LLM Agent Capabilities onto Weaker Agents Beyond Skill Stealing | 一项安全研究：只泄露显式的 skill 工件并不能把能力转移给较弱的 agent，因为较强的 agent 还依赖隐式的过程行为；可以作为 skill 文本迁移存在上限的证据。 | [paper](https://arxiv.org/abs/2609.07131) |

<!-- GENERATED CATALOG:END -->

<a id="scope"></a>

## 收录范围

收录：在 agent 权重冻结的前提下，创建、修改、编译、选择或评测 **显式 skill 工件** 的方法，以及关于这类 skill 什么时候有用、什么时候失效、能不能迁移的实证研究。把 skill 训练进模型权重的工作单列一节。

不收录：分层强化学习或机器人里把 skill 当作潜在策略的 skill discovery；不产出可复用 skill 工件的一般 prompt 优化；不以 skill 为优化对象的工具使用或记忆类论文。

## 相关资源

- [Awesome-Gradient-Free-LLMOpt](https://github.com/zz1358m/Awesome-Gradient-Free-LLMOpt)：LLM 参数的 ES 与零阶优化；其关联研究部分也收录对 prompt 和 agent 工件的梯度无关搜索。
- [Awesome-Edge-Cloud-LLM](https://github.com/zz1358m/Awesome-Edge-Cloud-LLM)：LLM 与 agent 的端云协同，包括 skill 的交换。

## 维护

修改 `data/papers.json` 后运行 `python scripts/render.py`；提交前运行 `python scripts/render.py --check`。欢迎通过 Issue 或 PR 补充论文、作者代码和勘误。

本仓库采用 [MIT License](LICENSE)；所链接的论文、代码和数据集保留各自的许可。
