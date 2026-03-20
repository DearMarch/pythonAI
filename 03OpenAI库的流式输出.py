from openai import OpenAI

# 1. 获取client对象，openai 类对象
client = OpenAI (
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2. 调用模型
response = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=[
        {"role": "system", "content": "你是一个Python专家，并且不说废话 简单回答"},
        {"role": "assistant", "content": "好的，我是一个编程专家，并且话不多，你要问什么？"},
        {"role": "user", "content": "输出1-10的数字，使用Python实现"}
    ],
    stream=True # 启用流式输出
)

# 3.处理结果
#print(response.choices[0].message.content)
for chunk in response:
    print(chunk.choices[0].delta.content,
          end=" ", # 每一段之间以空格隔开
          flush=True # 立刻刷新缓冲区
          )