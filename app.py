import streamlit as st


st.set_page_config(
    page_title="RL Playground",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 RL Playground")
st.caption("An Interactive Reinforcement Learning Laboratory")

st.write(
    "欢迎来到 RL Playground。我们将从 GridWorld 和经典强化学习算法开始，"
    "逐步构建一个可解释、可复现的强化学习实验平台。"
)

st.info("当前版本：项目初始化阶段。下一步将实现 GridWorld 环境。")

left, right = st.columns(2)

with left:
    st.subheader("学习路线")
    st.markdown(
        """
        1. 强化学习基本概念
        2. 马尔可夫决策过程（MDP）
        3. GridWorld 环境
        4. Q-learning 与 SARSA
        5. DQN、PPO、SAC
        6. 机器人仿真实验
        """
    )

with right:
    st.subheader("项目原则")
    st.markdown(
        """
        - 算法与界面分离
        - 先理解原理，再实现代码
        - 每个模块都进行测试
        - 记录随机种子与实验参数
        """
    )
