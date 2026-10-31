# club - 算法入门实践项目

两个用于上手的优化算法项目，纯 Python 实现，无第三方依赖（matplotlib 仅用于可选的可视化）。

## 项目列表

| 项目 | 目录 | 算法 | 说明 |
|------|------|------|------|
| 模拟退火 | `simulated_annealing/` | Simulated Annealing | 解决 TSP 快递配送路线规划 |
| 梯度下降 | `gradient_descent/` | Gradient Descent | 线性回归预测房价 |

## 快速开始

在 club 根目录运行（推荐）：

```bash
python run.py           # 查看项目列表
python run.py sa        # 运行模拟退火
python run.py gd        # 运行梯度下降
python run.py all       # 依次运行全部
```

或者进入子目录单独运行：

```bash
cd simulated_annealing
python main.py
```

## 可视化（可选）

两个项目都会在各自目录下生成 `result.png`。需要安装 matplotlib：

```bash
pip install matplotlib
```

- `simulated_annealing/result.png` — 左：最优配送路线图；右：退火收敛曲线
- `gradient_descent/result.png` — 左：数据散点 + 拟合直线；右：MSE 下降曲线

## 环境要求

- Python 3.8+
- matplotlib（可选，仅用于生成图片）

## 目录结构

```
club/
├── run.py                    # 一键运行入口
├── .gitignore
├── simulated_annealing/
│   ├── main.py               # 主程序
│   ├── annealing.py          # 模拟退火核心算法
│   ├── visualize.py          # 可视化
│   └── README.md
└── gradient_descent/
    ├── main.py               # 主程序
    ├── gradient.py           # 梯度下降核心算法
    ├── visualize.py          # 可视化
    └── README.md
```
