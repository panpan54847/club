"""
可视化模块 - 展示线性回归拟合结果和损失下降曲线

依赖: matplotlib (pip install matplotlib)
如果没安装，会自动降级为纯文本输出
"""

import os
from typing import List


def try_plot(X: List[float], y_true: List[float], w: float, b: float, loss_history: List[float]):
    """
    绘制两张图：
    - 左图：数据散点 + 拟合直线
    - 右图：损失（MSE）下降曲线
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use("Agg")
    except ImportError:
        print("[提示] 未安装 matplotlib，跳过绘图。")
        print("       安装方法: pip install matplotlib")
        return None

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # ---- 左图：散点 + 拟合直线 ----
    ax1.scatter(X, y_true, c='blue', alpha=0.6, label='真实数据', zorder=5)
    
    # 画拟合直线
    x_min, x_max = min(X), max(X)
    y_min = w * x_min + b
    y_max = w * x_max + b
    ax1.plot([x_min, x_max], [y_min, y_max], 'r-', linewidth=2, label=f'y = {w:.2f}x + {b:.2f}')
    
    ax1.set_title('房价预测：线性回归拟合', fontsize=14)
    ax1.set_xlabel('房屋面积（平米）')
    ax1.set_ylabel('房价（万元）')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # ---- 右图：损失曲线 ----
    ax2.plot(loss_history, 'g-', linewidth=1.5)
    ax2.set_title('损失下降曲线（MSE）', fontsize=14)
    ax2.set_xlabel('迭代轮数')
    ax2.set_ylabel('MSE')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    
    output_path = os.path.join(os.path.dirname(__file__), "result.png")
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"[可视化] 结果已保存到: {output_path}")
    return output_path
