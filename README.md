# RL Playground

An interactive, open-source laboratory for learning and visualizing reinforcement learning.

> 当前版本：项目初始化阶段（v0.1-dev）

## 项目目标

RL Playground 从简单的 GridWorld 和表格型强化学习开始，逐步扩展到深度强化学习与机器人仿真实验。

当前开发重点：

- [ ] GridWorld 环境
- [ ] Random Agent
- [ ] Q-learning
- [ ] SARSA
- [ ] 训练过程与策略可视化
- [ ] DQN / PPO / SAC
- [ ] 机器人仿真实验

## 环境要求

- Python 3.11
- Conda（推荐）或 Python venv
- Git

## Windows + Anaconda 安装

在 Anaconda Prompt 中执行：

```bash
conda create -n rl_playground python=3.11 -y
conda activate rl_playground
```

进入项目根目录后安装依赖：

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

启动网页：

```bash
streamlit run app.py
```

运行测试：

```bash
pytest
```

## 项目结构

```text
rl-playground/
├── app.py
├── requirements.txt
├── README.md
├── rl_playground/
│   ├── environments/
│   ├── algorithms/
│   └── visualization/
├── tests/
└── docs/
```

## 开发原则

1. 算法实现与网页展示分离。
2. 优先自己实现经典算法，理解后再使用成熟算法库。
3. 每个算法都配套测试、实验记录和说明文档。
4. 实验尽量记录随机种子、超参数和评估结果。
5. 先完成小而可靠的版本，再逐步扩展。

## Roadmap

详见 [`docs/roadmap.md`](docs/roadmap.md)。

## License

项目公开发布前，请选择并添加开源许可证。若采用 MIT License，请填写正确的版权持有人信息。
