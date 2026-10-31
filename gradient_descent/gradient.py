"""
梯度下降核心实现 - 一元线性回归预测房价

模型: y = wx + b
损失: MSE = (1/n) * Σ(y_pred - y_true)²
梯度: ∂L/∂w = (2/n) * Σ((y_pred - y_true) * x)
      ∂L/∂b = (2/n) * Σ(y_pred - y_true)
更新:  w = w - lr * ∂L/∂w
       b = b - lr * ∂L/∂b
"""

from typing import List, Tuple
import random


def predict(x: float, w: float, b: float) -> float:
    """前向预测: y = wx + b"""
    return w * x + b


def compute_mse(X: List[float], y_true: List[float], w: float, b: float) -> float:
    """
    计算均方误差（MSE）
    
    MSE = (1/n) * Σ(y_pred - y_true)²
    """
    n = len(X)
    total = 0.0
    for i in range(n):
        y_pred = predict(X[i], w, b)
        total += (y_pred - y_true[i]) ** 2
    return total / n


def compute_gradients(X: List[float], y_true: List[float], w: float, b: float) -> Tuple[float, float]:
    """
    计算梯度（对 w 和 b 分别求偏导）
    
    ∂L/∂w = (2/n) * Σ((y_pred - y_true) * x)
    ∂L/∂b = (2/n) * Σ(y_pred - y_true)
    
    返回:
        (grad_w, grad_b)
    """
    n = len(X)
    grad_w = 0.0
    grad_b = 0.0
    
    for i in range(n):
        y_pred = predict(X[i], w, b)
        error = y_pred - y_true[i]
        grad_w += error * X[i]
        grad_b += error
    
    grad_w = (2 / n) * grad_w
    grad_b = (2 / n) * grad_b
    
    return grad_w, grad_b


def gradient_descent(
    X: List[float],
    y_true: List[float],
    learning_rate: float = 0.000001,
    epochs: int = 1000,
    initial_w: float = 0.0,
    initial_b: float = 0.0,
) -> Tuple[float, float, List[float]]:
    """
    梯度下降主函数
    
    参数:
        X: 输入特征（房屋面积）
        y_true: 真实标签（房价）
        learning_rate: 学习率（步长）
        epochs: 迭代轮数
        initial_w: w 初始值
        initial_b: b 初始值
    
    返回:
        (最终w, 最终b, 损失历史记录)
    """
    w = initial_w
    b = initial_b
    loss_history = []
    
    for epoch in range(epochs):
        # 1. 计算当前损失
        loss = compute_mse(X, y_true, w, b)
        loss_history.append(loss)
        
        # 2. 计算梯度
        grad_w, grad_b = compute_gradients(X, y_true, w, b)
        
        # 3. 更新参数（沿梯度反方向）
        w = w - learning_rate * grad_w
        b = b - learning_rate * grad_b
        
        # 每1000轮打印一次
        if (epoch + 1) % 1000 == 0:
            print(f"  Epoch {epoch+1:4d}/{epochs} | MSE: {loss:.4f} | w: {w:.6f} | b: {b:.4f}")
    
    return w, b, loss_history


def generate_house_data(n: int = 20, seed: int = 42) -> Tuple[List[float], List[float]]:
    """
    生成模拟房价数据
    真实关系: 房价 ≈ 3.5 * 面积 + 20 + 噪声
    
    参数:
        n: 数据样本数
        seed: 随机种子
    
    返回:
        (面积列表, 房价列表)
    """
    random.seed(seed)
    X = []
    y = []
    for _ in range(n):
        area = random.uniform(30, 200)        # 面积 30~200 平米
        price = 3.5 * area + 20 + random.gauss(0, 15)  # 加高斯噪声
        X.append(area)
        y.append(price)
    return X, y
