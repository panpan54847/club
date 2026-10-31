"""
模拟退火算法 - 快递配送路线规划（TSP）
主程序入口

运行方式: python main.py
"""

import random
from annealing import simulated_annealing, total_distance
from visualize import try_plot


def generate_cities(n: int = 10, seed: int = 42) -> list:
    """
    随机生成 n 个快递点坐标
    
    参数:
        n: 快递点数量
        seed: 随机种子（保证可复现）
    
    返回:
        城市坐标列表 [(x1, y1), (x2, y2), ...]
    """
    random.seed(seed)
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]


def print_route(route, cities):
    """打印路线详情"""
    print("\n========== 最优路线 ==========")
    for i, idx in enumerate(route):
        x, y = cities[idx]
        if i == 0:
            print(f"  起点  → 快递点{idx}  坐标({x:.1f}, {y:.1f})")
        elif i == len(route) - 1:
            print(f"  回起点 → 快递点{idx}  坐标({x:.1f}, {y:.1f})")
        else:
            print(f"  第{i}站 → 快递点{idx}  坐标({x:.1f}, {y:.1f})")
    print("=" * 30)


def main():
    print("=" * 50)
    print("  模拟退火算法 - 快递配送路线规划（TSP）")
    print("=" * 50)

    # 1. 生成快递点
    num_cities = 10
    cities = generate_cities(n=num_cities, seed=42)
    print(f"\n[1] 已生成 {num_cities} 个快递点：")
    for i, (x, y) in enumerate(cities):
        print(f"    快递点{i}: ({x:.1f}, {y:.1f})")

    # 2. 计算初始路线距离（顺序访问）
    initial_route = list(range(num_cities)) + [0]
    initial_dist = total_distance(initial_route, cities)
    print(f"\n[2] 初始路线（按顺序）总距离: {initial_dist:.2f}")

    # 3. 运行模拟退火
    print(f"\n[3] 开始模拟退火优化...")
    print(f"    初始温度: 1000.0")
    print(f"    冷却系数: 0.995")
    print(f"    每个温度迭代: 100 次")

    best_route, best_dist, history = simulated_annealing(
        cities=cities,
        initial_temp=1000.0,
        cooling_rate=0.995,
        min_temp=1.0,
        iterations_per_temp=100,
    )

    print(f"\n[4] 优化完成！")
    print(f"    最短距离: {best_dist:.2f}")
    print(f"    初始距离: {initial_dist:.2f}")
    improvement = (1 - best_dist / initial_dist) * 100
    print(f"    优化幅度: {improvement:.1f}%")

    # 4. 打印路线
    print_route(best_route, cities)

    # 5. 可视化
    print(f"\n[5] 生成可视化...")
    try_plot(cities, best_route, history)

    print("\n完成！")


if __name__ == "__main__":
    main()
