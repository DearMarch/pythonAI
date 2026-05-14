from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool

import config_data as config

@tool(description="查询天气")
def get_weather() -> str:
    return "今天天气不错"

agent = create_agent(
    model=ChatTongyi(model=config.chat_model_deepseek),
    tools=[get_weather],
    system_prompt="你是一个聊天助手，可以回答用户问题。"
)

res = agent.invoke(
    {
        "messages":[
            {
                "role": "user",
                "content": "明天郑州的天气如何？"
            }
        ]
    }
)

for message in res["messages"]:
    print(type(message).__name__, message.content)