import os
import asyncio
from pathlib import Path
from openai import AsyncOpenAI

async def upload_single_file(client, file_path):
    try:
        await client.files.create(file=file_path, purpose="file-extract")
        print(f"成功上传文件 {file_path.name}")
    except Exception as e:
        print(f"上传文件 {file_path.name} 时发生错误: {str(e)}")

async def upload_files(folder_path):
    client = AsyncOpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("BASE_URL"),
    )
    
    # 将输入路径转换为 Path 对象
    folder = Path(folder_path)
    
    # 确保路径存在且是文件夹
    if not folder.is_dir():
        raise ValueError(f"提供的路径 '{folder_path}' 不是一个有效的文件夹")
    
    # 创建上传任务列表
    tasks = []
    for file_path in folder.glob('*'):
        if file_path.is_file():  # 只处理文件，跳过子文件夹
            tasks.append(upload_single_file(client, file_path))
    
    # 并发执行所有上传任务
    await asyncio.gather(*tasks)

# 运行异步函数的包装器
def run_upload_files(folder_path):
    asyncio.run(upload_files(folder_path))

if __name__ == "__main__":
    files_path = os.path.join(os.getcwd(), "Files")
    asyncio.run(upload_files(files_path))

