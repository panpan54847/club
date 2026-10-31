"""
可视化模块 - 展示线性回归拟合结果和损失下降曲线

依赖: matplotlib (pip install matplotlib)
如果没安装，会自动降级为纯文本输出
"""

import os
from typing import List


def setup_chinese_font():
    """配置 matplotlib 中文字体，避免中文显示为方块"""
    try:
        import matplotlib.pyplot as plt
        from matplotlib import font_manager
    except ImportError:
        return None

    # 常见中文字体候选（Windows / macOS / Linux）
    candidates = [
        'Microsoft YaHei', 'SimHei', 'SimSun', 'PingFang SC',
        'Heiti SC', 'WenQuanYi Micro Hei', 'Noto Sans CJK SC', 'Arial Unicode MS',
    ]

    # 先查系统已安装的字体
    installed = {f.name for f in font_manager.fontManager.ttflist}
    for name in candidates:
        if name in installed:
            plt.rcParams['font.sans-serif'] = [name]
            plt.rcParams['axes.unicode_minus'] = False  # 修复负号显示
            return name

    # 兜底：直接按文件路径注册
    for path in ['C:/Windows/Fonts/msyh.ttc', 'C:/Windows/Fonts/simhei.ttf']:
        if os.path.exists(path):
            font_manager.fontManager.addfont(path)
            prop = font_manager.FontProperties(fname=path)
            plt.rcParams['font.sans-serif'] = [prop.get_name()]
            plt.rcParams['axes.unicode_minus'] = False
            return prop.get_name()

    plt.rcParams['axes.unicode_minus'] = False
    return None


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

    # 配置中文字体
    font_name = setup_chinese_font()
    if font_name:
        print(f"[字体] 使用中文字体: {font_name}")
    else:
        print("[提示] 未找到中文字体，图中的中文可能显示为方块。")

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
