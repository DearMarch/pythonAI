from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool

import config_data as config

@tool(description="查询股票的价格，传入股票名称，返回字符串信息")
def get_price(name: str) -> str:
    return f"股票{name}的价格是20元"

@tool(description="查询股票信息，传入股票名称，返回字符串信息")
def get_info(name: str) -> str:
    return f"股票{name}是一家A股上市公司，专注于IT行业"

agent = create_agent(
    model=ChatTongyi(model=config.chat_model_deepseek),
    tools=[get_price,get_info],
    system_prompt="你是一个智能助手，请回答股票相关问题，记住请告知我思考过程，告诉我为什么调用某个工具。"
)

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "小米股价多少，并介绍一下"}]},
    stream_mode="values"
):
    latest_message = chunk["messages"][-1]
    print(latest_message)
    #print("="*10)
    if latest_message.content:
        print(type(latest_message).__name__, latest_message.content)

    try:
        if latest_message.tool_calls:
            print(f"工具调用：{[tc['name'] for tc in latest_message.tool_calls]}")
    except AttributeError:
        pass
