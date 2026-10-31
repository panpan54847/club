"""
梯度下降 - 线性回归预测房价
主程序入口

运行方式: python main.py
"""

from gradient import (
    generate_house_data,
    compute_mse,
    gradient_descent,
    predict,
)
from visualize import try_plot


def main():
    print("=" * 50)
    print("  梯度下降 - 线性回归预测房价")
    print("=" * 50)

    # 1. 生成模拟房价数据
    print("\n[1] 生成模拟房价数据...")
    X, y_true = generate_house_data(n=20, seed=42)
    print(f"    样本数: {len(X)}")
    print(f"    面积范围: {min(X):.1f} ~ {max(X):.1f} 平米")
    print(f"    房价范围: {min(y_true):.1f} ~ {max(y_true):.1f} 万元")
    print(f"\n    数据明细:")
    print(f"    {'面积(平米)':>12}  {'房价(万元)':>10}  {'预测(万元)':>10}")
    print(f"    {'-'*12}  {'-'*10}  {'-'*10}")
    for i in range(len(X)):
        print(f"    {X[i]:>12.1f}  {y_true[i]:>10.1f}")

    # 2. 初始化参数
    print(f"\n[2] 初始化参数:")
    print(f"    w = 0.0 (斜率)")
    print(f"    b = 0.0 (截距)")
    print(f"    学习率 lr = 0.000001")
    print(f"    迭代轮数 epochs = 10000")

    initial_mse = compute_mse(X, y_true, w=0.0, b=0.0)
    print(f"    初始 MSE: {initial_mse:.2f}")

    # 3. 运行梯度下降
    print(f"\n[3] 开始梯度下降训练...")
    w, b, loss_history = gradient_descent(
        X=X,
        y_true=y_true,
        learning_rate=0.000001,
        epochs=10000,
        initial_w=0.0,
        initial_b=0.0,
    )

    # 4. 输出结果
    final_mse = compute_mse(X, y_true, w, b)
    print(f"\n[4] 训练完成！")
    print(f"    最终参数: w = {w:.4f}, b = {b:.4f}")
    print(f"    模型公式: y = {w:.4f}x + {b:.4f}")
    print(f"    最终 MSE: {final_mse:.2f}")
    print(f"    初始 MSE: {initial_mse:.2f}")
    print(f"    下降幅度: {(1 - final_mse/initial_mse)*100:.1f}%")

    # 5. 预测示例
    print(f"\n[5] 预测示例:")
    test_areas = [50, 80, 100, 150]
    print(f"    {'面积(平米)':>12}  {'预测房价(万元)':>14}")
    print(f"    {'-'*12}  {'-'*14}")
    for area in test_areas:
        price = predict(area, w, b)
        print(f"    {area:>12}  {price:>14.1f}")

    # 6. 可视化
    print(f"\n[6] 生成可视化...")
    try_plot(X, y_true, w, b, loss_history)

    print("\n完成！")


if __name__ == "__main__":
    main()
