"""
可视化模块 - 展示模拟退火过程和结果

依赖: matplotlib (pip install matplotlib)
如果没安装，会自动降级为纯文本输出
"""

import os
from typing import List, Tuple

Point = Tuple[float, float]


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


def try_plot(cities: List[Point], best_route: List[int], history: List[float]):
    """
    尝试用 matplotlib 绘图：
    - 左图：城市坐标 + 最优路线
    - 右图：退火过程中最优距离的收敛曲线
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib
        # 使用非交互后端，避免窗口弹窗问题
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

    # ---- 左图：路线 ----
    route_x = [cities[i][0] for i in best_route]
    route_y = [cities[i][1] for i in best_route]
    ax1.plot(route_x, route_y, 'b-o', markersize=8, linewidth=1.5)
    ax1.plot(route_x[0], route_y[0], 'r^', markersize=15, label='起点')
    
    for i, (x, y) in enumerate(cities):
        ax1.annotate(f'  {i}', (x, y), fontsize=10)
    
    ax1.set_title('最优配送路线', fontsize=14)
    ax1.set_xlabel('X 坐标')
    ax1.set_ylabel('Y 坐标')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # ---- 右图：收敛曲线 ----
    ax2.plot(history, 'g-', linewidth=1.5)
    ax2.set_title('退火过程：最优距离收敛', fontsize=14)
    ax2.set_xlabel('冷却步数')
    ax2.set_ylabel('最短距离')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    
    output_path = os.path.join(os.path.dirname(__file__), "result.png")
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"[可视化] 结果已保存到: {output_path}")
    return output_path
