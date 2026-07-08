# -*- coding: utf-8 -*-
"""1_DEFINE_guide 模块导览 deck —— Fathom 数据叙事风 (Path A, html2pptx 原生可编辑).
画布 960x540px. 与 lecture/v2.0 数据叙事风、2_hcai_guide slides 同源。"""
import os

BG="#FFFFFF"; INK="#2B2B2B"; NAVY="#1A365D"; ACC="#C2410C"
GREEN="#2D7D46"; RED="#B03A2E"; GREY="#8A8A8A"; LINE="#E3E1DC"
PANEL="#F6F4EF"; NAVYT="#EAF0F6"
FCJK="'PingFang SC','Helvetica Neue',sans-serif"
FNUM="'Helvetica Neue','PingFang SC',Arial,sans-serif"
W,H=960,540; MX=56; CW=W-2*MX

def rect(x,y,w,h,fill=None,border=None,bw=1.5,radius=0):
    s=f"position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;box-sizing:border-box;"
    if fill:s+=f"background:{fill};"
    if border:s+=f"border:{bw}px solid {border};"
    if radius:s+=f"border-radius:{radius}px;"
    return f'<div style="{s}"></div>'
def hline(x,y,w,color=NAVY,h=2): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};"></div>'
def vline(x,y,h,color=NAVY,w=2): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};"></div>'
def txt(x,y,w,s,size=17,color=INK,weight=400,align="left",lh=1.35,tag="p",font=FCJK,ls="0px"):
    st=(f"position:absolute;left:{x}px;top:{y}px;width:{w}px;margin:0;padding:0;"
        f"font-family:{font};font-size:{size}px;color:{color};font-weight:{weight};"
        f"text-align:{align};line-height:{lh};letter-spacing:{ls};")
    return f'<{tag} style="{st}">{s}</{tag}>'
def bullets(x,y,w,items,size=15,color=INK,lh=1.6,gap=4):
    lis="".join(f'<li style="margin:0 0 {gap}px 0;padding:0;">{it}</li>' for it in items)
    st=(f"position:absolute;left:{x}px;top:{y}px;width:{w}px;margin:0;padding:0 0 0 18px;"
        f"font-family:{FCJK};font-size:{size}px;color:{color};line-height:{lh};list-style:disc;")
    return f'<ul style="{st}">{lis}</ul>'
def kicker(k): return txt(MX,38,CW,k.upper(),12,NAVY,700,ls="1.5px")
def title(t,y=60,size=32,color=INK): return txt(MX,y,CW,t,size,color,700,lh=1.18)
def rule(y,x=MX,w=54): return hline(x,y,w,ACC,3)
def foot(deck,page): return [txt(MX,512,460,deck,11,GREY,500),txt(W-140,512,84,f"{page:02d}",11,GREY,600,align="right",font=FNUM)]
def source(s,y=508,x=MX): return txt(x,y,CW,s,11,GREY,400,lh=1.3)
def page(bl):
    body=("<body style='margin:0;padding:0;width:960px;height:540px;position:relative;"
          f"background:{BG};overflow:hidden;'>"+"".join(bl)+"</body>")
    return ("<!doctype html><html><head><meta charset='utf-8'>"
            "<style>*{box-sizing:border-box;}p,h1,h2,h3,h4,ul,li{margin:0;}</style></head>"+body+"</html>")

def cards(items,y,h,accents=None,gap=18,top=18,bodysize=13):
    n=len(items); cw=(CW-gap*(n-1))//n; b=[]
    for i,(lab,tt,bd) in enumerate(items):
        x=MX+i*(cw+gap); acc=accents[i] if accents else NAVY
        b.append(rect(x,y,cw,h,fill="#FFFFFF",border=LINE,bw=1.4)); b.append(vline(x,y,h,acc,4))
        if lab: b.append(txt(x+16,y+top,cw-26,lab.upper(),11,acc,700,ls="1px"))
        b.append(txt(x+16,y+top+(20 if lab else 0),cw-26,tt,16,INK,700,lh=1.22))
        b.append(txt(x+16,y+top+(48 if lab else 26),cw-26,bd,bodysize,INK,400,lh=1.5))
    return b

DECK="1_DEFINE_guide · 双支柱方法论"; P=[]

# 1 cover
P.append(page([
    rect(0,0,W,6,fill=NAVY),
    txt(MX,120,CW,"1_DEFINE_guide",52,NAVY,800,font=FNUM,lh=1.0),
    rule(196,MX,72),
    txt(MX,216,CW,"DEFINE 与 Eval 双支柱方法论",34,INK,800,lh=1.2),
    txt(MX,278,CW,"好 agent 的两道功夫:先「定义清楚」,再「评估到位」",18,GREY,500),
    txt(MX,340,CW,"DEFINE THE RIGHT THING · EVALUATE IT RIGHT",12,NAVY,700,ls="2px"),
    txt(MX,470,CW,"面向零 UX / 产品背景的心理与教育本科生",13,GREY,400),
]))
# 2 positioning
b=[kicker("定位 · WHERE THIS FITS"),title("模块 0/1 给了你手,这个模块给你眼睛和心"),rule(112)]
b+=cards([("模块 0 / 1","造 agent 的手","s0–s5 造行为 · c0–c5 造框架:你已经会「造」"),
          ("本模块 1_DEFINE","定义 + 评估的眼睛和心","造什么、为谁、边界在哪;凭什么说它行、安不安全"),
          ("模块 2_hcai","idea→impact 全程","把这套方法用到一个完整项目并上线")],
         178,196,accents=[NAVY,ACC,NAVY])
b.append(txt(MX,404,CW,"本模块是 2_hcai_guide 全流程的「方法论前置地基」——先学会想清楚、评明白。",13,GREY,500))
b+=foot(DECK,2); P.append(page(b))
# 3 why define & eval
b=[kicker("为什么 · WHY THESE TWO"),title("两个最难、最像「专业判断」的环节"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill=NAVYT,border=NAVY,bw=1.6),
    txt(MX+20,196,360,"DEFINE 定义",15,NAVY,800),
    txt(MX+20,224,(CW-24)//2-40,"动手写 prompt 之前",20,INK,800),
    bullets(MX+20,266,(CW-24)//2-46,["为谁造?解决什么?边界在哪?","对话怎么流动?何时让人把关?","这是<b>设计</b>,不是编程"],14.5)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FBF1EC",border=ACC,bw=1.8),
    txt(x2+20,196,360,"EVAL 评估",15,ACC,800),
    txt(x2+20,224,(CW-24)//2-40,"能跑 ≠ 能用 ≠ 该用",20,INK,800),
    bullets(x2+20,266,(CW-24)//2-46,["凭什么说它有用、安全、稳定?","不是「我试了感觉不错」","这是<b>科学</b>,不是感觉"],14.5)]
b.append(txt(MX,428,CW,"这两件事正好是心理/教育专业的主场:用户研究、信度效度、伦理边界。",13,GREY,500))
b+=foot(DECK,3); P.append(page(b))
# 4 three advantages
b=[kicker("你的优势 · YOUR EDGE"),title("你有工程师没有的三重优势"),rule(112)]
b+=cards([("懂 人","访谈·共情·需求洞察","「为人而设计」是你的基本功,不是工程师的"),
          ("懂 测量","信度·效度·量表设计","科学地测量看不见的东西,是心理测量学的本行"),
          ("懂 边界","「不伤害」的伦理直觉","对危机、隐私、越界最敏感——安全的第一道防线")],
         178,196,accents=[NAVY,NAVY,ACC])
b.append(txt(MX,404,CW,"工程师会写代码;但「为人而造、为人负责」这件事,你更在行。",13,GREY,500))
b+=foot(DECK,4); P.append(page(b))
# 5 DEFINE six-step split
b=[kicker("主线 · D.E.F.I.N.E."),title("DEFINE 六步,天然分成两半"),rule(112)]
steps=[("D","域分析",NAVY),("E","体验",NAVY),("F","功能",NAVY),
       ("I","实现",GREY),("N","测试",ACC),("E","演化",ACC)]
cw=(CW-5*10)//6
for i,(L,t,acc) in enumerate(steps):
    x=MX+i*(cw+10); y=176
    b.append(rect(x,y,cw,104,fill=("#FBF1EC" if acc==ACC else "#FFFFFF"),border=(acc if acc!=GREY else LINE),bw=(1.8 if acc!=GREY else 1.3)))
    b.append(txt(x,y+16,cw,L,30,acc,800,align="center",font=FNUM))
    b.append(txt(x,y+62,cw,t,13,INK,600,align="center"))
b+=[rect(MX,300,(CW-24)//3*1-8,64,fill=NAVYT,border=NAVY,bw=1.4),
    txt(MX+14,314,240,"D·E·F = 定义支柱",13,NAVY,800),
    txt(MX+14,336,240,"想清楚造什么、为谁、边界",11.5,GREY,500)]
xa=MX+(CW-24)//3
b+=[rect(xa+8,300,(CW-24)//3-16,64,fill=PANEL,border=LINE,bw=1.3),
    txt(xa+22,314,240,"I = 实现",13,GREY,800),
    txt(xa+22,336,240,"在模块 0/1 已学,本模块不重复",11.5,GREY,500)]
xb=MX+2*(CW-24)//3
b+=[rect(xb+16,300,(CW-24)//3-8,64,fill="#FBF1EC",border=ACC,bw=1.6),
    txt(xb+30,314,240,"N·E = 评估支柱",13,ACC,800),
    txt(xb+30,336,240,"证明行不行、安不安全 + 迭代",11.5,GREY,500)]
b.append(txt(MX,392,CW,"阅读顺序 = 设计顺序:先想清楚「领域和人」,最后才写 prompt。最常见的错就是一上来写 prompt。",13,GREY,500))
b+=foot(DECK,5); P.append(page(b))

# 6 SECTION DEFINE
P.append(page([rect(0,0,W,H,fill=NAVY),
    txt(MX,150,CW,"PILLAR 01",16,"#8FB0CC",800,ls="3px",font=FNUM),rule(196,MX,72),
    txt(MX,214,CW,"定义支柱 · DEFINE",44,"#FFFFFF",800),
    txt(MX,290,CW,"D 域分析 → E 体验与需求 → F 功能与边界",19,"#C6D6E6",500),
    txt(MX,470,CW,"产出:一张 DEFINE 设计卡(T5)——想清楚再动手",13,"#8FB0CC",400)]))
# 7 D0 好agent≠好模型 + 双钻石
b=[kicker("D0 · 好 agent ≠ 好模型"),title("模型只是一环,设计的是「人 + AI」的整体体验"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill="#FFFFFF",border=LINE,bw=1.4),vline(MX,178,232,NAVY,5),
    txt(MX+20,196,360,"第一颗钻 · 找对问题",15,NAVY,800),
    bullets(MX+20,228,(CW-24)//2-44,["D 发散调研 → E 收敛定义","很多项目失败,是一开始就在解决错的问题","先搞懂「人和领域」"],14.5)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FFFFFF",border=ACC,bw=1.6),vline(x2,178,232,ACC,5),
    txt(x2+20,196,360,"第二颗钻 · 做对方案",15,ACC,800),
    bullets(x2+20,228,(CW-24)//2-44,["F 发散构思 → I 收敛做原型","别听到需求就冲去写代码(单钻石)","每一步先张开、再收拢"],14.5)]
b.append(source("双钻石 Double Diamond · Don Norman《设计心理学》· Google PAIR",470))
b+=foot(DECK,7); P.append(page(b))
# 8 D1 域分析
b=[kicker("D1 · 域分析 DOMAIN"),title("找「专家行为里那个缺失的、可被 AI 补位的环节」"),rule(112)]
b+=[rect(MX,178,516,232,fill="#FFFFFF",border=LINE,bw=1.4),vline(MX,178,232,NAVY,5),
    txt(MX+22,196,470,"范例 · 小智",13,NAVY,700,ls="1px"),
    bullets(MX+22,226,470,["舒华四层提问法教具,<b>前提是旁边有个「会提问的大人」</b>","凉山乡村课堂:那位大人常缺席","小智 = 把引导者行为<b>可规模化补位</b>,不取代老师"],14.5,lh=1.7)]
x2=MX+516+16
b+=[rect(x2,178,CW-516-16,232,fill=NAVYT,border=LINE,bw=1.2),
    txt(x2+18,196,150,"选题三标准",12,NAVY,700,ls="1px"),
    bullets(x2+18,226,150,["小切口高刚需","可 Agent 化","人本价值明确"],13.5,lh=1.9)]
b.append(source("证据链表达:结论来自 3 句用户原话,不是「我觉得」;AI 拆活,人把关",470))
b+=foot(DECK,8); P.append(page(b))
# 9 D2-D3 用户+需求
b=[kicker("D2 – D3 · 体验与需求"),title("为「一个具体的人」设计,而不是一个标签"),rule(112)]
b+=cards([("用户建模 T2","四要素画像","他几岁?此刻在哪?拿什么设备?心情如何?"),
          ("三层需求 T3","刚性 / 情感 / 成长","要学会 / 被鼓励不被评判 / 独立表达"),
          ("旅程地图 T3","痛点·情绪·AI介入点","逐阶段标:哪里卡住、什么情绪、AI 何时介入")],
         178,200,accents=[NAVY,ACC,NAVY])
b.append(txt(MX,408,CW,"情感与成长需求,决定 agent 的语气与「什么时候该退场」。",13,GREY,500))
b+=foot(DECK,9); P.append(page(b))
# 10 D4 PRD与边界
b=[kicker("D4 · PRD 与边界"),title("边界是灵魂:先写清楚它「不做什么」"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill="#FFFFFF",border=NAVY,bw=1.5),
    txt(MX+20,196,360,"PRD 六要素",15,NAVY,800),
    bullets(MX+20,228,(CW-24)//2-44,["问题 · 用户 · 核心功能","<b>边界</b> · 成功标准 · 风险","边界写进产品,不靠用户自觉"],14.5,lh=1.7)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FBECEA",border=RED,bw=1.6),
    txt(x2+20,196,360,"红黄绿数据分级",15,RED,800),
    bullets(x2+20,228,(CW-24)//2-44,["<b>红</b>:真实咨询记录/可识别身份 → 禁用","<b>黄</b>:脱敏 + 授权后可用","<b>绿</b>:公开,可直接用"],14.5,lh=1.7)]
b.append(txt(MX,428,CW,"每用一个数据,先问一句它是红、黄、还是绿——数据伦理的第一道闸。",13,GREY,500))
b+=foot(DECK,10); P.append(page(b))
# 11 D5 人设与工作流
b=[kicker("D5 · 人设与工作流"),title("人设三段式 + 工作流 + 三种记忆 → 设计卡"),rule(112)]
b+=cards([("人设三段式","身份 · 语气 · 边界","系统提示写死:我是谁、怎么说话、绝不做什么"),
          ("工作流四件套","触发·循环·工具·边界","什么时候动、怎么一轮轮走、调什么、到哪停"),
          ("三种记忆","情景·语义·程序","记得住关系;化名脱敏存储(Tulving)")],
         172,182,accents=[NAVY,ACC,NAVY])
b+=[rect(MX,366,CW,48,fill=NAVYT,border=LINE,bw=1.2),
    txt(MX+18,380,CW-36,"safety_check 红黄绿:识别危机 → <b>静默上报真人</b>,绝不自行处理。这一步整合成 T5 DEFINE 设计卡。",13,INK,500,lh=1.3)]
b+=foot(DECK,11); P.append(page(b))

# 12 SECTION EVAL
P.append(page([rect(0,0,W,H,fill=NAVY),
    txt(MX,150,CW,"PILLAR 02",16,"#8FB0CC",800,ls="3px",font=FNUM),rule(196,MX,72),
    txt(MX,214,CW,"评估支柱 · EVAL",44,"#FFFFFF",800),
    txt(MX,290,CW,"能跑 ≠ 能用 ≠ 该用:用证据说话",19,"#C6D6E6",500),
    txt(MX,470,CW,"信度、效度、危机测试——这是你们心理学生的主场",13,"#8FB0CC",400)]))
# 13 E0 能跑≠能用 + 信效度
b=[kicker("E0 · 为何评估难"),title("同一个问题问三次,答案都不一样,怎么评?"),rule(112)]
b+=[rect(MX,178,516,232,fill="#FFFFFF",border=LINE,bw=1.4),vline(MX,178,232,ACC,5),
    txt(MX+22,196,470,"LLM agent 的五个难点",13,ACC,700,ls="1px"),
    bullets(MX+22,226,470,["黑盒 · 概率 · 无限输入空间","<b>语义失败</b>:语法对、听着顺,意思却错或有害","误差传播:多步任务里前一步的小错被放大"],14.5,lh=1.7)]
x2=MX+516+16
b+=[rect(x2,178,CW-516-16,232,fill=NAVYT,border=LINE,bw=1.2),
    txt(x2+18,196,160,"你的主场",12,NAVY,700,ls="1px"),
    txt(x2+18,222,160,"信度",16,NAVY,800),txt(x2+18,244,180,"稳不稳:结果一致吗",12,GREY,500),
    txt(x2+18,276,160,"效度",16,NAVY,800),txt(x2+18,298,180,"准不准:测的真是你想测的吗",12,GREY,500,lh=1.3)]
b.append(source("「流畅温暖 ≠ 安全」:越流畅的错建议越危险。评估三问:有用吗?安全吗?稳定吗?",470))
b+=foot(DECK,13); P.append(page(b))
# 14 E1 四维 quadrant
b=[kicker("E1 · 四维评估模型"),title("四维画像,不是一个会骗人的总分"),rule(112)]
gx=MX+70; gw=CW-70; cwd=(gw-14)//2; chd=112
cells=[("① 技术","稳定 · 鲁棒 · 边界",NAVY,""),("② UX 人本","可用 · 共情 · 可控",NAVY,""),
       ("③ 专业有效","教育价值 / 心理有效",ACC,"!"),("④ 伦理合规","隐私 · 合规 · 权责",NAVY,"")]
pos=[(gx,168),(gx+cwd+14,168),(gx,168+chd+14),(gx+cwd+14,168+chd+14)]
for (cx,cy),(tt,bd,acc,mk) in zip(pos,cells):
    strong=acc==ACC
    b.append(rect(cx,cy,cwd,chd,fill=("#FBF1EC" if strong else "#FFFFFF"),border=(acc if strong else LINE),bw=(2.2 if strong else 1.3)))
    if mk: b.append(txt(cx+cwd-30,cy+8,22,mk,16,acc,800,align="right"))
    b.append(txt(cx+16,cy+14,cwd-46,tt,15,(acc if strong else INK),700))
    b.append(txt(cx+16,cy+40,cwd-30,bd,12.5,INK if strong else GREY,400,lh=1.4))
b.append(txt(MX,462,CW,"一个 78 分的 agent,可能安全维只有 40——安全一票否决,画雷达一眼看出短板。",13,GREY,500))
b+=foot(DECK,14); P.append(page(b))
# 15 E2 三视角 + judge
b=[kicker("E2 · 三视角与 LLM 评委"),title("只看结果的评估是脆弱的"),rule(112)]
b+=cards([("三视角","过程·工具·结果","结果对不代表过程对——它可能蒙对了"),
          ("LLM-as-Judge","让 AI 批量打分","陷阱:偏爱长答案、偏爱第一个、自评偏高"),
          ("对策","校准评委","rubric 写细 · 位置随机 · 独立模型 · 人工抽检")],
         178,200,accents=[NAVY,ACC,NAVY])
b.append(source("基准 GAIA/SWE-bench/τ²-bench · 心理专项 MindBench/Mind-Eval/PsychEval(会被刷分,不能只看基准)",470))
b+=foot(DECK,15); P.append(page(b))
# 16 E3 危机 + redteam
b=[kicker("E3 · 危机测试与红队"),title("评估不是打分,是想办法「攻破它」"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill="#FBECEA",border=RED,bw=1.8),
    txt(MX+20,196,360,"危机测试必测输入",14,RED,800),
    bullets(MX+20,228,(CW-24)//2-44,["自伤自杀 / 暴力 / 饮食失调","未成年人求助与情绪崩溃","合格:识别 + 声明边界 + 转介真人"],14,lh=1.7)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FFFFFF",border=NAVY,bw=1.5),
    txt(x2+20,196,360,"Red-team 四连问",14,NAVY,800),
    bullets(x2+20,228,(CW-24)//2-44,["它说能做的,拿什么证明?","什么输入会让它出丑?","换人评还一样吗?我怎么诱导它越界?"],14,lh=1.7)]
b.append(txt(MX,428,CW,"安全一票否决:危机测试一条不过,整体不通过。课堂上全班一起当复核人。",13,GREY,500))
b+=foot(DECK,16); P.append(page(b))
# 17 E4 自检环
b=[kicker("E4 · 迭代自检环"),title("「诊断 > 再试一次」"),rule(112)]
loop=[("① 生成","先给一个回答"),("② 验证","独立检查:对不对、安不安全"),
      ("③ 反思","诊断哪错了,不是盲目重试"),("④ 纠正","针对性改,再输出")]
cw=(CW-3*14)//4
for i,(t,d) in enumerate(loop):
    x=MX+i*(cw+14); y=178
    b.append(rect(x,y,cw,150,fill="#FFFFFF",border=LINE,bw=1.4))
    b.append(txt(x+14,y+16,cw-24,t,16,NAVY,800))
    b.append(hline(x+14,y+48,cw-28,LINE,1))
    b.append(txt(x+14,y+62,cw-24,d,12.5,INK,400,lh=1.5))
    if i<3: b.append(txt(x+cw-2,y+64,16,"→",18,ACC,800))
b.append(txt(MX,352,CW,"外部反馈胜内部自省(让另一个 agent 审)。三层优化:技术 / UX / 专业话术。护栏四道:输入·输出·HITL→GITL·可观测。",13,GREY,500))
b+=foot(DECK,17); P.append(page(b))

# 18 three projects
b=[kicker("参考答案 · EXAMPLE PROJECT"),title("三个真实项目,就是你的三份参考答案"),rule(112)]
b+=cards([("小智 · Reading Bot","DEFINE 全六步范本","舒华四层提问法 + Harness四件套 + 优雅失败 + safety"),
          ("Agent Leo","F 功能:persona + 多agent","112 大师 SKILL.md · 圆桌 vs 自由 编排"),
          ("HEAI","N 测试:评估科学","强制引用 grounding + red-team + 雷达多维")],
         178,200,accents=[ACC,NAVY,NAVY])
b.append(txt(MX,408,CW,"看颗粒度,别照抄。三项目均已真实上线(reading-bot / deepsy.ai)。",13,GREY,500))
b+=foot(DECK,18); P.append(page(b))
# 19 skills + paths
b=[kicker("怎么用 · HOW TO USE"),title("八个教练 skill + 三条使用路径"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill="#FFFFFF",border=LINE,bw=1.4),vline(MX,178,232,NAVY,5),
    txt(MX+20,196,360,"/define-* · /eval-* 教练",14,NAVY,800),
    bullets(MX+20,226,(CW-24)//2-44,["define: domain·persona·needs·prd·flow","eval: design·crisis·iterate","<b>教练不是枪手</b>:提问、检查、陪跑"],14,lh=1.7)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FBF1EC",border=ACC,bw=1.6),
    txt(x2+20,196,360,"三条路径(可混用)",14,ACC,800),
    bullets(x2+20,226,(CW-24)//2-44,["跟着走:D0→D5、E0→E4,过门禁","让 AI 带着走:启动 skill","对照示例:看三项目颗粒度"],14,lh=1.7)]
b.append(txt(MX,428,CW,"红线:选题、画像、评估数据必须是你自己的——虚构数据 = 学术不端。",13,RED,600))
b+=foot(DECK,19); P.append(page(b))
# 20 closing
P.append(page([rect(0,0,W,6,fill=NAVY),
    txt(MX,120,CW,"带走两句话",13,NAVY,700,ls="2px"),rule(156,MX,72),
    txt(MX,184,CW-40,"「先想清楚领域和人,再写 prompt。」",32,INK,800,lh=1.3),
    txt(MX,244,CW-40,"「能跑不等于能用,能用不等于该用——",32,INK,800,lh=1.3),
    txt(MX,288,CW-40,"用证据说话,安全一票否决。」",32,ACC,800,lh=1.3),
    txt(MX,372,CW,"定义清楚 + 评估到位,是你把专业变成产品的两道功夫。",16,GREY,500),
    txt(MX,470,CW,"郑先隽 · 北京师范大学心理学部 · 人本 AI 设计与创新",13,GREY,400)]))

HERE=os.path.dirname(os.path.abspath(__file__))
d=os.path.join(HERE,"html"); os.makedirs(d,exist_ok=True)
for i,html in enumerate(P,1):
    open(os.path.join(d,f"{i:02d}.html"),"w",encoding="utf-8").write(html)
print(f"{len(P)} pages")
