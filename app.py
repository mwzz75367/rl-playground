
import streamlit as st

st.set_page_config(
    page_title="RL Playground",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 RL Playground")

st.caption(
    "An Interactive Reinforcement Learning Laboratory"
)

st.markdown("---")

st.header("欢迎来到 RL Playground")

st.write(
    """
    RL Playground 是一个用于强化学习算法研究、
    实验和可视化的开源平台。

    我们将逐步构建经典强化学习算法、
    深度强化学习算法和机器人仿真实验模块。
    """
)

st.subheader("平台功能")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌍 环境实验室")
    st.write("管理和运行强化学习实验环境。")

    st.markdown("### 🧠 算法实验室")
    st.write("管理不同强化学习算法。")

with col2:
    st.markdown("### 📊 实验分析")
    st.write("分析训练过程和实验结果。")

    st.markdown("### 📚 项目文档")
    st.write("查看项目说明和开发文档。")

st.divider()

st.info(
    "当前版本：v0.2-dev | "
    "项目正在持续开发中。"
)
