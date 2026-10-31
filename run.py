"""
一键运行脚本 - 在 club 根目录直接运行任意项目

用法:
    python run.py            # 列出所有项目
    python run.py sa         # 运行模拟退火
    python run.py gd         # 运行梯度下降
    python run.py all        # 依次运行全部
"""

import subprocess
import sys
import os

PROJECTS = {
    "sa": {
        "name": "模拟退火算法 - 快递配送路线规划 (TSP)",
        "path": "simulated_annealing",
        "entry": "main.py",
    },
    "gd": {
        "name": "梯度下降 - 线性回归预测房价",
        "path": "gradient_descent",
        "entry": "main.py",
    },
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def run_project(key: str) -> int:
    """运行指定项目"""
    proj = PROJECTS[key]
    work_dir = os.path.join(BASE_DIR, proj["path"])
    entry = os.path.join(work_dir, proj["entry"])

    print("=" * 60)
    print(f"  运行: {proj['name']}")
    print(f"  路径: {work_dir}")
    print("=" * 60)

    # 使用当前 Python 解释器运行子项目
    result = subprocess.run([sys.executable, entry], cwd=work_dir)
    return result.returncode


def list_projects():
    """列出所有可用项目"""
    print("=" * 60)
    print("  可用项目")
    print("=" * 60)
    for key, proj in PROJECTS.items():
        print(f"  {key:4s}  {proj['name']}")
        print(f"        -> {proj['path']}/{proj['entry']}")
    print()
    print("  用法:")
    print("    python run.py sa      # 运行模拟退火")
    print("    python run.py gd      # 运行梯度下降")
    print("    python run.py all     # 运行全部")
    print("=" * 60)


def main():
    if len(sys.argv) < 2:
        list_projects()
        return

    arg = sys.argv[1].lower()

    if arg == "all":
        for key in PROJECTS:
            run_project(key)
            print()
        return

    if arg in PROJECTS:
        run_project(arg)
        return

    print(f"[错误] 未知项目: {arg}")
    print("可用项目: sa, gd, all")
    list_projects()


if __name__ == "__main__":
    main()
