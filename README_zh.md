# Awesome Skill Optimization for LLM Agents

[English](README.md) | **简体中文**

收集 **agent skill 优化** 的论文与代码。这里的 skill 指文本形式、可复用的过程性工件（例如 `SKILL.md` 包），由权重冻结的 LLM agent 在推理时加载。清单按 skill 的生命周期组织：怎么从经验里归纳、怎么根据反馈进化、怎么跨模型和跨 harness 迁移、运行时怎么选择和呈现、怎么评测。

**最近一次文献检查：2026-10-15 · 58 篇。**

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
| 2026-10-14 | **AtomSearch** — AtomSearch: Evidence-Grounded Tree Search for Agent Skill Optimization | 用原子化的规则修改修订 skill，每次修改都关联到对比的失败与成功执行、一个行为假设和预期作用范围；在 skill 状态树上搜索，保留可回溯、可扩展的短修改组合，并用结果记忆记录以往的修复与退化。 | [paper](https://arxiv.org/abs/2610.19951) |
| 2026-10-09 | **Cortex** — Cortex: Measurement-Gated Evolution and Pruning of Coding-Agent Skills and Rules | 把开发者对 coding agent 的纠正保存为可重放的任务，每次只新增或删除一条 skill 或规则，只有在有无它的多次重复运行显示净收益、且没有任务明显变差时才保留；在专门构建的仓库上用 Claude Haiku 4.5 评测。 | [paper](https://arxiv.org/abs/2610.14216) · [code](https://github.com/samugit83/cortex) |
| 2026-10-08 | **SkillMorph** — Trajectory-Guided Fault Localization for Agent Skill Evolution | 先把执行证据对应到具体的 skill 内容再做修改：在多次运行、多个任务的抽象轨迹里对比失败和成功的证据，找出可疑动作，再据此定位 skill 里要改的位置并生成修改；在 SWE-Skills-Bench 和 CannBot 上评测。 | [paper](https://arxiv.org/abs/2610.11858) |
| 2026-10-08 | **Skill-V** — Skill-V: Verifiable Self-Evolving Skill Library for Interactive Agents | 把 skill 表示成带版本、可证伪的契约，将语义意图和可观察的行为标准对应起来：任务失败触发新增 skill，契约评估和任务结果不一致时触发对 skill 边界的修订，修订必须在重放的历史证据上通过不退化检查。 | [paper](https://arxiv.org/abs/2610.11781) · [ICLR 2027 submission](https://openreview.net/forum?id=FANt1TYG1p) |
| 2026-10-04 | **TeleTune** — TeleTune: Evolving Agent Skills From Offline Telemetry | 从离线使用日志中学习文本形式的 skill 库，这些日志没有记录目标、不能重放、还可能把多个任务混在一起：用日志轨迹上的动作预测误差提出对 skill 库的修改，只保留能提高 held-out 动作预测准确率的修改。 | [paper](https://arxiv.org/abs/2610.05437) · [ICLR 2027 submission](https://openreview.net/forum?id=4Idj4dQE5E) |
| 2026-10-01 | **SkillEvoLean** — SkillEvoLean: Mutation-enhanced skill evolution for Lean provers | 面向 Lean 定理证明器的 skill 自进化，同时进化高层解题策略和它的参考知识：渐进式更新利用成功和失败的轨迹；当生成不出完整证明时，变异步骤通过采样数学概念产生新的 skill 候选，并在 verifier 反馈下选择。 | [paper](https://arxiv.org/abs/2610.01799) |
| 2026-10 | **COBRA-Skills** — COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization | 把 skill 优化写成在不断变化的候选空间上的有预算序贯优化，用 contextual bandit 决定把代价高的执行评测分配给哪些候选。 | [paper](https://openreview.net/forum?id=6XFoqlavXz) · ICLR 2027 submission |
| 2026-10 | **SkillNEO** — SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills | 指出修到一半的 skill 在后续修改完成之前可能一直得分偏低，因此提出非精英的进化优化，利用对比式的执行证据继续发展中间版本。 | [paper](https://openreview.net/forum?id=DScGkPg0NR) · ICLR 2027 submission |
| 2026-09-18 | **GraphSkillEvo** — GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills | 把 skill 表示成图结构的自然语言工件，提供显式的 workflow 级指导并约束搜索空间，再用进化搜索优化。 | [paper](https://arxiv.org/abs/2609.21749) · [code](https://github.com/ruisun7/GraphSkillEvo) · [ICLR 2027 submission](https://openreview.net/forum?id=FrghfkhvZh) |
| 2026-09-08 | **SkillAdam** — SkillAdam: Stable and Efficient Skill Evolution for Agents | 针对 skill 自进化不稳定、迭代效率低的问题，提出两条原则：方向稳定（有效的修正跨迭代累积）和更新自适应（修改范围随反馈的一致程度变化）。 | [paper](https://arxiv.org/abs/2609.08944) · [code](https://github.com/ruc-datalab/SkillAdam) · [ICLR 2027 submission](https://openreview.net/forum?id=PQv8PT4UGn) |
| 2026-08-18 | **WER** — Write, Execute, Refine: From Skill Follower to Skill Optimizer via Reinforcement Learning from Execution Feedback | 在冻结的执行 agent 之外训练一个 skill 优化器：以多次执行的验证结果作为组内相对奖励，并把配对的成功与失败轨迹作为下一阶段的修订输入；在 BFCL v4 多轮和 tau2-bench 上评测。 | [paper](https://arxiv.org/abs/2608.17587) · [code](https://github.com/littlepkk/wer-training) |
| 2026-07-29 | **SkillMentor** — SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis | 把盲点诊断当作和执行分开的、可学习的能力：训练一个 Mentor 策略，同时排除执行模型更新和人工监督这两个改进来源。 | [paper](https://arxiv.org/abs/2607.27360) |
| 2026-07-06 | **MetaSkill-Evolve** — MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution | 用两个时间尺度让 skill 的自我改进变成递归的：改进流程本身和任务 skill 一起进化，不再是写一次就固定。 | [paper](https://arxiv.org/abs/2607.05297) |
| 2026-05-31 | **SkillAdaptor** — SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories | 免训练的步骤级 skill 适配：在失败轨迹里定位第一个可处理的出错步骤，归因到候选 skill，在显式的接受检查下做针对性修改，backbone 保持冻结。 | [paper](https://arxiv.org/abs/2606.01311) · [code](https://github.com/zjunlp/SkillAdaptor) |
| 2026-05-22 | **SkillOpt** — SkillOpt: Executive Strategy for Self-Evolving Agent Skills | 把 skill 当作冻结 agent 的可训练外部状态：由单独的优化器模型把打分后的 rollout 变成对一份 skill 文档的有界增、删、改，只有 held-out 验证分数严格提高时才接受修改。 | [paper](https://arxiv.org/abs/2605.23904) |
| 2026-05-19 | **MOCHA** — MOCHA: Multi-Objective Chebyshev Annealing for Agent Skill Optimization | 把 skill 优化看作多目标问题（准确率，以及 description、正文等字段占用的上下文成本），用随机权重的 Chebyshev 标量化挑选待改进的 skill，接受能扩展 Pareto 前沿的修改，并从探索逐步退火到利用。 | [paper](https://arxiv.org/abs/2605.19330) |
| 2026-05-10 | **Skill-R1** — Skill-R1: Agent Skill Evolution via Reinforcement Learning | 训练一个轻量的 skill 生成器，以任务上下文、先前 rollout 和验证结果为条件，在多代中为冻结的任务 LLM 修订 skill；优化目标是带代内与代间优势的双层 GRPO。 | [paper](https://arxiv.org/abs/2605.09359) · [ICLR 2027 submission](https://openreview.net/forum?id=1b8Jj09JxE) |

<a id="induction"></a>

## 从经验中归纳 Skill

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-13 | **Socratic Skill Learning** — Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills | 让 Educator 的指导与 Student 的实践交替进行，Student 始终是唯一操作环境、撰写 skill 的一方；同时提出 SkillTransferBench，检验学到的 skill 在全新求解会话、留出变体上是否仍然有效。 | [paper](https://arxiv.org/abs/2610.17860) · [code](https://github.com/NJU-LINK/Socratic-Skill-Learning) · [ICLR 2027 submission](https://openreview.net/forum?id=MVaW9iL9CL) |
| 2026-10-09 | **Work2Skill** — Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction | 用一个对齐屏幕录像、鼠标键盘事件和 accessibility tree 信息的录制工具采集人在桌面 GUI 上的演示，发布 350 条演示的数据集，并由一个按需查看证据的 agent 归纳出包含 workflow 规则、步骤依赖和完成检查的可复用 skill。 | [paper](https://arxiv.org/abs/2610.12984) · [code](https://github.com/china-qijizhifeng/Work2Skill) · [ICLR 2027 submission](https://openreview.net/forum?id=yJpMXl0CY4) |
| 2026-10-05 | **Mining Agent Skills from Production Traces** | 在挖掘流程固定的前提下，比较三种挖掘证据（只用成功轨迹、带结果标签的成功与失败轨迹、去掉标签的同一批轨迹）和两种 skill 形式（有序的 workflow 计划、声明式的 ontology），在两个企业场景基准上评测；哪种组合有效取决于领域。 | [paper](https://arxiv.org/abs/2610.05777) · [ICLR 2027 submission](https://openreview.net/forum?id=PWml1Dhee7) |
| 2026-09-04 | **Trace2Tower** — Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents | 把步骤级交互抽象成规范事件，按语义相容性、转移动态和结果证据建图，再用对比式谱分解蒸馏出多层的 skill 层级。 | [paper](https://arxiv.org/abs/2609.05261) |
| 2026-08-27 | **WikiSkill** — WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution | 让 agent skill 和一个持久的 wiki 共同进化，把原始执行经验、累积的知识和可执行的 skill 分开，使后续的 skill 更新能建立在已整合的结论上。 | [paper](https://arxiv.org/abs/2608.27454) · [ICLR 2027 submission](https://openreview.net/forum?id=eENzccuqfn) |
| 2026-08-15 | **SkillCommit** — SkillCommit: Evolving Agent Skills through Behaviorally Validated Scope Expansion | 先把每条经验存成针对具体实例的 patch，只有当跨实例重放和 LLM 机制检查都表明它们共享同一行为机制、且抽象后的 skill 保留每个组成部分已验证的行为时，才合并成更高层的 skill。 | [paper](https://arxiv.org/abs/2608.15165) |
| 2026-08-03 | **Skill-α** — Progressive Agent Skill Generation via Reinforcement Learning | 用 RL 学习一个统一的策略，依次读取文档或经验中的证据、逐步编辑出 skill；每次编辑的奖励来自在锚定 query 上比较原 skill 与修改后 skill 的下游执行结果。 | [paper](https://arxiv.org/abs/2608.01678) · [code](https://github.com/ejhshen/skill-alpha) · [ICLR 2027 submission](https://openreview.net/forum?id=V1zG5WErz2) |
| 2026-03-26 | **Trace2Skill** — Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills | 通过归纳推理，把大量执行轨迹并行地整合成一个统一的 skill 目录；既能加深人写的 skill，也能从较弱的 LLM 草稿出发构建 skill。 | [paper](https://arxiv.org/abs/2603.25158) |

<a id="transfer"></a>

## 跨模型与跨 harness 迁移

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10 | **SkillProbe** — One Skill, Many Models: Learning Representation Compatibility from Sparse Behavioral Tests | 一个有预算约束的框架，在适配之前诊断各模型对语义等价的 skill 写法的偏好：probe 库有 156 个配对的 probe，覆盖 14 个指令和可执行结构的因素，用分层贝叶斯画像挑选下一个 probe。 | [paper](https://openreview.net/forum?id=wRCOe7Vsp1) · ICLR 2027 submission |
| 2026-10 | **Skill Transfer** — Skill Transfer: Adapting Agent Skills from Strong to Weak Agents | 提出假设：强模型会默默补上 skill 里没写明的过程步骤，而弱模型会漏掉；论文把从强 agent 到弱 agent 适配 skill 时补上这一差距的问题形式化。 | [paper](https://openreview.net/forum?id=LD4Zo7u7Jr) · ICLR 2027 submission |
| 2026-10 | **CMRF** — Cross-Model Reproductive Fitness: Evolving Transferable Skills across Model Hosts | 一个考虑迁移的进化框架：在进化过程中就在异构的模型与 harness 组合上评估 skill，而不是先在一个主模型上优化、事后再测迁移。 | [paper](https://openreview.net/forum?id=L18vEjanZr) · ICLR 2027 submission |
| 2026-10 | **HEIRS** — Beyond the Final Skill: Revaluing Skill Evolution History After Executor Replacement | 保留进化过程中产生的各个 skill 版本；执行模型更换之后，通过目标侧的筛选和确认，从存档里原样选出一个版本使用。 | [paper](https://openreview.net/forum?id=Ds8Nz1GuuQ) · ICLR 2027 submission |
| 2026-05-29 | **MASA** — Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents | 用对照实验说明对一个 backbone 有益的 skill 可能伤害另一个，并在不改 agent 权重的前提下按目标 backbone 适配 skill，第一阶段是分层的 skill 进化流程。 | [paper](https://arxiv.org/abs/2605.30723) · [ICLR 2027 submission](https://openreview.net/forum?id=W0XuwkomQP) |
| 2026-05-05 | **SkCC** — SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents | 一个 skill 编译器，核心是强类型的中间表示 SkIR，把 skill 的语义和各框架特有的格式分开，处理跨框架可移植性和安全问题。 | [paper](https://arxiv.org/abs/2605.03353) · [code](https://github.com/Nexa-Language/Skill-Compiler) |
| 2026-04-03 | **SkVM** — SkVM: Revisiting Language VM for Skills across Heterogenous LLMs and Harnesses | 把 skill 当代码、把 LLM 当异构处理器：将 skill 的需求分解成 primitive capability，测量每个模型和 harness 的组合支持到什么程度，再按这份能力画像编译 skill。 | [paper](https://arxiv.org/abs/2604.03088) |

<a id="routing"></a>

## 检索、选择与呈现

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-08 | **SkillContrast** — SkillContrast: Difference-Guided Text Selection for Agent Skill Reranking | 一个免训练的文本选择器，用于 skill 重排序：把检索到的 skill 互相比较，将它们有差异的段落连同局部上下文交给预训练的 reranker，使写法相近但适用条件不同的 skill 在较短的输入长度下仍能被区分。 | [paper](https://arxiv.org/abs/2610.11650) |
| 2026-10 | **SkillCraft** — SkillCraft: Skill-Set Retrieval Beyond Ranking for LLM Agents | 把检索后的 skill 选择从排序问题改为集合判定问题：基于列表内的相对证据估计非单调的成员概率，从而跳过排名靠前的干扰项，并用集合层面的校准决定纳入多少个 skill。 | [paper](https://openreview.net/forum?id=0HwdIddQeM) · ICLR 2027 submission |
| 2026-09-07 | **SkillAlign** — SkillAlign: Aligning Skill Interfaces for LLM-based Agents | 把候选 skill 表示成多视图的过程卡片，并用不同的呈现方式（完整指令、提示、压缩摘要、workflow、不呈现）交给 agent，从而能对“怎么呈现 skill”做反事实评测。 | [paper](https://arxiv.org/abs/2609.07255) |
| 2026-08-28 | **SkillDreamer** — Imagine Before Acting: Prospective Skill Identification for LLM Agents | 指出任务描述写的是目标、skill 文档写的是能力和流程，这种不对齐会让合适的 skill 在检索或调用时被漏掉；做法是先把执行所需的能力想象成 pseudo skill 来引导检索，执行过程中再随新出现的子任务重新判断该调用哪些 skill。 | [paper](https://arxiv.org/abs/2609.01642) · [ICLR 2027 submission](https://openreview.net/forum?id=zhLjwy8Fig) |
| 2026-08-10 | **Emotion2Skill** — Emotion2Skill: Model-Internal Emotion Signals for Adaptive Skill Selection and Evolution | 从 LLM 内部表示中提取情绪向量，既用于选择 skill，也用来标记有问题的调用，以便有针对性地修订 skill；在 WebShop 和 ALFWorld 上评测。 | [paper](https://arxiv.org/abs/2608.09248) · [code](https://github.com/BoHan-LIN04/Emotion2Skill) |
| 2026-08-07 | **SkillAligner** — SkillAligner: Treating Retrieved Skills as Adaptable Drafts at Execution Time | 形式化了 skill 与执行不匹配的问题，把检索到的 skill 当作可改的草稿：执行前做一次免训练的联合适配，让 skill 片段贴合任务，并让它的假设和执行接口对齐。 | [paper](https://arxiv.org/abs/2608.06880) |

<a id="evaluation"></a>

## 基准与实证研究

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-13 | **Skill Inconsistencies at Runtime** — Why Static Skill Inconsistencies Do Not Equate to Runtime Risks: A Behavioral Analysis of LLM Agent Execution | 审计社区和基准 skill 包中文档、脚本与配置文件之间的冲突，再比较无 skill、原 skill、修复后 skill 三种设置下的执行，衡量这些静态缺陷实际在多大程度上改变 agent 行为。 | [paper](https://arxiv.org/abs/2610.18927) |
| 2026-10-08 | **One Skill Too Many** — One Skill Too Many: How Co-Installed Skills Conflict in Coding Agents | 对编程 agent 中同时安装、功能相同的 skill 之间的冲突做实证研究：从 20,947 个仓库的快照中挖掘，在三个模型上运行 312 对确认的 skill；相似的 skill 可能顶替已安装的那个并丢掉它的核心功能，而任务仍然通过。 | [paper](https://arxiv.org/abs/2610.11647) |
| 2026-10-06 | **An Empirical Study of Agent Skills' Downstream Utility** | 把下游效用定义为同一模型与 harness 配置下相对无 skill 运行的通过率差值，在 SkillsBench 的 87 个任务、九种配置上测量，并考察 marketplace 里的替代 skill 和多个 skill 的组织方式；在 36.78% 的任务上，同一批 skill 对一些配置有益、对另一些有害。 | [paper](https://arxiv.org/abs/2610.08875) |
| 2026-10 | **Understanding Agent Skills** — Understanding Agent Skills: How Well Do They Transfer to Smaller Models? | 一项实证研究，跨多个 skill 生成框架和模型家族，考察前沿模型产出的 skill 能不能帮到小得多的 agent；结论是强模型的 skill 并不能稳定地带来提升。 | [paper](https://openreview.net/forum?id=HupVHeskZE) · ICLR 2027 submission |
| 2026-10 | **SkillsBench-Compose** — When Skills Fail to Compose: Benchmarking and Compiling Agent Skills | 一个包含 20 个人工编写任务的基准，把各组件的要求和组件之间的关系分开打分，暴露出单独可用的 skill 组合起来失败的情况；同时提出 SkillCompiler，把给定的 skill 编译成一份针对任务的包。 | [paper](https://openreview.net/forum?id=mJyF7aM0bc) · ICLR 2027 submission |
| 2026-09-30 | **Do Self-Evolving Skills Generalize to Held-Out Tasks?** | 在六个基准上用相同的模型、agent 和训练/测试划分测试五种 skill 自进化方法和一个一次性生成的 skill：在训练任务上有提升的 21 个 skill 中，5 个在测试任务上保住了全部提升，13 个保住一部分，3 个完全没有保住；同时给出 GSO，只保留一份写 skill 的指南，对每个任务新写一个 skill。 | [paper](https://arxiv.org/abs/2609.39148) · [ICLR 2027 submission](https://openreview.net/forum?id=rM2eQio3e3) |
| 2026-09-17 | **EconSkills** — EconSkills: Studying Skill Transfer and Retrieval for Web Agents on Live Economic Data | 一个 skill 库和评测框架，把经过验证的 EconWebArena 轨迹蒸馏成参数化的标准操作流程，并把两个问题分开考察：已知相关的流程能否迁移到 held-out 任务，以及 agent 从 50 个 skill 的库里自行选择时这一收益能否保住。 | [paper](https://arxiv.org/abs/2609.19523) |
| 2026-08-07 | **SkillEval** — SkillEval: Decomposing Agent Skill Quality into Interpretable Signals | 对 SKILL.md 文档的通用属性给出方向固定、可解释的评分，并降低无关文档特征的干扰；这些分数可作为下游效果的早期信号，也用于指导有针对性的修订。 | [paper](https://arxiv.org/abs/2608.06891) |
| 2026-08-04 | **ContinualSkillBench** — ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities? | 一个面向上下文内持续 skill 学习的基准，含五个领域、按难度排序的任务；发现只保留上下文和反馈、不维护显式 skill 库时，平均表现与维护 skill 库相当，显式 skill 只在需要可复用流程或精确输出的任务上有选择性收益。 | [paper](https://arxiv.org/abs/2608.03874) |
| 2026-06-16 | **A Framework for Evaluating Agentic Skills at Scale** | 一个评测框架：skill 的作者可以构造贴近实际的任务来估计 skill 的效用；论文把它用在 500 个真实 skill 上，生成了 1,000 个任务，并配有指令遵从和目标完成两类评分标准。 | [paper](https://arxiv.org/abs/2606.17819) |
| 2026-06-09 | **SameCapRisk-Bench** — Right Family, Wrong Skill: Evaluating Risk Exposure in Agent Skill Retrieval | 一个 skill 检索基准，包含 890 个单元和 1,314 个查询用例；每个单元把满足查询要求的 skill 和一个能力相同但违反该要求的 skill 配成一对，同时考察检索器和 reranker 命中有用 skill 的情况以及把冲突 skill 暴露给 agent 的情况。 | [paper](https://arxiv.org/abs/2606.10388) |
| 2026-05-22 | **From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills** | 对模型生成的领域级 skill 做系统研究，覆盖经验生成、skill 提取、skill 使用的完整生命周期，考察这类 skill 是否有用、何时有用以及原因。 | [paper](https://arxiv.org/abs/2605.23899) |
| 2026-03-16 | **SWE-Skills-Bench** — SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering? | 一个由需求驱动的基准，把 49 个公开 skill 和固定 commit 的 GitHub 仓库、基于执行的验收测试配对，用来分离出 agent skill 在软件工程里的边际效用。 | [paper](https://arxiv.org/abs/2603.15401) · [code](https://github.com/GeniusHTX/SWE-Skills-Bench) · [ICLR 2027 submission](https://openreview.net/forum?id=kCYXuqBxmm) |
| 2026-02-18 | **Agent Skill Framework: Perspectives on the Potential of Small to Medium Language Models in Industrial Environments** | 在两个公开任务和一个保险理赔任务上，研究 270M 到 80B 的开源模型使用 skill 的效果：很小的模型难以可靠地选对 skill，30B 到 80B 左右的模型收益明显。 | [paper](https://arxiv.org/abs/2602.16653) |
| 2026-02-13 | **SkillsBench** — SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks | 一个基准：8 个领域 87 个任务，配有人工整理的 skill 和确定性验证器，在 18 个模型与 harness 的组合上做了有 skill 和无 skill 的配对评测。 | [paper](https://arxiv.org/abs/2602.12670) |

<a id="internalization"></a>

## 把 Skill 内化进权重

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-11 | **RSIPO** — RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution | 在 agentic RL 中让 skill 与策略模型共同进化：策略从自己完成的轨迹中提炼 skill，并通过轨迹重放训练这一能力；同时用经验贝叶斯收缩调节学生对以 skill 为条件的教师打分的信任程度。 | [paper](https://arxiv.org/abs/2610.15772) |
| 2026-08-03 | **SKT** — SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation | 一个经过验证的数据合成流程：从公开 agent skill 构造单 skill 和多 skill 任务，只保留实际用到全部所需 skill 的可执行轨迹，用于监督微调模型的 skill 使用能力；同时发布一个留出的 skill 使用基准。 | [paper](https://arxiv.org/abs/2608.02287) |

<a id="adjacent"></a>

## 邻近工作

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-09-07 | **AgentLeak** — AgentLeak: Cloning Stronger LLM Agent Capabilities onto Weaker Agents Beyond Skill Stealing | 一项安全研究：只泄露显式的 skill 工件并不能把能力转移给较弱的 agent，因为较强的 agent 还依赖隐式的过程行为；可以作为 skill 文本迁移存在上限的证据。 | [paper](https://arxiv.org/abs/2609.07131) |
| 2026-09-01 | **Defense-as-Skill** — Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents | 把防御恶意 skill 的运行时 guard 本身做成一个可安装、可编辑的 skill，按用户任务的边界检查敏感动作，并用由 rollout 反馈驱动的 Monte-Carlo tree search 改进这个 guard skill；收在这里是因为它是以安全为目标进化 skill 的例子。 | [paper](https://arxiv.org/abs/2609.01487) |
| 2026-08-13 | **Skill Misevolution** — Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents | 说明 skill 进化可能把不安全的流程留在一个本身有用的 skill 里，让之后的良性任务重复这一危害；构建了能分别检查写入和检索两个环节的 gym 和一个 525 个任务的基准，并提出 SafeEvolve，在 skill 写入时和被后续任务检索时各检查一次。 | [paper](https://arxiv.org/abs/2608.12851) · [code](https://github.com/henrymao2004/misevolve) |

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
