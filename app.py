import streamlit as st
import random

# --- 1. 语料库 (保持你的专业描述) ---
CONDITION_DATA = ["全新", "几乎全新", "轻微使用痕迹", "明显使用痕迹"]
CHAT_COMPONENTS = {
    "hooks": ["懂行的兄弟看过来，", "这杆子有点意思，", "实话实说，", "真心分享个好东西，", "老粉都知道我不推烂货，", "今天给哥们儿放个福利，"],
    "sources": ["是老主顾刚从我这升级万级好杆换下来的，", "当初我也是求了半天才从球友手里抢回来的，", "这是我店里压箱底的一根好木头，", "帮一个要出国退坑的哥们代出的，", "最近手里货实在太多了，腾个位置给新货，"],
    "verdicts": ["打感确实惊艳到我了，绝对不是那种流水线通货。", "纹路看图就懂，这种老料子现在的行情可遇不可求。", "我自己偷偷下场打了几把，传力反馈真的透，舍不得出。", "东西保正，品质我亲自背书，闭眼入就行。"]
}
SMALL_FEEL = ["由于是老料白蜡木一体成型，整体锥度过渡非常顺滑，", "这根前节的木纤维非常紧密，传力那叫一个透，反馈清晰，"]
LARGE_FEEL = ["分体接口连接非常致密，12.5mm的原厂标准锥度，", "前节硬度极高，支撑性非常强，高强度先角配合优质枫木，"]

# --- 2. 网页界面 ---
st.set_page_config(page_title="安仔球杆行情工具", page_icon="🎱")
st.title("🎱 安仔二手球杆工具")

# 球杆类型选择
cue_type = st.radio("球杆类型", ["小头杆", "大头杆"], horizontal=True)

# 联动逻辑：默认材质
mat_default_index = 0 if cue_type == "小头杆" else 1

# --- 品牌输入逻辑改进 ---
brand_list = ["野豹", "皮尔力", "美兹", "美洲豹", "天工", "威利", "奥斯本兹", "南匠",  "其他（手动输入）"]
col_b1, col_b2 = st.columns([1, 1])

with col_b1:
    brand_choice = st.selectbox("选择品牌", brand_list)

# 如果选择了“其他”，则显示手动输入框
if brand_choice == "其他（手动输入）":
    brand = st.text_input("请输入品牌名称", placeholder="例如：FURY、GOGO等")
else:
    brand = brand_choice

# --- 其他参数输入 ---
col1, col2 = st.columns(2)
with col1:
    model = st.text_input("型号", value="石家班5")
with col2:
    material = st.selectbox("材质", ["白蜡木", "枫木", "碳纤维", "黑科技"], index=mat_default_index)

col3, col4 = st.columns(2)
with col3:
    price = st.text_input("一口价", value="1500")
with col4:
    condition = st.selectbox("成色", CONDITION_DATA, index=1)

# 配件勾选
st.write("**配件选择**")
acc_options = ["手套", "巧克", "毛巾", "加长把", "杆盒", "杆包"]
acc_cols = st.columns(3)
selected_accs = [acc for i, acc in enumerate(acc_options) if acc_cols[i % 3].checkbox(acc)]

# 生成按钮
if st.button("🚀 生成专业文案", use_container_width=True):
    if not brand:
        st.error("请先输入或选择品牌！")
    else:
        chat = random.choice(CHAT_COMPONENTS["hooks"]) + random.choice(CHAT_COMPONENTS["sources"]) + random.choice(CHAT_COMPONENTS["verdicts"])
        feel = random.choice(SMALL_FEEL if cue_type == "小头杆" else LARGE_FEEL)
        taper = f"{random.choice([10.1, 10.2, 10.3, 10.4, 10.5])}mm" if cue_type == "小头杆" else "12.5mm"
        acc_str = "、".join(selected_accs) if selected_accs else "无（裸杆）"

        desc = f"""{brand}{model} | {cue_type} | {material} | {condition} | 顺丰包邮

{chat}

{feel}接口连接极其严丝合缝，整体保养得非常用心，上手就能打。

【参数】
* 球杆品牌：{brand} {model}
* 杆头锥度：{taper}
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
        st.code(desc, language="markdown")
