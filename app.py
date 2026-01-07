import streamlit as st
import random

# --- 1. 语料库配置 (完全保留你的最新版本) ---
CONDITION_DATA = ["全新", "几乎全新", "轻微使用痕迹", "明显使用痕迹"]

CHAT_COMPONENTS = {
    "hooks": ["懂行的兄弟看过来，", "这杆子有点意思，", "实话实说，", "真心分享个好东西，", "老粉都知道我不推烂货，",
              "今天给哥们儿放个福利，", "这根杆子我得夸两句，", "刚拍完视频，手感还没忘，"],
    "sources": ["是老主顾刚从我这升级万级好杆换下来的，", "当初我也是求了半天才从球友手里抢回来的，",
                "这是我店里压箱底的一根好木头，", "帮一个要出国退坑的哥们代出的，",
                "最近手里货实在太多了，腾个位置给新货，", "老客户置换回来的回血款，性价比无敌，",
                "这根是我自己留着打的主力杆，最近想换手感了，"],
    "verdicts": ["打感确实惊艳到我了，绝对不是那种流水线通货。", "纹路看图就懂，这种老料子现在的行情可遇不可求。",
                 "我自己偷偷下场打了几把，传力反馈真的透，舍不得出。", "这价格和这个成色，基本就是给老哥们捡漏用的。",
                 "东西保正，品质我亲自背书，闭眼入就行。"]
}

SMALL_FEEL_COMPONENTS = {
    "starts": ["整体锥度过渡非常顺滑，", "这根前节的木纤维非常紧密，"],
    "cores": ["传力那叫一个透，完全没有力量损耗，", "击球瞬间反馈极其清晰，点位非常精准，",
              "弹性与硬度的比例拿拿捏得刚好，韧性十足，", "打感扎实得像直接用手抓球，反馈非常通透，"],
    "ends": ["拉杆和塞球的偏移量控制得很稳。", "中高杆击球声音很清脆，一点不震手。",
             "特别是打中八贴库球的时候，手感很扎实。", "对于追求细腻控球的兄弟来说，这根是极品。"]
}

LARGE_FEEL_COMPONENTS = {
    "starts": ["分体接口连接非常致密，", "12.5mm的原厂标准锥度，", "前节硬度极高，支撑性非常强，",
               "高强度先角配合优质枫木，"],
    "cores": ["爆力击球时毫无颤动，传力非常‘整’，", "偏移量极低，远台长台基本不用怎么让点，",
              "下塞时的力量回馈非常直接，爆发力十足，", "白球的旋转效率非常高，塞力反馈很清脆，"],
    "ends": ["大跨度拉杆非常轻松，不费力。", "稳定性在同价位里绝对是天花板级别的。", "声音很扎实。",
             "这种反馈极其敏锐，上手就能感觉到好坏。"]
}

# --- 2. 网页设置 ---
st.set_page_config(page_title="安仔球杆行情工具", page_icon="🎱")

# 手机端样式优化
st.markdown("""
    <style>
    .main { max-width: 600px; margin: 0 auto; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #d9534f; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎱 安仔二手球杆工具")

# --- 3. 输入区域 ---

# 球杆类型选择 (联动逻辑)
cue_type = st.radio("球杆类型", ["小头杆", "大头杆"], horizontal=True)

# 自动联动材质预选
if cue_type == "小头杆":
    mat_default_index = 0  # 白蜡木
    taper_default = f"{random.choice([10.0, 10.1, 10.2, 10.3, 10.4, 10.5])}mm"
else:
    mat_default_index = 1  # 枫木
    taper_default = "12.5mm"

col1, col2 = st.columns(2)
with col1:
    brand = st.selectbox("品牌", ["野豹", "皮尔力", "美兹", "美洲豹", "天工", "威利", "奥斯本兹"])
    model = st.text_input("型号", value="石家班5")
with col2:
    # 材质列表根据你的 tkinter 代码对应
    mat_list = ["白蜡木", "枫木", "碳纤维", "黑科技"]
    material = st.selectbox("材质", mat_list, index=mat_default_index)
    price = st.text_input("价格", value="1500")

condition = st.selectbox("成色", CONDITION_DATA, index=1)

# 配件勾选
st.write("**配件选择**")
acc_options = ["手套", "巧克", "毛巾", "加长把", "杆盒", "杆包"]
acc_cols = st.columns(3)
selected_accs = []
for i, acc in enumerate(acc_options):
    if acc_cols[i % 3].checkbox(acc):
        selected_accs.append(acc)

# --- 4. 文案生成 ---
if st.button("✨ 生成专业文案"):
    # 随机组合逻辑
    chat = random.choice(CHAT_COMPONENTS["hooks"]) + random.choice(CHAT_COMPONENTS["sources"]) + random.choice(CHAT_COMPONENTS["verdicts"])
    feel_lib = SMALL_FEEL_COMPONENTS if cue_type == "小头杆" else LARGE_FEEL_COMPONENTS
    feel = random.choice(feel_lib["starts"]) + random.choice(feel_lib["cores"]) + random.choice(feel_lib["ends"])
    
    acc_str = "、".join(selected_accs) if selected_accs else "无（裸杆）"

    # 按照你最新的文案结构组装
    desc = f"""{brand}{model} | {cue_type} | {material} | {condition} | 顺丰包邮


{chat}


{feel} 接口连接极其严丝合缝，整体保养得非常用心，上手就能打。

【参数】
* 球杆品牌：{brand} {model}
* 杆头锥度：{taper_default}
* 材质说明：{material}
* 整体成色：{condition}

【关于配件】
买就送：{acc_str}。

【售后保障】
1. **支持试打**：支持到货当天试打（不动皮头不磕碰），不满意承担往返运费退回即可。
2. **永久回收**：在我这买的杆子，**永久包回收**！以后想升级或换装备随时行情价收回，无忧换新。

【关于价格】
一口价：**{price}元**（顺丰包邮）。
拒绝套路，诚信第一，看好了直接敲我。🤝

#台球 #台球杆 #{brand} #二手球杆行情 #{cue_type} #顺丰包邮"""

    st.subheader("📋 生成结果")
    # Streamlit 自带复制按钮在代码块右上角
    st.code(desc, language="markdown")
    st.success("手机端：长按上方灰色区域即可全选复制。")
