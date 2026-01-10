import streamlit as st
import random

# --- 1. 安全合规语料库 (v2.3) ---
CORPUS = {
    "老哥闲聊": {
        "hooks": ["懂球的兄弟看过来，", "实话说，这根杆子挺顺手，", "老粉都知道我不整虚的，", "刚试打了两杆，反馈很稳，", "真心分享个实用货，", "给哥们儿推个性价比高的，"],
        "sources": ["是老客户刚升级换下来的，", "帮球友代出的闲置，", "店里收回来的一根老料，", "老主顾置换的回血款，", "我自己留着打过一段时间，", "朋友出国托我处理的，东西正，"],
        "verdicts": ["打感确实可以，不是那种通货能比的。", "木纹看图，这种老料子现在很难得了。", "传力反馈很直接，没有发空的感觉。", "东西保真，成色对得起这个价。", "料子选得挺扎实，在这个价位很能打。", "上手就能感觉到，是一根好干活的杆子。"]
    },
    "专业发烧友": {
        "hooks": ["【自用转让】出一根底子不错的", "【球友进】分享一根保养到位的", "客观评价一下这根", "物理性能保持得很好的"],
        "sources": ["一直作为主力杆使用，木性已经稳定，", "因为入手了定制杆，这根闲置了，", "纯粹因为杆盒放不下了，腾个地儿，", "这根前节的传力反馈在这个价位里很难得，", "前节自然风干，稳定性保持得不错，"],
        "verdicts": ["力量损耗很小，发力很整。", "整体重心分布合理，控球手感细腻。", "反馈比较敏锐，能清晰感觉到皮头触球。", "点位比较准，下塞修正量可控。", "实战利器，无论是走位还是准度都很稳。"]
    },
    "急售回血风": {
        "hooks": ["手慢无！诚心出，", "全网比价，这成色这价格很合适，", "亏本赚个名声，看上的速度，", "不墨迹！直接到底价，捡漏的来，", "急用钱回血，忍痛出了，"],
        "sources": ["刚收回来还没捂热，急需周转直接出，", "本来留着自用的，今天放福利，", "这就是纯粹的捡漏价，对比行情就知道，", "家里领导让清仓，懂的都懂，", "性价比很高，买到就是赚到，"],
        "verdicts": ["这价格基本就是买前节送后把。", "成色摆在这，同价位里很难找到第二根。", "东西保正保直，爽快的包邮。", "实物比照片有质感，拿去打球不丢面。", "闭眼入，这个价格以后出手也不亏。"]
    }
}

# --- 2. 打感描述 (去风险化) ---
FEEL_SMALL = [
    "一体白蜡木前节，木质紧密，传力通透。", 
    "配置原装铜箍，反馈清晰，中高杆发力脆。", 
    "整体锥度过渡自然，弹性与硬度平衡得不错。",
    "传力感很整，击球声音清脆。",
    "前节硬度够，小力控球细腻，大力出杆不飘。"
]
FEEL_LARGE = [
    "分体结构连接紧实，12.5mm标准锥度，支撑性强。", 
    "高硬度先角配合枫木前节，下塞偏移小，表现稳定。", 
    "爆发力足，白球旋转强，击球音色扎实。",
    "长台表现稳健，没有明显的虚位。",
    "打感扎实，传力反馈没有延迟感。"
]

# --- 3. 网页配置 ---
st.set_page_config(page_title="安仔球杆文案专业版", page_icon="🎱")

# 手机端CSS优化（按钮更大，更好点）
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; height: 3em; background-color: #28a745; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎱 安仔二手球杆工具 (合规版)")

# --- 4. 核心选项 ---
# 风格选择 (Radio)
style_label = st.radio(
    "文案风格", 
    ["捡漏回血 (急售)", "江湖老哥 (亲切)", "专业发烧 (严谨)"], 
    horizontal=True
)

# 映射回语料库的Key
if "捡漏" in style_label:
    style_key = "急售回血风"
elif "江湖" in style_label:
    style_key = "老哥闲聊"
else:
    style_key = "专业发烧友"

# 球杆类型
cue_type = st.radio("球杆类型", ["小头杆", "大头杆"], horizontal=True)

# 材质自动联动逻辑
mat_default_index = 0 if cue_type == "小头杆" else 1

# 品牌输入 (纯手动)
brand = st.text_input("品牌 (直接输入)", value="野豹", placeholder="例如：奥斯本兹、天工")

# 其他参数
col1, col2 = st.columns(2)
with col1:
    model = st.text_input("型号", value="石家班5")
with col2:
    material = st.selectbox("材质", ["白蜡木", "枫木", "碳纤维", "黑科技"], index=mat_default_index)

col3, col4 = st.columns(2)
with col3:
    price = st.text_input("一口价", value="1500")
with col4:
    condition = st.selectbox("成色", ["全新", "几乎全新", "轻微使用痕迹", "明显使用痕迹"], index=1)

# 配件勾选
st.write("**配件赠送**")
acc_options = ["手套", "巧克", "毛巾", "加长把", "杆盒", "杆包"]
acc_cols = st.columns(3)
selected_accs = [acc for i, acc in enumerate(acc_options) if acc_cols[i % 3].checkbox(acc)]

# --- 5. 生成逻辑 ---
if st.button("🚀 生成合规文案"):
    if not brand:
        st.error("请先填写品牌名称！")
    else:
        # 随机组合
        style_lib = CORPUS[style_key]
        chat = random.choice(style_lib["hooks"]) + random.choice(style_lib["sources"]) + random.choice(style_lib["verdicts"])
        feel = random.choice(FEEL_SMALL if cue_type == "小头杆" else FEEL_LARGE)
        taper = f"{random.choice([10.0, 10.1, 10.2, 10.3, 10.4, 10.5])}mm" if cue_type == "小头杆" else "12.5mm"
        
        acc_str = "、".join(selected_accs) if selected_accs else "无（裸杆）"
        
        # 急售风增加紧迫感文案
        if style_key == "急售回血风":
            scarcity_msg = "【特别提醒】此价仅限今天，看中直接敲。"
        else:
            scarcity_msg = "【诚意转让】寻找爱球的有缘人。"

        # 组装文案 (v2.3 合规结构)
        desc = f"""{brand}{model} | {cue_type} | {material} | {condition} | 顺丰包邮

{chat}

{feel} 接口连接紧实，保养到位。{scarcity_msg}

【核心参数】
* 球杆品牌：{brand} {model}
* 杆头锥度：{taper}
* 材质说明：{material}
* 整体成色：{condition}（细节见图）

【关于配件】
买就送：{acc_str}。

【售后保障】
1. **支持试打**：支持到货当天试打（不动皮头不磕碰），不满意承担往返运费退回即可。
2. **永久回收**：在我这买的杆子，**永久行情价回收**！想换装备随时回来，无忧换新。

【一口价】
**{price}元**（顺丰包邮）。
价格实在，诚心要的兄弟直接拍。🤝

#台球 #台球杆 #{brand} #二手球杆行情 #{cue_type} #捡漏"""

        st.subheader("📋 生成结果")
        st.code(desc, language="markdown")
        st.success(f"已生成【{style_label}】风格文案，长按上方代码块即可复制！")
