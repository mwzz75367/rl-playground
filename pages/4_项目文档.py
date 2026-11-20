
import streamlit as st

st.set_page_config(
    page_title="项目文档",
    page_icon="📚",
    layout="wide"
)

st.title("📚 项目文档")

st.caption("Documentation")

st.divider()

st.subheader("项目介绍")

st.write(
    "RL Playground 是一个开源强化学习实验平台。"
)

st.subheader("技术栈")

st.markdown("""
- Python
- Streamlit
- NumPy
- PyTorch
- Matplotlib
- Pytest
""")

st.subheader("项目地址")

st.markdown(
    "[GitHub Repository](https://github.com/mwzz75367/rl-playground)"
)
