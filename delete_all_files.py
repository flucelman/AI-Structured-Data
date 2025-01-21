import os
import asyncio
from openai import AsyncOpenAI

async def delete_file(client, file):
    try:
        await client.files.delete(file.id)
        print(f"成功删除文件: {file.filename} (ID: {file.id})")
    except Exception as e:
        print(f"删除文件 {file.filename} 时出错: {str(e)}")

async def delete_all_files():
    client = AsyncOpenAI(
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("BASE_URL"),
    )
    # 获取文件列表
    files = await client.files.list()
    
    # 创建所有删除任务
    tasks = [delete_file(client, file) for file in files.data]
    
    # 并发执行所有删除任务
    await asyncio.gather(*tasks)

# 运行异步函数
if __name__ == "__main__":
    asyncio.run(delete_all_files())