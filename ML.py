import os
import sys
from pathlib import Path

# 定义项目结构
project_structure = {
    "data": {
        "raw": [],
        "processed": [],
        "interim": []
    },
    "models": {
        "trained": [],
        "archs": []
    },
    "src": {
        "data": ["loaders.py", "preprocess.py", "augment.py"],
        "models": ["base.py", "nn_models.py", "ml_models.py"],
        "trainers": ["base_trainer.py", "classifier.py"],
        "utils": ["metrics.py", "visualizer.py", "logger.py"],
        "configs": ["default.yaml", "experiment1.yaml"]
    },
    "notebooks": {
        "exploratory": [],
        "models": []
    },
    "tests": ["test_data.py", "test_models.py"],
    "scripts": ["train.py", "predict.py", "preprocess.py"]
}

# 定义根目录下的文件
root_files = ["requirements.txt", "README.md"]

def create_project_structure(project_path="my_ml_project"):
    """创建机器学习项目的目录结构"""
    # 转换为绝对路径
    project_path = Path(project_path).resolve()
    
    # 检查项目目录是否已存在
    if project_path.exists():
        print(f"警告: 目录 '{project_path}' 已存在")
        overwrite = input("是否继续并覆盖现有文件? (y/N): ").strip().lower()
        if overwrite != 'y':
            print("操作已取消")
            return False
    
    try:
        # 创建项目根目录
        project_path.mkdir(parents=True, exist_ok=True)
        print(f"创建目录: {project_path}")
        
        # 创建目录结构
        for dir_name, content in project_structure.items():
            dir_path = project_path / dir_name
            dir_path.mkdir(exist_ok=True)
            print(f"创建目录: {dir_path}")
            
            # 处理子目录
            if isinstance(content, dict):
                for sub_dir, files in content.items():
                    sub_dir_path = dir_path / sub_dir
                    sub_dir_path.mkdir(exist_ok=True)
                    print(f"创建目录: {sub_dir_path}")
                    
                    # 创建子目录中的文件
                    for file_name in files:
                        file_path = sub_dir_path / file_name
                        create_file(file_path)
            
            # 处理当前目录中的文件
            elif isinstance(content, list):
                for file_name in content:
                    file_path = dir_path / file_name
                    create_file(file_path)
        
        # 创建根目录下的文件
        for file_name in root_files:
            file_path = project_path / file_name
            create_file(file_path)
        
        print(f"\n项目结构已成功创建于: {project_path}")
        return True
        
    except Exception as e:
        print(f"错误: 创建项目结构时发生异常: {e}")
        return False

def create_file(file_path):
    """创建文件并添加简单的模板内容"""
    # 如果文件不存在或允许覆盖，则创建文件
    if not file_path.exists():
        try:
            # 根据文件扩展名添加不同的模板内容
            file_path.touch()
            print(f"创建文件: {file_path}")
            
            # 为Python文件添加编码声明
            if file_path.suffix == '.py':
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write("# -*- coding: utf-8 -*-\n\n")
                    # 为入口脚本添加主函数
                    if file_path.parent.name == "scripts":
                        f.write("if __name__ == '__main__':\n    pass\n")
            
            # 为YAML配置文件添加简单结构
            elif file_path.suffix == '.yaml':
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write("# 配置文件\n")
            
            # 为README添加项目说明
            elif file_path.name == "README.md":
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write("# 机器学习项目\n\n")
                    f.write("## 项目结构\n\n")
                    f.write("此项目遵循标准的机器学习项目布局:\n\n")
                    f.write("- `data/`: 数据存储\n")
                    f.write("- `models/`: 模型存储\n")
                    f.write("- `src/`: 源代码\n")
                    f.write("- `notebooks/`: Jupyter笔记本\n")
                    f.write("- `tests/`: 单元测试\n")
                    f.write("- `scripts/`: 可执行脚本\n\n")
                    f.write("## 使用说明\n\n")
                    f.write("1. 安装依赖:\n")
                    f.write("   ```bash\n")
                    f.write("   pip install -r requirements.txt\n")
                    f.write("   ```\n\n")
                    f.write("2. 运行训练脚本:\n")
                    f.write("   ```bash\n")
                    f.write("   python scripts/train.py\n")
                    f.write("   ```\n")
            
            # 为requirements.txt添加基本依赖
            elif file_path.name == "requirements.txt":
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write("# 项目依赖\n")
                    f.write("numpy>=1.21\n")
                    f.write("pandas>=1.3\n")
                    f.write("scikit-learn>=1.0\n")
                    f.write("matplotlib>=3.4\n")
                    f.write("seaborn>=0.11\n")
                    f.write("tensorflow>=2.6  # 如果使用深度学习\n")
                    f.write("torch>=1.9  # 如果使用PyTorch\n")
            
        except Exception as e:
            print(f"警告: 创建文件 {file_path} 失败: {e}")
    else:
        print(f"跳过已存在的文件: {file_path}")

if __name__ == "__main__":
    # 默认项目路径为当前目录下的my_ml_project
    project_path = "my_ml_project"
    
    # 如果提供了命令行参数，则使用该路径
    if len(sys.argv) > 1:
        project_path = sys.argv[1]
    
    create_project_structure(project_path)


    