import os
import asyncio
from openai import AsyncOpenAI

async def process_file(client, file_id, index, prompt):
    print(f'正在处理第{index}个文件')
    completion = await client.chat.completions.create(
        model="qwen-long",
        messages=[
            {'role': 'system', 'content': f'fileid://{file_id}'},
            {'role': 'user', 'content': prompt}
        ],
        stream=True
    )
    
    with open(f'bank/题库{index}.md', 'w', encoding='utf-8') as f:
        async for chunk in completion:
            if chunk.choices and chunk.choices[0].delta.content:
                f.write(chunk.choices[0].delta.content)
    
    print(f'题库{index}.md 已生成')

async def main():
    client = AsyncOpenAI(
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("BASE_URL"),
    )
    
    files = await client.files.list()
    files_id = [file.id for file in files.data]
    print(files_id)
    
    prompt = """
    请根据文件内容，按照以下格式输出：
    1.以markdown格式仅输出文件内容
    2.不要包含```markdown```等标识符，不要包含它无关的任何内容，不要包含文件名
    3.判断每一个小题的类型，并在小题前面打上标签，如：
        - 如果是选择题：（选择题）
        - 如果是判断题：（判断题）
        - 如果是名词解释：（名词解释）
        - 如果是简答题：（简答题）
        - 如果是计算题：（计算题）
    4.每一道小题都要以"---"分割
    """
    
    tasks = []
    for index, file_id in enumerate(files_id, 1):
        task = asyncio.create_task(process_file(client, file_id, index, prompt))
        tasks.append(task)
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

