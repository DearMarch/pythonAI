from openai import OpenAI

# 1. 获取client对象，openai 类对象
client = OpenAI (
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2. 调用模型
response = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=[
        {"role": "system", "content": "你是一个AI助理，回答很简洁"},
        {"role": "user", "content": "小明有三只小猴"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有三只小猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "一共有多少只宠物？"},
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