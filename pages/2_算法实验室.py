
import streamlit as st

st.set_page_config(
    page_title="算法实验室",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 算法实验室")

st.caption("Algorithm Laboratory")

st.divider()

st.subheader("算法列表")

st.info(
    "算法模块正在开发中。"
)

st.markdown("""
未来支持：

- Q-learning
- SARSA
- DQN
- PPO
- SAC
- TD3
""")
