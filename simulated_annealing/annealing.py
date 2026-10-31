"""
模拟退火算法核心实现 - 解决TSP（旅行商问题）

核心思想：
- 高温时大胆接受劣解，探索更多可能性
- 低温时趋于保守，收敛到最优解
- 通过 Metropolis 准则决定是否接受劣解
"""
import random
import math
from typing import List, Tuple


Point = Tuple[float, float]


def distance(p1: Point, p2: Point) -> float:
    """计算两点之间的欧氏距离"""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def total_distance(route: List[int], cities: List[Point]) -> float:
    """
    计算路线总距离（能量/成本函数）
    
    参数:
        route: 城市访问顺序的索引列表，如 [0, 2, 1, 3, 0]
        cities: 城市坐标列表
    
    返回:
        总距离（从起点出发，经过所有城市，回到起点）
    """
    dist = 0.0
    for i in range(len(route) - 1):
        dist += distance(cities[route[i]], cities[route[i + 1]])
    return dist


def get_neighbor(route: List[int]) -> List[int]:
    """
    生成邻域解：随机交换路线中两个城市的位置
    
    参数:
        route: 当前路线
    
    返回:
        新路线（深拷贝，不修改原路线）
    """
    new_route = route[:]
    i, j = random.sample(range(1, len(route) - 1), 2)
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route


def metropolis(delta_e: float, temperature: float) -> bool:
    """
    Metropolis 准则：决定是否接受劣解
    
    - 如果新解更好（delta_e < 0），直接接受
    - 如果新解更差（delta_e > 0），以 exp(-delta_e / temperature) 的概率接受
    
    参数:
        delta_e: 能量变化（新能量 - 旧能量），正值表示变差
        temperature: 当前温度
    
    返回:
        是否接受新解
    """
    if delta_e < 0:
        return True
    if temperature <= 0:
        return False
    accept_prob = math.exp(-delta_e / temperature)
    return random.random() < accept_prob


def simulated_annealing(
    cities: List[Point],
    initial_temp: float = 1000.0,
    cooling_rate: float = 0.995,
    min_temp: float = 1.0,
    iterations_per_temp: int = 100,
) -> Tuple[List[int], float, List[float]]:
    """
    模拟退火算法主函数
    
    参数:
        cities: 城市坐标列表
        initial_temp: 初始温度（越高越容易探索）
        cooling_rate: 冷却系数（每轮温度乘以此值，越接近1冷却越慢）
        min_temp: 最低温度（低于此温度停止）
        iterations_per_temp: 每个温度下的迭代次数
    
    返回:
        (最优路线, 最短距离, 历史距离记录)
    """
    n = len(cities)
    
    # 初始路线：0 -> 1 -> 2 -> ... -> n-1 -> 0
    current_route = list(range(n)) + [0]
    current_energy = total_distance(current_route, cities)
    
    best_route = current_route[:]
    best_energy = current_energy
    
    temperature = initial_temp
    history = [current_energy]  # 记录每次迭代的最优距离，用于可视化
    
    while temperature > min_temp:
        for _ in range(iterations_per_temp):
            # 1. 生成邻域解
            new_route = get_neighbor(current_route)
            new_energy = total_distance(new_route, cities)
            
            # 2. 计算能量变化
            delta_e = new_energy - current_energy
            
            # 3. Metropolis 准则决定是否接受
            if metropolis(delta_e, temperature):
                current_route = new_route
                current_energy = new_energy
                
                # 4. 更新全局最优
                if current_energy < best_energy:
                    best_energy = current_energy
                    best_route = current_route[:]
        
        # 记录当前最优
        history.append(best_energy)
        
        # 5. 冷却
        temperature *= cooling_rate
    
    return best_route, best_energy, history
