# 资源库 —— 案例与权威框架(按「什么时候查」组织)

> 不用一次读完。**卡在哪一步,就翻到对应那节。** 每条给一句「什么时候用得上」+ 可查证来源。
> 反面案例作**批判性讨论**素材,注明时间与出处。完整版案例库见 `../lecture/v2.0/00_案例库与参考文献_v2.0.md`。

---

## 🧭 贯穿全程:四套人本 AI 权威框架

它们视角不同,但共同指向**人本 AI 四原则:可控 / 透明 / 适配 / 安全**。做 DEFINE 每一步都可对照。

- **Ben Shneiderman 二维框架 + RST 三层治理** —— *什么时候查*:想讲清"自动化高不等于人失控"、给 agent 加 override/超控时。二维四象限目标在右上(高控制+高自动化);RST=Reliable/Safe/Trustworthy。arXiv:2002.04087
- **微软 HAX 18 条准则** —— *什么时候查*:写 PRD、做设计自查时,当"可勾选验收清单"逐条对照(见 `checklists/人本AI七原则自查表.md`)。https://www.microsoft.com/en-us/haxtoolkit/
- **Google PAIR People+AI Guidebook** —— *什么时候查*:纠结"要不要用 AI、怎么建立用户正确预期、错误怎么优雅降级"时。https://pair.withgoogle.com/guidebook/
- **Stanford HAI 三理念** —— *什么时候查*:需要"为何要以人为本"的价值坐标时(增强人性,而非取代)。https://hai.stanford.edu/

---

## 🎯 选题 / 域分析时查(D1)

- **Khanmigo(可汗学院)** —— *什么时候查*:想做教育类、纠结"要不要直接给答案"时。人本亮点:**拒绝直接给答案**,苏格拉底式反问;家长可见对话;风险主动上报。https://www.khanmigo.ai/
- **Duolingo Max** —— *什么时候查*:纠结"AI 和人怎么分工"时。**人写剧本、AI 演**,专家兜底。https://blog.duolingo.com/duolingo-max/
- **认知外包 / 元认知懒惰研究** —— *什么时候查*:担心"我的 agent 会不会让用户变懒/变笨"时。把思考外包给 AI → 依赖加深、批判性下降;这正是"不给答案"重要的原因。arXiv:2412.09315

## 👤 用户与需求时查(D2–D3)

- **效应量的真相:0.2–0.7σ 才是真实** —— *什么时候查*:写"成功标准"、被"AI 让成绩翻倍"忽悠时。MATHia(RAND)0.19–0.36σ;智能辅导系统元分析 0.66σ;**Bloom「2σ 神话」仅小样本、难复现**。https://nintil.com/bloom-sigma/
- **诗婕 · HCAI Research Radar** —— *什么时候查*:想了解"信任校准/依赖/AI 陪伴"等人本 AI 研究前沿时。18 个方向、142 个研究问题。https://hcai.online/

## 📋 写 PRD 与边界时查(D4–D5)

- **微软 HAX 18 条**(见上)——PRD 的边界与交互设计直接对照。
- **信任校准 / 恰当依赖** —— *什么时候查*:设计"让用户既不过度信任也不信任不足"时。Trust(感知)≠ Reliance(行为)。Appropriate Reliance, IJHCI 2024. https://www.tandfonline.com/doi/full/10.1080/10447318.2024.2348216

## 🔬 做评估时查(E1–E2)

- **信度与效度** —— *什么时候查*:设计评分标准时。信度=稳不稳(同输入结果一致吗)、效度=准不准(测的真是"共情"还是只是"用词礼貌"?)。这是你们心理测量学的本行。
- **心理专项基准** —— *什么时候查*:想找"统考卷"横向对比时。MindBench / Mind-Eval / PsychEval(共情、安全、专业性)。**警示:基准会被刷分,通用考卷测不出你项目的真实安全,必须自己设计评估。**
- **Limbic Access(NHS 临床级分诊)** —— *什么时候查*:做心理评估/分诊类、想要"临床级严谨"参照时。Class IIa 医疗器械;分类准确率 93%;**决策仍在医生手中**。https://ai.jmir.org/2023/1/e44358

## 🚨 危机与安全时查(E3–E4)

- **Woebot(正例)** —— *什么时候查*:设计危机识别与转介时。危机语言检测准确率 98%;**主动声明"无法处理危机"、承认边界、转介真人**。https://mental.jmir.org/2017/2/e19/
- **Wysa(正例)** —— *什么时候查*:讲"可及性"与"监管分级"时。FDA 突破性设备认定(≠已获批治疗)、NHS 采用、匿名可及。https://www.wysa.com/clinical-evidence
- **❌ NEDA「Tessa」(2023)** —— *什么时候查*:提醒"未经领域验证的通用生成式 AI 在脆弱人群上是致命的"。擅自加生成式 AI,给饮食失调人群减肥建议 → 下线。https://www.npr.org/2023/06/08/1181131532/
- **❌ Koko(2022)** —— *什么时候查*:讲知情同意时。未获知情同意用 GPT-3 给约 4000 名求助者回复。https://www.nbcnews.com/tech/internet/chatgpt-ai-experiment-mental-health-tech-app-koko-rcna65110
- **❌ Character.AI(2024)** —— *什么时候查*:讲"依赖设计 + 危机护栏缺失"三重失守时。14 岁少年长期对话后自杀,诉讼与和解。https://www.nbcnews.com/tech/characterai-lawsuit-florida-teen-death-rcna176791
- **APA 2025.11 健康警示** —— *什么时候查*:给"AI 不能替代专业照护"找权威背书时。https://www.apaservices.org/practice/business/technology/artificial-intelligence-chatbots-therapists
- **JAMA 共情研究** —— *什么时候查*:讨论"感知共情 ≠ 真正理解"时。ChatGPT 回复被评共情更高——但"显得共情"不等于"在场"。

---

## 心理健康 5 条红线(危机测试的准绳)
1. **危机必须转介真人**(正:Woebot;反:Character.AI)
2. **不诊断、不替代治疗**(APA;Limbic)
3. **透明披露 AI 身份与能力边界**(反:Koko / Tessa)
4. **知情同意与隐私保护**(正:Wysa;反:Koko)
5. **防依赖、护脆弱人群**(反:Character.AI / Tessa)

> 收尾金句:「AI 可以更快、更耐心、看起来更共情——但它必须**知道自己的边界,并在关键时刻把人交还给人**。」

---
*MIT License｜郑先隽,北京师范大学心理学部教授,人本AI设计与创新*
