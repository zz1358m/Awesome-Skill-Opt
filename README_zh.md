# Awesome Skill Optimization for LLM Agents

[English](README.md) | **简体中文**

收集 **agent skill 优化** 的论文与代码。这里的 skill 指文本形式、可复用的过程性工件（例如 `SKILL.md` 包），由权重冻结的 LLM agent 在推理时加载。清单按 skill 的生命周期组织：怎么从经验里归纳、怎么根据反馈进化、怎么跨模型和跨 harness 迁移、运行时怎么选择和呈现、怎么评测。

**最近一次文献检查：2026-10-25 · 143 篇。**

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
| 2026-10-19 | **EvoSkill v2** — EvoSkill v2: Fully Agentic Skill Evolution from Benchmark Adaptation to a Stateful Evolver | 由基准适配器、求解器和进化器组成的三 agent 系统：进化器是一个贯穿整个运行、带 bash 工具的有状态编码 agent，每轮读取训练 rollout 并改写求解器的 skill；每个训练任务给多次尝试，并直接接受每轮的 skill，而不是依据有噪声的分数做选择。 | [paper](https://arxiv.org/abs/2610.25931) |
| 2026-10-19 | **GRSE** — Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving Multi-Agent Teams | 在多 agent 系统中把团队共享奖励归因到具体的 agent–skill 对：借鉴 GRPO 的组内相对思路，在相同 skill 库下多次执行同一问题并对比结果，再结合结构化的失败诊断来修订 skill。 | [paper](https://arxiv.org/abs/2610.27227) |
| 2026-10-17 | **SELM** — Selm: Self-Evolving Library Management for Multi-Skill Agent Optimization | 把 skill 演化看作库层面的管理，结合考虑效用的检索、基于任务经验的 Map-Reduce 式更新生成，以及保留或删除 skill 的生命周期控制。 | [paper](https://arxiv.org/abs/2610.24630) · [ICLR 2027 submission](https://openreview.net/forum?id=3bkesSncgC) |
| 2026-10-16 | **CDSE** — From Trajectories to Differentiated Skills: Cognitive Differentiation for Self-Improving Agents | 把一个 skill 拆成元信息、经验、工具、脚本四个功能不同的组件分别进化：从成功和失败轨迹中提取有证据支撑的修改，按组件整合与验证，并在组件间协调、按需调用。 | [paper](https://arxiv.org/abs/2610.23599) |
| 2026-10-15 | **FedSkillGit** — FedSkillGit: Federated Skill Evolution via Version Control | 联邦式 skill 进化：各客户端只提交针对具名规则的有限补丁和一段本轮经验摘要，二者先经过隐私过滤；服务器去重后合并成候选 skill，只有各客户端在本地验证集上报告的分数提高时才发布。 | [paper](https://arxiv.org/abs/2610.21348) |
| 2026-10-14 | **SkillNEO** — SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills | 指出修到一半的 skill 在后续修改完成之前可能一直得分偏低，因此提出非精英的进化优化，利用对比式的执行证据继续发展中间版本。 | [paper](https://arxiv.org/abs/2610.20926) · [ICLR 2027 submission](https://openreview.net/forum?id=DScGkPg0NR) |
| 2026-10-14 | **AtomSearch** — AtomSearch: Evidence-Grounded Tree Search for Agent Skill Optimization | 用原子化的规则修改修订 skill，每次修改都关联到对比的失败与成功执行、一个行为假设和预期作用范围；在 skill 状态树上搜索，保留可回溯、可扩展的短修改组合，并用结果记忆记录以往的修复与退化。 | [paper](https://arxiv.org/abs/2610.19951) |
| 2026-10-09 | **Cortex** — Cortex: Measurement-Gated Evolution and Pruning of Coding-Agent Skills and Rules | 把开发者对 coding agent 的纠正保存为可重放的任务，每次只新增或删除一条 skill 或规则，只有在有无它的多次重复运行显示净收益、且没有任务明显变差时才保留；在专门构建的仓库上用 Claude Haiku 4.5 评测。 | [paper](https://arxiv.org/abs/2610.14216) · [code](https://github.com/samugit83/cortex) |
| 2026-10-08 | **SkillMorph** — Trajectory-Guided Fault Localization for Agent Skill Evolution | 先把执行证据对应到具体的 skill 内容再做修改：在多次运行、多个任务的抽象轨迹里对比失败和成功的证据，找出可疑动作，再据此定位 skill 里要改的位置并生成修改；在 SWE-Skills-Bench 和 CannBot 上评测。 | [paper](https://arxiv.org/abs/2610.11858) |
| 2026-10-08 | **Skill-V** — Skill-V: Verifiable Self-Evolving Skill Library for Interactive Agents | 把 skill 表示成带版本、可证伪的契约，将语义意图和可观察的行为标准对应起来：任务失败触发新增 skill，契约评估和任务结果不一致时触发对 skill 边界的修订，修订必须在重放的历史证据上通过不退化检查。 | [paper](https://arxiv.org/abs/2610.11781) · [ICLR 2027 submission](https://openreview.net/forum?id=FANt1TYG1p) |
| 2026-10-04 | **TeleTune** — TeleTune: Evolving Agent Skills From Offline Telemetry | 从离线使用日志中学习文本形式的 skill 库，这些日志没有记录目标、不能重放、还可能把多个任务混在一起：用日志轨迹上的动作预测误差提出对 skill 库的修改，只保留能提高 held-out 动作预测准确率的修改。 | [paper](https://arxiv.org/abs/2610.05437) · [ICLR 2027 submission](https://openreview.net/forum?id=4Idj4dQE5E) |
| 2026-10-04 | **EVISKILL** — EVISKILL: Grounding Skill Evolution in Replayable Evidence | 把执行观测整理成可回放的证据卡并与每条 skill 修改关联，通过定向回放验证修改，先暂存有证据支持的修改，再由全局验证决定是否并入。 | [paper](https://arxiv.org/abs/2610.05030) · [ICLR 2027 submission](https://openreview.net/forum?id=SzgazZZUKR) |
| 2026-10-01 | **SkillEvoLean** — SkillEvoLean: Mutation-enhanced skill evolution for Lean provers | 面向 Lean 定理证明器的 skill 自进化，同时进化高层解题策略和它的参考知识：渐进式更新利用成功和失败的轨迹；当生成不出完整证明时，变异步骤通过采样数学概念产生新的 skill 候选，并在 verifier 反馈下选择。 | [paper](https://arxiv.org/abs/2610.01799) |
| 2026-10 | **COBRA-Skills** — COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization | 把 skill 优化写成在不断变化的候选空间上的有预算序贯优化，用 contextual bandit 决定把代价高的执行评测分配给哪些候选。 | [paper](https://openreview.net/forum?id=6XFoqlavXz) · ICLR 2027 submission |
| 2026-10 | **JIT Skill Compilation** — Optimizing Agent Execution through Just-in-Time Skill Compilation | 一个即时编译器：把执行轨迹当作 profiling 信息，将反复出现的确定性片段编译成参数化脚本并作为 skill 交付，同时记录并检验每个脚本的前提假设。 | [paper](https://openreview.net/forum?id=2I4ISoNutM) · ICLR 2027 submission |
| 2026-10 | **LCA-RLOO** — Lineage-Calibrated Evidence Aggregation for Sybil-Resistant Skill Evolution | 利用执行谱系图校准持久 skill 的更新，避免把来自同一上游来源的轨迹当作独立证据，并在接纳前做按根节点留一的验证。 | [paper](https://openreview.net/forum?id=3jpM74BSeN) · ICLR 2027 submission |
| 2026-10 | **CoEvo-MAS** — CoEvo-MAS: Co-Evolving Skills and Agent Organizations in Multi-Agent Systems | 同时演化提炼出的 skill 和多 agent 的组织结构：把 skill 使用情况汇总成画像，由 meta agent 据此提出 skill 分配、角色或组成的修改，并经验证后部署。 | [paper](https://openreview.net/forum?id=4sQ2Zncban) · ICLR 2027 submission |
| 2026-10 | **VeriTree** — Verification as a Budget: Posterior-Separation Scheduling for Self-Evolving Agent Skills | 把 skill 优化的外层循环改成带不确定性估计的 skill 树，每一轮依据后验分离准则在追加验证和生成新候选之间做选择。 | [paper](https://openreview.net/forum?id=5ZKVbEvIto) · ICLR 2027 submission |
| 2026-10 | **Future-SE** — Live Skill Evolution for Forecasting Agents with Delayed Outcome Feedback | 面向预测类 agent 的在线 skill 演化框架，在延迟的结果揭晓后修订由判断类和取证类 skill 组成的库，基座模型和 harness 保持不变。 | [paper](https://openreview.net/forum?id=8MIM9QGcap) · ICLR 2027 submission |
| 2026-10 | **AdaCraft** — AdaCraft: Evolving Reliable Skills for Articulated 3D Generation | 从执行反馈中为铰接 3D 资产生成演化可复用的 skill，使用记录几何条件的运动记忆，以及限制每次更新可改动规则数量的自适应预算。 | [paper](https://openreview.net/forum?id=8ubJP97hzG) · ICLR 2027 submission |
| 2026-10 | **SkillMuse** — SkillMuse: Multi-Turn User Simulation as a Feedback Generator for Skill Evolution | 把多轮用户模拟从评测终点改造成 skill 进化的反馈来源，用追问逐层暴露 skill 的缺陷，并在每次修订后由治理层修复事实退化和结构膨胀；在云服务领域的生产 skill 上评测。 | [paper](https://openreview.net/forum?id=ANEng5oYwD) · ICLR 2027 submission |
| 2026-10 | **CoEvolve** — CoEvolve: Counterfactual-Guided Co-Evolution of Memory and Collaboration in Multi-Agent System | 在多 agent 系统中用编码局部协作模式的 skill 作为记忆与协作之间的接口，通过对比原始轨迹与反事实轨迹，协调更新 skill 库、skill 记忆和各执行者的记忆。 | [paper](https://openreview.net/forum?id=CHyFv1A8il) · ICLR 2027 submission |
| 2026-10 | **EvoGap** — EvoGap: Weakness-Graph-Guided Skill Evolution for Frozen LLM Agents | 为冻结 agent 维护一张记录已诊断行为缺口的弱点图，针对选中的弱点生成可执行、可验证的练习任务，候选 skill 经过针对性验证才被收录，其实测效果再写回弱点图。 | [paper](https://openreview.net/forum?id=CbtqNEJJCA) · ICLR 2027 submission |
| 2026-10 | **ScienceCUA** — ScienceCUA: Resource-to-Skill Construction and Execution-Guided Skill Evolution for Scientific Computer Use Agents | 从软件文档为科学软件 computer-use agent 构建初始 skill 和按需查阅的参考资料，再对比成功与失败轨迹、经真实环境反复验证来进化 skill 库，并提供把进化任务与测试任务分开的审校版基准。 | [paper](https://openreview.net/forum?id=DlO53FBynm) · ICLR 2027 submission |
| 2026-10 | **GeoEvolve** — GeoEvolve: Recursive Skill Evolution for Image Geolocalization | 递归进化一个编码工具编排策略的图像地理定位 skill：对 on-policy 轨迹批中的决策做过程级归因，据此保留、澄清或修改规则，并把 skill 引导下的轨迹蒸馏进一个小模型。 | [paper](https://openreview.net/forum?id=HZeGsz6OOZ) · ICLR 2027 submission |
| 2026-09-30 | **Rep2Skill** — Rep2Skill: Representation-Guided Skill Self-Evolution for LLM Agents | 利用 agent 内部表示的轨迹定位偏离成功执行的轮次，再把这些信号转成文本反馈用于有针对性的 skill 修订。 | [paper](https://arxiv.org/abs/2609.39149) |
| 2026-09-30 | **SkillSpec** — SkillSpec: Consensus-Gated Agent Skill Evolution via Representation Specialization | 只有在配对评估达成一致时才提交 skill 修改，之后再依据整个优化轨迹的信号为 skill 选择扁平、图或混合的表示。 | [paper](https://arxiv.org/abs/2610.00704) · [ICLR 2027 submission](https://openreview.net/forum?id=C15zm5YCsW) |
| 2026-09-29 | **SSPE** — Semantic Projection for Continual Self-Evolution of Language Agents | 把正交梯度投影的思路迁移到自然语言 skill 修订：共享的 skill 在非平稳任务流上演化时，构造不干扰已有能力的修订。 | [paper](https://arxiv.org/abs/2609.36626) · [ICLR 2027 submission](https://openreview.net/forum?id=ArGLtNZkb6) |
| 2026-09-29 | **EASE** — EASE: Behavior-Adaptive Skill Curation for Self-Evolving Agents | 用强化学习训练一个统一的 skill 整理器，以执行模型行为的在线画像为条件，为不同的冻结执行模型增删改 skill，无需逐模型微调。 | [paper](https://arxiv.org/abs/2609.36746) · [ICLR 2027 submission](https://openreview.net/forum?id=Y4GjO4J3NZ) |
| 2026-09-29 | **SkillCome** — SkillCome: Group Contrast Skill Optimization with Dual Memory | 对每个问题生成一组轨迹，对比成功与失败轨迹找出关键分歧，并用双重记忆累积历史证据，使 skill 修改方向更稳定。 | [paper](https://arxiv.org/abs/2609.37128) · [ICLR 2027 submission](https://openreview.net/forum?id=vLSHYnL2vR) |
| 2026-09-29 | **RASO** — Retrieval-Augmented Skill Optimization via Cross-Harness Adaptation | 把公开的 skill 语料作为 skill 优化的先验，在初始化和反馈驱动的更新两个阶段检索相关 skill，并针对领域与 harness 的差异做适配。 | [paper](https://arxiv.org/abs/2609.38024) · [ICLR 2027 submission](https://openreview.net/forum?id=vTCwPX06pU) |
| 2026-09-29 | **Prompt2Skill** — Prompt2Skill: Unsupervised Skill Optimization From Natural Language Instructions | 只凭自然语言任务描述构建 skill：先推出任务规格、寻找或合成数据，再通过反思式编辑迭代改进 skill。 | [paper](https://arxiv.org/abs/2609.38593) · [ICLR 2027 submission](https://openreview.net/forum?id=5J6WudE0Gk) |
| 2026-09-28 | **SkillFocus** — SkillFocus: Evolving Agent Skills via Capability Decomposition | 把反复出现的任务要求分解成固定的能力空间，选出使最多任务未解决的能力，据此决定修订 skill 的哪部分以及使用哪些证据。 | [paper](https://arxiv.org/abs/2609.34397) |
| 2026-09-28 | **V-Gym** — V-Gym: Enhancing Agentic Visual Reasoning via Skill-Data Co-Evolution | 从执行轨迹出发，同时演化分层的流程性 skill 和多模态练习数据，skill 更新只有在提升验证集表现时才保留。 | [paper](https://arxiv.org/abs/2609.34682) · [ICLR 2027 submission](https://openreview.net/forum?id=N5j6fRhiR1) |
| 2026-09-28 | **RSI-Router** — RSI-Router: Evolving Subtask-Level LLM Routing and Skills for Cost-Efficient Agents | 通过递归自我改进同时构建大小模型之间子任务级的路由和针对各模型的 skill，并维护路由方案的 Pareto 种群。 | [paper](https://arxiv.org/abs/2609.34712) |
| 2026-09-27 | **R² Flow** — R$^2$ Flow: Recursive Self-Improvement via Recursive Skill Evolution | 在共享状态的编排图上交替进行基于 flow 的策略学习、独立验证和带版本的 skill 库修改，用 flow 份额和带符号的效用决定改哪些 skill。 | [paper](https://arxiv.org/abs/2609.33867) · [code](https://github.com/beita6969/r2flow) · [ICLR 2027 submission](https://openreview.net/forum?id=Wnrr8HTdq3) |
| 2026-09-26 | **SkillVine** — SkillVine: Agent Skill Evolution via Branching Exploration | 把 skill 库演化表述为图搜索，采用主干与分支协同探索、父节点选择器和自适应粒度的更新，而不是只在最新版本上线性修改。 | [paper](https://arxiv.org/abs/2609.32731) · [ICLR 2027 submission](https://openreview.net/forum?id=onGjqwrhS7) |
| 2026-09-26 | **VALVE** — Certified Long-Horizon Code Agent Evolution via Validation-Gated Skill Optimization | 一个带验证门控的长时程文本 skill 优化框架，面向仓库级软件任务流，给出收敛、后续任务收益和回撤的理论保证。 | [paper](https://arxiv.org/abs/2609.32990) · [ICLR 2027 submission](https://openreview.net/forum?id=VJvsdeZ3eW) |
| 2026-09-25 | **SkillEvoReg** — SkillEvoReg: Regularizing Agent Skill Evolution Against Overfitting | 把反复的 skill 更新视为会过拟合的学习过程，用更新生成时的 skill dropout、考虑复杂度的局部正则和因果反例验证来加以约束。 | [paper](https://arxiv.org/abs/2609.30861) · [ICLR 2027 submission](https://openreview.net/forum?id=IPjzJ62HxM) |
| 2026-09-25 | **MammoClaw** — MammoClaw: Towards Skill-Evolving Agent Harness for Breast Cancer Mammography Analysis | 基于冻结 MLLM、不需训练的乳腺 X 线分析 agent，配有区域和双视图检查工具，通过 skill 演化把失败轨迹转成后续可复用的指导。 | [paper](https://arxiv.org/abs/2609.31789) · [code](https://krishnakanthnakka.github.io/mammoclaw) |
| 2026-09-24 | **SkillPivot** — A Wrong Turn Does Not Ruin the Journey: Deviation-Guided Skill Self-Evolution for LLM Agents | 找出失败轨迹从有用前缀转为错误后缀的位置，让更强的教师模型从该前缀继续执行，再对比两段后缀生成局部的 skill 更新。 | [paper](https://arxiv.org/abs/2609.29154) |
| 2026-09-24 | **HEXIS** — HEXIS: Compiling Agent Skills into Extended Finite State Machines | 把 agent skill 编译成扩展有限状态机，将 skill 知识与控制流分离；根据开发轨迹增量添加或细化状态，更新须通过静态检查和轨迹回放才被接受。 | [paper](https://arxiv.org/abs/2609.30123) · [ICLR 2027 submission](https://openreview.net/forum?id=zI7jcDF5p7) |
| 2026-09-18 | **GraphSkillEvo** — GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills | 把 skill 表示成图结构的自然语言工件，提供显式的 workflow 级指导并约束搜索空间，再用进化搜索优化。 | [paper](https://arxiv.org/abs/2609.21749) · [code](https://github.com/ruisun7/GraphSkillEvo) · [ICLR 2027 submission](https://openreview.net/forum?id=FrghfkhvZh) |
| 2026-09-08 | **SkillAdam** — SkillAdam: Stable and Efficient Skill Evolution for Agents | 针对 skill 自进化不稳定、迭代效率低的问题，提出两条原则：方向稳定（有效的修正跨迭代累积）和更新自适应（修改范围随反馈的一致程度变化）。 | [paper](https://arxiv.org/abs/2609.08944) · [code](https://github.com/ruc-datalab/SkillAdam) · [ICLR 2027 submission](https://openreview.net/forum?id=PQv8PT4UGn) |
| 2026-08-18 | **WER** — Write, Execute, Refine: From Skill Follower to Skill Optimizer via Reinforcement Learning from Execution Feedback | 在冻结的执行 agent 之外训练一个 skill 优化器：以多次执行的验证结果作为组内相对奖励，并把配对的成功与失败轨迹作为下一阶段的修订输入；在 BFCL v4 多轮和 tau2-bench 上评测。 | [paper](https://arxiv.org/abs/2608.17587) · [code](https://github.com/littlepkk/wer-training) |
| 2026-07-29 | **SkillMentor** — SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis | 把盲点诊断当作和执行分开的、可学习的能力：训练一个 Mentor 策略，同时排除执行模型更新和人工监督这两个改进来源。 | [paper](https://arxiv.org/abs/2607.27360) |
| 2026-07-29 | **SIGIL** — SIGIL: Skill Compilation for Reliable and Efficient Agent Execution | 把编写好的 skill 及其资源编译成带类型、经过校验的中间表示，再确定性地生成可执行的 harness，只把 skill 原本交给模型的决策留给模型。 | [paper](https://arxiv.org/abs/2607.27309) · [ICLR 2027 submission](https://openreview.net/forum?id=lo1tnbagnQ) |
| 2026-07-06 | **MetaSkill-Evolve** — MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution | 用两个时间尺度让 skill 的自我改进变成递归的：改进流程本身和任务 skill 一起进化，不再是写一次就固定。 | [paper](https://arxiv.org/abs/2607.05297) |
| 2026-06-12 | **SelfEvoSkill** — SelfEvoSkill: Paired Execution Audits for Skill Revision without External Outcome Supervision | 不依赖任务奖励修订 skill：对比同一任务在有无该 skill 时的配对执行，把行为差异定位到具体段落，修改后再重新执行评估。 | [paper](https://arxiv.org/abs/2606.14239) · [ICLR 2027 submission](https://openreview.net/forum?id=5QzKESnW79) |
| 2026-06-06 | **VideoWeaver** — VideoWeaver: Evaluating and Evolving Skills for Agentic Long Video Generation | 面向长视频生成的 agent harness 和基准：agent 自行把基础 skill 组合成工作流，演化算法再依据 agent-as-judge 的反馈改进组合类和创作类 skill。 | [paper](https://arxiv.org/abs/2606.08091) · [code](https://github.com/JianhuiWei7/VideoWeaver) · [ICLR 2027 submission](https://openreview.net/forum?id=ahcNtcQxsO) |
| 2026-05-31 | **SkillAdaptor** — SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories | 免训练的步骤级 skill 适配：在失败轨迹里定位第一个可处理的出错步骤，归因到候选 skill，在显式的接受检查下做针对性修改，backbone 保持冻结。 | [paper](https://arxiv.org/abs/2606.01311) · [code](https://github.com/zjunlp/SkillAdaptor) |
| 2026-05-22 | **SkillOpt** — SkillOpt: Executive Strategy for Self-Evolving Agent Skills | 把 skill 当作冻结 agent 的可训练外部状态：由单独的优化器模型把打分后的 rollout 变成对一份 skill 文档的有界增、删、改，只有 held-out 验证分数严格提高时才接受修改。 | [paper](https://arxiv.org/abs/2605.23904) |
| 2026-05-19 | **MOCHA** — MOCHA: Multi-Objective Chebyshev Annealing for Agent Skill Optimization | 把 skill 优化看作多目标问题（准确率，以及 description、正文等字段占用的上下文成本），用随机权重的 Chebyshev 标量化挑选待改进的 skill，接受能扩展 Pareto 前沿的修改，并从探索逐步退火到利用。 | [paper](https://arxiv.org/abs/2605.19330) |
| 2026-05-13 | **SkillFlow (orchestration)** — SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration | 在冻结执行模型和动态 skill 库之上，用基于 flow matching 的轨迹平衡损失训练编排 supervisor，并依据 flow 诊断决定何时创建或删除哪些 skill。 | [paper](https://arxiv.org/abs/2605.14089) · [ICLR 2027 submission](https://openreview.net/forum?id=4bCRO5OIWY) |
| 2026-05-10 | **Skill-R1** — Skill-R1: Agent Skill Evolution via Reinforcement Learning | 训练一个轻量的 skill 生成器，以任务上下文、先前 rollout 和验证结果为条件，在多代中为冻结的任务 LLM 修订 skill；优化目标是带代内与代间优势的双层 GRPO。 | [paper](https://arxiv.org/abs/2605.09359) · [ICLR 2027 submission](https://openreview.net/forum?id=1b8Jj09JxE) |
| 2026-05-08 | **SkillLens** — SkillLens: Adaptive Multi-Granularity Skill Reuse for Cost-Efficient LLM Agents | 把 skill 组织成策略、方略、流程、原语四层图，用随机游走按混合粒度检索，由 verifier 决定每个单元是接受、分解、改写还是跳过，skill 和 verifier 都随时间迭代。 | [paper](https://arxiv.org/abs/2605.08386) |

<a id="induction"></a>

## 从经验中归纳 Skill

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-16 | **DrugHarness** — DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery | 面向计算药物发现的 agent harness：从执行轨迹和结果中归纳带适用条件、推荐动作和支持证据的条件式 skill，由独立的审查 agent 核对来源、必要时做针对性试验后才收录，并在后续反馈中修订。 | [paper](https://arxiv.org/abs/2610.23791) · [ICLR 2027 submission](https://openreview.net/forum?id=HcKDYJ7cxV) |
| 2026-10-13 | **Socratic Skill Learning** — Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills | 让 Educator 的指导与 Student 的实践交替进行，Student 始终是唯一操作环境、撰写 skill 的一方；同时提出 SkillTransferBench，检验学到的 skill 在全新求解会话、留出变体上是否仍然有效。 | [paper](https://arxiv.org/abs/2610.17860) · [code](https://github.com/NJU-LINK/Socratic-Skill-Learning) · [ICLR 2027 submission](https://openreview.net/forum?id=MVaW9iL9CL) |
| 2026-10-09 | **Work2Skill** — Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction | 用一个对齐屏幕录像、鼠标键盘事件和 accessibility tree 信息的录制工具采集人在桌面 GUI 上的演示，发布 350 条演示的数据集，并由一个按需查看证据的 agent 归纳出包含 workflow 规则、步骤依赖和完成检查的可复用 skill。 | [paper](https://arxiv.org/abs/2610.12984) · [code](https://github.com/china-qijizhifeng/Work2Skill) · [ICLR 2027 submission](https://openreview.net/forum?id=yJpMXl0CY4) |
| 2026-10-05 | **Mining Agent Skills from Production Traces** | 在挖掘流程固定的前提下，比较三种挖掘证据（只用成功轨迹、带结果标签的成功与失败轨迹、去掉标签的同一批轨迹）和两种 skill 形式（有序的 workflow 计划、声明式的 ontology），在两个企业场景基准上评测；哪种组合有效取决于领域。 | [paper](https://arxiv.org/abs/2610.05777) · [ICLR 2027 submission](https://openreview.net/forum?id=PWml1Dhee7) |
| 2026-10 | **SPARK** — Evidence Over Plans: Online Trajectory Verification for Skill Distillation | 一个闭环的 skill 合成框架，从经环境验证的轨迹中生成 skill，并用衡量后验证据的轨迹级指标作为在线信号引导 skill 生成。 | [paper](https://openreview.net/forum?id=7JkQOn29p5) · ICLR 2027 submission |
| 2026-10 | **AtmoSkillRSI** — AtmoSkillRSI: Skill Formation and Recursive Refinement in Atmospheric Workflows | 在基于 Earth2Studio 的大气科学工作流构建中研究持久 skill 的形成与反复修订的受控设定，比较顺序和任务并行两种经验组织方式。 | [paper](https://openreview.net/forum?id=AB1G0b3tLS) · ICLR 2027 submission |
| 2026-09-26 | **ExpVoyager** — ExpVoyager: Direct Experience Navigation for Dynamic Agent Skill Synthesis | 把 skill 合成改为按需在原始历史轨迹中导航：skill 整理器针对当前任务以不同视角和粒度探索经验，而不是预先抽象成固定知识。 | [paper](https://arxiv.org/abs/2609.32630) · [ICLR 2027 submission](https://openreview.net/forum?id=hSwCTccrjq) |
| 2026-09-04 | **Trace2Tower** — Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents | 把步骤级交互抽象成规范事件，按语义相容性、转移动态和结果证据建图，再用对比式谱分解蒸馏出多层的 skill 层级。 | [paper](https://arxiv.org/abs/2609.05261) |
| 2026-08-27 | **WikiSkill** — WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution | 让 agent skill 和一个持久的 wiki 共同进化，把原始执行经验、累积的知识和可执行的 skill 分开，使后续的 skill 更新能建立在已整合的结论上。 | [paper](https://arxiv.org/abs/2608.27454) · [ICLR 2027 submission](https://openreview.net/forum?id=eENzccuqfn) |
| 2026-08-15 | **SkillCommit** — SkillCommit: Evolving Agent Skills through Behaviorally Validated Scope Expansion | 先把每条经验存成针对具体实例的 patch，只有当跨实例重放和 LLM 机制检查都表明它们共享同一行为机制、且抽象后的 skill 保留每个组成部分已验证的行为时，才合并成更高层的 skill。 | [paper](https://arxiv.org/abs/2608.15165) |
| 2026-08-03 | **Skill-α** — Progressive Agent Skill Generation via Reinforcement Learning | 用 RL 学习一个统一的策略，依次读取文档或经验中的证据、逐步编辑出 skill；每次编辑的奖励来自在锚定 query 上比较原 skill 与修改后 skill 的下游执行结果。 | [paper](https://arxiv.org/abs/2608.01678) · [code](https://github.com/ejhshen/skill-alpha) · [ICLR 2027 submission](https://openreview.net/forum?id=V1zG5WErz2) |
| 2026-03-26 | **Trace2Skill** — Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills | 通过归纳推理，把大量执行轨迹并行地整合成一个统一的 skill 目录；既能加深人写的 skill，也能从较弱的 LLM 草稿出发构建 skill。 | [paper](https://arxiv.org/abs/2603.25158) |

<a id="transfer"></a>

## 跨模型与跨 harness 迁移

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-20 | **D-Skill** — D-Skill: Distilling Teacher Knowledge through Agent Skills | 把较强的 agent 当作黑盒教师，离线对比成对 rollout，把它的行为优势提炼成供较弱学生使用的自然语言 skill，不需要标注、额外环境交互或权重更新。 | [paper](https://arxiv.org/abs/2610.28914) · [ICLR 2027 submission](https://openreview.net/forum?id=FG476Lwadh) |
| 2026-10 | **SkillProbe** — One Skill, Many Models: Learning Representation Compatibility from Sparse Behavioral Tests | 一个有预算约束的框架，在适配之前诊断各模型对语义等价的 skill 写法的偏好：probe 库有 156 个配对的 probe，覆盖 14 个指令和可执行结构的因素，用分层贝叶斯画像挑选下一个 probe。 | [paper](https://openreview.net/forum?id=wRCOe7Vsp1) · ICLR 2027 submission |
| 2026-10 | **Skill Transfer** — Skill Transfer: Adapting Agent Skills from Strong to Weak Agents | 提出假设：强模型会默默补上 skill 里没写明的过程步骤，而弱模型会漏掉；论文把从强 agent 到弱 agent 适配 skill 时补上这一差距的问题形式化。 | [paper](https://openreview.net/forum?id=LD4Zo7u7Jr) · ICLR 2027 submission |
| 2026-10 | **CMRF** — Cross-Model Reproductive Fitness: Evolving Transferable Skills across Model Hosts | 一个考虑迁移的进化框架：在进化过程中就在异构的模型与 harness 组合上评估 skill，而不是先在一个主模型上优化、事后再测迁移。 | [paper](https://openreview.net/forum?id=L18vEjanZr) · ICLR 2027 submission |
| 2026-10 | **HEIRS** — Beyond the Final Skill: Revaluing Skill Evolution History After Executor Replacement | 保留进化过程中产生的各个 skill 版本；执行模型更换之后，通过目标侧的筛选和确认，从存档里原样选出一个版本使用。 | [paper](https://openreview.net/forum?id=Ds8Nz1GuuQ) · ICLR 2027 submission |
| 2026-10 | **Skill-in-Skill** — Skill-in-Skill: Agent Skills That Carry Their Own Execution Conditions Across Domains | 一种可移植的 skill 架构，把激活、授权、执行和验证条件与 skill 打包在一起，并在跨边界迁移场景下与把同等治理放在外部 sidecar 的做法比较。 | [paper](https://openreview.net/forum?id=1pMeMmzDVx) · ICLR 2027 submission |
| 2026-09 | **SkCC** — SkCC: A Compiler for Cross-Framework Agent Skills | 编译器式系统：先把 skill 规范化为带类型的中间表示并做静态检查，再由面向不同目标的发射器渲染给不同 agent 框架；在 SkillsBench 上用多个编码 agent 命令行工具评测。 | [paper](https://openreview.net/forum?id=EgaT7aRhoK) · ICLR 2027 submission |
| 2026-08-20 | **Break It Down, Pass It On** — Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents | 对照研究 skill 的归纳方式如何影响其在其他任务上的复用：子任务级 skill 总体有益，任务级 skill 常常不如不用记忆的基线，文本 skill 比代码 skill 迁移得更好；作者提出结合具体性与抽象性的 skill 效用分数，只需 skill 和任务描述即可计算，并与迁移成功率相关。 | [paper](https://arxiv.org/abs/2608.20274) |
| 2026-05-29 | **MASA** — Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents | 用对照实验说明对一个 backbone 有益的 skill 可能伤害另一个，并在不改 agent 权重的前提下按目标 backbone 适配 skill，第一阶段是分层的 skill 进化流程。 | [paper](https://arxiv.org/abs/2605.30723) · [ICLR 2027 submission](https://openreview.net/forum?id=W0XuwkomQP) |
| 2026-05-05 | **SkCC** — SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents | 一个 skill 编译器，核心是强类型的中间表示 SkIR，把 skill 的语义和各框架特有的格式分开，处理跨框架可移植性和安全问题。 | [paper](https://arxiv.org/abs/2605.03353) · [code](https://github.com/Nexa-Language/Skill-Compiler) |
| 2026-04-03 | **SkVM** — SkVM: Revisiting Language VM for Skills across Heterogenous LLMs and Harnesses | 把 skill 当代码、把 LLM 当异构处理器：将 skill 的需求分解成 primitive capability，测量每个模型和 harness 的组合支持到什么程度，再按这份能力画像编译 skill。 | [paper](https://arxiv.org/abs/2604.03088) |

<a id="routing"></a>

## 检索、选择与呈现

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-17 | **MetaSkill** — Where Natural Language Ends in Agents: Executable Skill Composition with MetaSkill | 保留每个 skill 包的自然语言内容，但把 skill 之间的调用顺序和上游输出的传递交给 DAG 运行时执行；在多 skill 产物任务上与纯自然语言流程、写进提示的图进行对比。 | [paper](https://arxiv.org/abs/2610.24723) · [code](https://github.com/TokenRhythm/opensquilla/tree/paper/metaskill-lp4fm-2026) |
| 2026-10-16 | **Code Skill Server** — Code Skill Server: A Large-Scale Search Engine for Code Generation Skills | 从多个来源持续收集并索引公开的代码生成 skill，为目标任务检索最有用的 skill 的搜索引擎；用多种检索方法在多个代码生成基准和模型上评测。 | [paper](https://arxiv.org/abs/2610.23186) · [code](https://github.com/haoyuli-sdu/CodeSkillServer) · [ICLR 2027 submission](https://openreview.net/forum?id=jKe0hrrk2U) |
| 2026-10-08 | **SkillContrast** — SkillContrast: Difference-Guided Text Selection for Agent Skill Reranking | 一个免训练的文本选择器，用于 skill 重排序：把检索到的 skill 互相比较，将它们有差异的段落连同局部上下文交给预训练的 reranker，使写法相近但适用条件不同的 skill 在较短的输入长度下仍能被区分。 | [paper](https://arxiv.org/abs/2610.11650) |
| 2026-10 | **SkillCraft** — SkillCraft: Skill-Set Retrieval Beyond Ranking for LLM Agents | 把检索后的 skill 选择从排序问题改为集合判定问题：基于列表内的相对证据估计非单调的成员概率，从而跳过排名靠前的干扰项，并用集合层面的校准决定纳入多少个 skill。 | [paper](https://openreview.net/forum?id=0HwdIddQeM) · ICLR 2027 submission |
| 2026-10 | **SkillCred** — SkillCred: Online Value Estimation for Evolving Agent Skills | 为每个演化中的 skill 保留多个竞争版本，从正常执行轨迹的局部进展信号在线估计其价值，用 Thompson 采样在版本间路由并决定晋升或归档。 | [paper](https://openreview.net/forum?id=9rc8Bl9gTD) · ICLR 2027 submission |
| 2026-10 | **SSG** — From Skills to Stages: Stage-Aware Graph Retrieval for Relevant Skills in Large-Scale Agent Skill Libraries | 把大规模 skill 库建成同时包含 skill 节点和 skill 内部阶段节点的图，通过阶段种子选择、阶段感知的 PageRank 和查询改写，为任务执行的不同阶段检索互补的 skill。 | [paper](https://openreview.net/forum?id=BvmLaGGL5h) · ICLR 2027 submission |
| 2026-10 | **Skill-as-Controller** — SKILL-AS-CONTROLLER: A NEW PARADIGM FOR SKILL UTILIZATION IN LONG-HORIZON AGENTS | 在每一步依据 skill 规则为候选动作打分，再通过 KL 正则化的闭式更新把这些 skill–动作一致性分数与基础动作分布结合，不改动模型参数。 | [paper](https://openreview.net/forum?id=K6Fpx45AP7) · ICLR 2027 submission |
| 2026-09-30 | **SkillSeek** — SkillSeek: Revisiting Agent Skill Retrieval at Marketplace Scale | 一个开源的两阶段 skill 检索器（双塔编码器加小型 cross-encoder，通过 MCP 提供），在 SkillsBench 上以低得多的成本达到与 LLM 介导的检索循环相当的效果。 | [paper](https://arxiv.org/abs/2609.38822) |
| 2026-09-26 | **SkillDelta** — When Does a Skill Add Value? Task-Conditional Gain Prediction for Selective Skill Use | 基于同一 agent 有无 skill 的配对执行，预测某个 skill 在具体任务上是否有益，并用局部预测器决定在新任务上何时启用 skill，无需重新训练 agent。 | [paper](https://arxiv.org/abs/2609.32274) · [code](https://github.com/TankTechnology/skilldelta) · [ICLR 2027 submission](https://openreview.net/forum?id=ABZmXDv352) |
| 2026-09-07 | **SkillAlign** — SkillAlign: Aligning Skill Interfaces for LLM-based Agents | 把候选 skill 表示成多视图的过程卡片，并用不同的呈现方式（完整指令、提示、压缩摘要、workflow、不呈现）交给 agent，从而能对“怎么呈现 skill”做反事实评测。 | [paper](https://arxiv.org/abs/2609.07255) |
| 2026-08-28 | **SkillDreamer** — Imagine Before Acting: Prospective Skill Identification for LLM Agents | 指出任务描述写的是目标、skill 文档写的是能力和流程，这种不对齐会让合适的 skill 在检索或调用时被漏掉；做法是先把执行所需的能力想象成 pseudo skill 来引导检索，执行过程中再随新出现的子任务重新判断该调用哪些 skill。 | [paper](https://arxiv.org/abs/2609.01642) · [ICLR 2027 submission](https://openreview.net/forum?id=zhLjwy8Fig) |
| 2026-08-10 | **Emotion2Skill** — Emotion2Skill: Model-Internal Emotion Signals for Adaptive Skill Selection and Evolution | 从 LLM 内部表示中提取情绪向量，既用于选择 skill，也用来标记有问题的调用，以便有针对性地修订 skill；在 WebShop 和 ALFWorld 上评测。 | [paper](https://arxiv.org/abs/2608.09248) · [code](https://github.com/BoHan-LIN04/Emotion2Skill) |
| 2026-08-07 | **SkillAligner** — SkillAligner: Treating Retrieved Skills as Adaptable Drafts at Execution Time | 形式化了 skill 与执行不匹配的问题，把检索到的 skill 当作可改的草稿：执行前做一次免训练的联合适配，让 skill 片段贴合任务，并让它的假设和执行接口对齐。 | [paper](https://arxiv.org/abs/2608.06880) |
| 2026-06-02 | **R3-Skill** — Skill Is Not Document: Query-Conditioned Compatibility for LLM Agent Skill Routing | 中英文 skill 检索基准，保留 LLM 对不合理 skill 组合的拒绝判断，作为与查询相关的兼容性监督；并在其上训练双编码器召回模型和交叉编码器重排模型。 | [paper](https://arxiv.org/abs/2606.03565) · [ICLR 2027 submission](https://openreview.net/forum?id=GPMWVYbVlL) |
| 2025-04-08 | **SkillFlow** — SkillFlow: Scalable and Efficient Agent Skill Retrieval System | 把获取 skill 看作在约 3.5 万个社区 SKILL.md 上的多阶段检索（稠密检索、两轮 cross-encoder 重排、LLM 选择），并发现只有语料里有目标领域可执行的 skill 时检索才有收益。 | [paper](https://arxiv.org/abs/2504.06188) · [code](https://github.com/IBPA/skill-flow) |

<a id="evaluation"></a>

## 基准与实证研究

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-19 | **SKILL-SIF** — How Effectively Do Security Skills Guide Coding Agents in Vulnerability Detection in Linux Kernel? | 大规模实证研究公开的安全类 skill 在 Claude Code（搭配多个底层 LLM）中检测真实 Linux 内核漏洞的效果并分析失败原因，同时提出 SKILL-SIF，依据漏报的漏洞和失败模式进化 skill，并在未见过的漏洞上测试。 | [paper](https://arxiv.org/abs/2610.25705) |
| 2026-10-18 | **SkillClash** — One Skill Takes Over: Clashing Agent Skills and a One-File Fix | 构建 SkillClash（同一任务的成对编码 skill，规则可由代码检查），发现两个 skill 同时加载时模型往往只遵循其中一个、丢掉另一个，原因在于 skill 内的示例；在每个 skill 末尾加一个同时遵循两者的示例，或把两者合并成一个文件，基本可以恢复遵循率。 | [paper](https://arxiv.org/abs/2610.25064) · [code](https://github.com/prazmara/skillclash) |
| 2026-10-13 | **Skill Inconsistencies at Runtime** — Why Static Skill Inconsistencies Do Not Equate to Runtime Risks: A Behavioral Analysis of LLM Agent Execution | 审计社区和基准 skill 包中文档、脚本与配置文件之间的冲突，再比较无 skill、原 skill、修复后 skill 三种设置下的执行，衡量这些静态缺陷实际在多大程度上改变 agent 行为。 | [paper](https://arxiv.org/abs/2610.18927) |
| 2026-10-08 | **One Skill Too Many** — One Skill Too Many: How Co-Installed Skills Conflict in Coding Agents | 对编程 agent 中同时安装、功能相同的 skill 之间的冲突做实证研究：从 20,947 个仓库的快照中挖掘，在三个模型上运行 312 对确认的 skill；相似的 skill 可能顶替已安装的那个并丢掉它的核心功能，而任务仍然通过。 | [paper](https://arxiv.org/abs/2610.11647) |
| 2026-10-06 | **An Empirical Study of Agent Skills' Downstream Utility** | 把下游效用定义为同一模型与 harness 配置下相对无 skill 运行的通过率差值，在 SkillsBench 的 87 个任务、九种配置上测量，并考察 marketplace 里的替代 skill 和多个 skill 的组织方式；在 36.78% 的任务上，同一批 skill 对一些配置有益、对另一些有害。 | [paper](https://arxiv.org/abs/2610.08875) |
| 2026-10-04 | **Skill Revisions Study** — Agent Skill Evolution: How Revisions Affect Coding Agents | 刻画开源项目中 SKILL.md 文件是如何被修订的，并测量增删规则对不同模型和 coding agent 的遵从度、动作执行率、正确性和 token 成本的影响。 | [paper](https://arxiv.org/abs/2610.04832) |
| 2026-10-02 | **SkillScriptBench** — SkillScriptBench: Benchmarking Self-Evolution of Executable Agent Skill Packages Beyond Markdown | 一个分别评估可执行 skill 包的文档修复、脚本修复和行为保持的基准，并提出用抽象语法树把维护需求关联到代码位置的修订方法。 | [paper](https://arxiv.org/abs/2610.04008) · [ICLR 2027 submission](https://openreview.net/forum?id=QsRBZC16Cv) |
| 2026-10-01 | **MCRI** — MCRI: A Four-Dimensional Framework for Analyzing and Evaluating Agent Skills | 一个四维的 agent skill 分析框架和基于 LLM 的评估方法，可在执行前评估 skill，应用于大规模公开 skill 库并用于 skill 选择。 | [paper](https://arxiv.org/abs/2610.01506) |
| 2026-10-01 | **Process-Level Skill Evaluation** — Continuous Process-Level Evaluation for Evolving Enterprise AI Agent Skills | 一个面向不断变化的企业级 agent skill 的持续评估框架，在最终输出检查之外加入工具选择、参数、执行顺序和数据库状态的过程级检查。 | [paper](https://arxiv.org/abs/2610.01833) |
| 2026-10 | **Understanding Agent Skills** — Understanding Agent Skills: How Well Do They Transfer to Smaller Models? | 一项实证研究，跨多个 skill 生成框架和模型家族，考察前沿模型产出的 skill 能不能帮到小得多的 agent；结论是强模型的 skill 并不能稳定地带来提升。 | [paper](https://openreview.net/forum?id=HupVHeskZE) · ICLR 2027 submission |
| 2026-10 | **SkillsBench-Compose** — When Skills Fail to Compose: Benchmarking and Compiling Agent Skills | 一个包含 20 个人工编写任务的基准，把各组件的要求和组件之间的关系分开打分，暴露出单独可用的 skill 组合起来失败的情况；同时提出 SkillCompiler，把给定的 skill 编译成一份针对任务的包。 | [paper](https://openreview.net/forum?id=mJyF7aM0bc) · ICLR 2027 submission |
| 2026-10 | **SciSkillBank** — SciSkillBank: A Dataset of Claude Code Skills for Scientific Research | 一个与科研相关的 Claude Code skill 仓库数据集，由 LLM 按科研阶段、是否包含方法知识和人工控制程度标注，并检验标签在不同提问方式和模型下的稳定性。 | [paper](https://openreview.net/forum?id=7HPYTLwNRG) · ICLR 2027 submission |
| 2026-10 | **PrivacySkills** — PrivacySkills: How Privacy Guidance Shapes Source Selection in LLM Agents | 一个受控评估框架，研究放在系统指令中和放在 skill 元数据标签中的隐私指导，分别如何影响 agent 对信息来源的选择。 | [paper](https://openreview.net/forum?id=7oN5Rjf8vo) · ICLR 2027 submission |
| 2026-10 | **SkillInertiaBench** — Following the Skill, Failing the Patient:Procedural Inertia in Clinical Agents | 一个经临床医生审核的基准，衡量临床 agent 在新证据使 skill 失效后仍继续执行它的“流程惯性”，并提出在推理时对照患者状态复核当前 skill 的门控机制。 | [paper](https://openreview.net/forum?id=8PYNWZs7MK) · ICLR 2027 submission |
| 2026-10 | **What Agent Skills Add** — What Agent Skills Add: A Causal Audit of Task Conventions | 用匹配的内容干预和预先登记的结论门槛做因果审计，区分两种情况：skill 只是补上了评测预期却没在任务里写明的约定，还是带来了可重复的能力提升；证据支持约定类指导的局部效应，但不支持一般性的机制。 | [paper](https://openreview.net/forum?id=HP8xFtGqk6) · ICLR 2027 submission |
| 2026-09-30 | **Do Self-Evolving Skills Generalize to Held-Out Tasks?** | 在六个基准上用相同的模型、agent 和训练/测试划分测试五种 skill 自进化方法和一个一次性生成的 skill：在训练任务上有提升的 21 个 skill 中，5 个在测试任务上保住了全部提升，13 个保住一部分，3 个完全没有保住；同时给出 GSO，只保留一份写 skill 的指南，对每个任务新写一个 skill。 | [paper](https://arxiv.org/abs/2609.39148) · [ICLR 2027 submission](https://openreview.net/forum?id=rM2eQio3e3) |
| 2026-09-30 | **EngramBench** — EngramBench: A Capability-Grounded Benchmark for Skill-Evolution Harnesses | 一个面向 skill 演化 harness 的基准，要求学习任务与迁移任务能力重叠而解法不重叠，以区分能力抽象和解法泄漏。 | [paper](https://arxiv.org/abs/2609.39284) |
| 2026-09-28 | **Progressive Disclosure** — Report: Progressive Disclosure of Agent Skills | 一份工业界报告，测量在已部署的 agent 中按需加载 skill 对检索质量和整体延迟的影响。 | [paper](https://arxiv.org/abs/2609.35692) |
| 2026-09-24 | **Smart Contract Audit Skills** — Demystifying Agent Skills for Smart Contract Auditing: Design, Effectiveness, Behavioral Impact | 收集 83 个真实环境中的智能合约审计 skill，在 EVMBench 上跨七种 agent 与模型组合评估其设计、效果和对执行轨迹的影响，发现 skill 能否被触发是主要瓶颈。 | [paper](https://arxiv.org/abs/2609.29454) |
| 2026-09-24 | **Plugin Migration Skill Study** — Evaluating Agent Skills for Version-Specific Plugin Migration: A Retrospective Study | 对一个已发布的插件升级 skill 做回顾性评估，把每个评分决定追溯到目标版本的契约，揭示 skill 增益背后的评分错误和对评审模型的敏感性。 | [paper](https://arxiv.org/abs/2609.30120) |
| 2026-09-17 | **EconSkills** — EconSkills: Studying Skill Transfer and Retrieval for Web Agents on Live Economic Data | 一个 skill 库和评测框架，把经过验证的 EconWebArena 轨迹蒸馏成参数化的标准操作流程，并把两个问题分开考察：已知相关的流程能否迁移到 held-out 任务，以及 agent 从 50 个 skill 的库里自行选择时这一收益能否保住。 | [paper](https://arxiv.org/abs/2609.19523) |
| 2026-08-22 | **Repo2Skill-Evo** — Repo2Skill-Evo: Repository Skills Go Stale in Silence | 把软件版本更替当作 skill 维护任务：agent 需要根据版本补丁更新仓库 skill，同时保留仍然有效的内容；在真实仓库上评测前沿 agent。 | [paper](https://arxiv.org/abs/2608.21964) · [ICLR 2027 submission](https://openreview.net/forum?id=JYd8XvwMkg) |
| 2026-08-07 | **SkillEval** — SkillEval: Decomposing Agent Skill Quality into Interpretable Signals | 对 SKILL.md 文档的通用属性给出方向固定、可解释的评分，并降低无关文档特征的干扰；这些分数可作为下游效果的早期信号，也用于指导有针对性的修订。 | [paper](https://arxiv.org/abs/2608.06891) |
| 2026-08-04 | **ContinualSkillBench** — ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities? | 一个面向上下文内持续 skill 学习的基准，含五个领域、按难度排序的任务；发现只保留上下文和反馈、不维护显式 skill 库时，平均表现与维护 skill 库相当，显式 skill 只在需要可复用流程或精确输出的任务上有选择性收益。 | [paper](https://arxiv.org/abs/2608.03874) |
| 2026-07-03 | **Shortening Skills** — Shortening agent skills leaves LLM agent cost unchanged | 在 SkillsBench 上的实证研究：对精选 skill 做压缩、用 LLM 改写或部分加载都没有降低单任务成本，LLM 改写还会降低小模型的成功率。 | [paper](https://arxiv.org/abs/2607.03048) |
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
| 2026-10 | **SkillCore** — From Loading Skills to Knowing Them: Scaffolding-Removed Fine-Tuning for Agent Skill Internalization | 一个数据流程和监督微调方案：从 agent 轨迹中去掉加载 skill 的脚手架，使通用 skill 内化进权重，同时混入少量原生调用 skill 的轨迹以保留对任务专用 skill 的调用。 | [paper](https://openreview.net/forum?id=2EC98UmU1e) · ICLR 2027 submission |
| 2026-10 | **CASU** — CASU: Case-to-Class Skill Synthesis with Adaptive Skill Utilization for LLM Agents | 把轨迹提炼成实例级再到类别级的 skill，并用 skill 吸收效率指标决定哪些 skill 通过蒸馏内化进参数、哪些保留为外部指导。 | [paper](https://openreview.net/forum?id=2uO2du40PO) · ICLR 2027 submission |
| 2026-10 | **ViSkill** — ViSkill: Reinforcing VLM Agents with Evolving Visual-Native Skills | 把成功交互编码成供 VLM agent 使用的视觉 skill 卡片，检索到的 skill 同时用于推理和奖励塑形，策略优化与 skill 积累相互促进。 | [paper](https://openreview.net/forum?id=4MqlhwiDQb) · ICLR 2027 submission |
| 2026-10 | **SCPO** — Skill in the Loop: Explicit Skill Declaration and Attribution for Agent Training | 让 agent 在每步行动前显式声明所依据的 skill，再利用对 skill 使用效果的回顾性反馈，同时用 GRPO 优化策略并更新 skill 库。 | [paper](https://openreview.net/forum?id=9EOpwpC7wW) · ICLR 2027 submission |
| 2026-10 | **Revise, Verify, Distill** — Revise, Verify, Distill: Self-Evolving Skills for Language Agent Learning | 借助环境验证逐条修复失败的 skill，把通过验证的 skill 归纳成冻结的 skill 库用于新任务，再用 EvoOPD 把这些修改内化进权重：这是一种 on-policy 蒸馏，用冻结基座模型在修复前后两个 skill 版本下对学生动作的评分差来加权。 | [paper](https://openreview.net/forum?id=BTSTI4cMH7) · ICLR 2027 submission |
| 2026-09-23 | **SkillGym** — SkillGym: Internalizing Human Skills into LLMs for Real-World Problem Solving | 把人写的 agent skill 转成带代码检查器的可验证训练环境，收集轨迹用于监督微调和基于结果奖励的强化学习，把 skill 内化进模型权重。 | [paper](https://arxiv.org/abs/2609.27717) · [ICLR 2027 submission](https://openreview.net/forum?id=Z3dXHNL258) |
| 2026-08-03 | **SKT** — SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation | 一个经过验证的数据合成流程：从公开 agent skill 构造单 skill 和多 skill 任务，只保留实际用到全部所需 skill 的可执行轨迹，用于监督微调模型的 skill 使用能力；同时发布一个留出的 skill 使用基准。 | [paper](https://arxiv.org/abs/2608.02287) |
| 2026-07-24 | **Skill-SP** — Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills | 把任务生成器、用强化学习训练的求解器和 skill 控制器放进同一个 self-play 循环：按采样到的 skill 生成任务，再用执行反馈更新和扩充 skill 库。 | [paper](https://arxiv.org/abs/2607.22529) · [code](https://github.com/Qwen-Applications/skill-self-play) · [ICLR 2027 submission](https://openreview.net/forum?id=07pvXM8POP) |

<a id="adjacent"></a>

## 邻近工作

| 日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-15 | **FAOPs** — FAOPs: Normal Forms and an Algebra for AI Agent Workflows | 为多步 agent skill（作者称 agent operating procedures）库提出形式化理论，定义分解、类型化、因子化、作用域受限四级范式以及可靠的等式改写代数，实现为管理系统 SkillBase，并以一个金融工作流示例说明，没有基准实验。 | [paper](https://arxiv.org/abs/2610.22061) |
| 2026-10-10 | **MetaCascade** — MetaCascade: End-to-End Attacks on Agent Skills via Metadata-Only Poisoning | 一种只篡改 skill 元数据的端到端攻击：先扩展出多个恶意候选，再用黑盒竞争反馈迭代优化元数据，使目标 skill 在检索和选择两步都能胜出。 | [paper](https://arxiv.org/abs/2610.14836) |
| 2026-10 | **SkillDOS** — SkillDOS: Token Amplification Attacks via Poisoned Skills in LLM Agents | 一种资源耗尽攻击：把投毒 skill 拆成诱导部分和放大部分，分两阶段优化，在保持最终答案不变的同时提高输出 token 消耗。 | [paper](https://openreview.net/forum?id=88AL9uYhnp) · ICLR 2027 submission |
| 2026-09-26 | **SkillDRE** — SkillDRE: Dual-Stage Red-Team Evolution of Agent Skills via Pre-Execution and Runtime Feedback | 通过闭环演化完整的恶意 skill 包：交替进行扫描器反馈引导的演化和防御下运行反馈引导的细化，同时保留正常任务能力。 | [paper](https://arxiv.org/abs/2609.32400) · [code](https://github.com/whfeLingYu/SkillDRE) · [ICLR 2027 submission](https://openreview.net/forum?id=XGBvOkQIzf) |
| 2026-09-07 | **AgentLeak** — AgentLeak: Cloning Stronger LLM Agent Capabilities onto Weaker Agents Beyond Skill Stealing | 一项安全研究：只泄露显式的 skill 工件并不能把能力转移给较弱的 agent，因为较强的 agent 还依赖隐式的过程行为；可以作为 skill 文本迁移存在上限的证据。 | [paper](https://arxiv.org/abs/2609.07131) |
| 2026-09-01 | **Defense-as-Skill** — Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents | 把防御恶意 skill 的运行时 guard 本身做成一个可安装、可编辑的 skill，按用户任务的边界检查敏感动作，并用由 rollout 反馈驱动的 Monte-Carlo tree search 改进这个 guard skill；收在这里是因为它是以安全为目标进化 skill 的例子。 | [paper](https://arxiv.org/abs/2609.01487) |
| 2026-08-22 | **SkillBloat** — SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents | 通过恶意 skill 放大 token 消耗的攻击：先在多种放大机制上筛选攻击类型，再用 LLM 引导的整篇 skill 改写细化最强的候选。 | [paper](https://arxiv.org/abs/2608.21929) · [ICLR 2027 submission](https://openreview.net/forum?id=8i0oGCFvw1) |
| 2026-08-13 | **Skill Misevolution** — Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents | 说明 skill 进化可能把不安全的流程留在一个本身有用的 skill 里，让之后的良性任务重复这一危害；构建了能分别检查写入和检索两个环节的 gym 和一个 525 个任务的基准，并提出 SafeEvolve，在 skill 写入时和被后续任务检索时各检查一次。 | [paper](https://arxiv.org/abs/2608.12851) · [code](https://github.com/henrymao2004/misevolve) |
| 2026-05-12 | **Proteus** — Proteus: A Self-Evolving Red Team for Agent Skill Ecosystems | 一个灰盒的自演化红队框架，根据审计结果和沙箱运行证据反复改写恶意 skill，用来度量有预算的自适应攻击者能多大程度绕过 skill 审核。 | [paper](https://arxiv.org/abs/2605.11891) |

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
