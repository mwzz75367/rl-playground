
import streamlit as st

st.set_page_config(
    page_title="环境实验室",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 环境实验室")

st.caption("Environment Laboratory")

st.divider()

st.subheader("环境列表")

st.info(
    "环境模块正在开发中。"
)

st.markdown("""
未来支持：

- GridWorld
- Gymnasium
- MuJoCo
- ManiSkill
- Isaac Lab
""")
