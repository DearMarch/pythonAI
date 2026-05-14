from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, wrap_model_call, \
    wrap_tool_call
from langchain_community.chat_models import ChatTongyi
from langchain_core.tools import tool
from langgraph.runtime import Runtime
import config_data as config


@tool(description="查询天气，传入城市名称字符串，返回字符串天气信息")
def get_weather(city:str) -> str:
    return f"{city}天气不错"


"""
agent执行前
agent执行后
model执行前
model执行后
工具执行中
模型执行中
"""

@before_agent
def log_before_agent(state: AgentState, runtime: Runtime) -> None:
    print(f"[before_agent]agent执行前,并附带{len(state['messages'])}消息")

@after_agent
def log_after_agent(state: AgentState, runtime: Runtime) -> None:
    print(f"[after_agent]agent执行结束,并附带{len(state['messages'])}消息")

@before_model
def log_before_model(state: AgentState, runtime: Runtime) -> None:
    print(f"[before_model]model执行前,并附带{len(state['messages'])}消息")

@after_model
def log_after_model(state: AgentState, runtime: Runtime) -> None:
    print(f"[after_model]model执行结束,并附带{len(state['messages'])}消息")


@wrap_model_call
def log_model_call(request, handler):
    print("模型调用啦")
    return handler(request)

@wrap_tool_call
def log_tool_call(request, handler):
    print(f"工具执行：{request.tool_call['name']}")
    print(f"工具参数：{request.tool_call['args']}")
    return handler(request)


agent = create_agent(
    model=ChatTongyi(model=config.chat_model_deepseek),
    tools=[get_weather],
    middleware=[log_before_agent, log_after_agent, log_before_model, log_after_model, log_model_call, log_tool_call]
)

res = agent.invoke(
    {
        "messages":[
            {
                "role": "user",
                "content": "明天郑州的天气如何， 如何穿衣？"
            }
        ]
    }
)

for message in res["messages"]:
    print(type(message).__name__, message.content)