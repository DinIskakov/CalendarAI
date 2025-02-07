from langchain.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
import os, os.path
from dotenv import load_dotenv
load_dotenv()

from google_authenticator import initialize_service
from calendar_tools import init_calendar_service, get_time, get_events, set_event, delete_event

llm=ChatOpenAI(model="gpt-4o", temperature=0, api_key=os.getenv("OPENAI_API_KEY"))


def execute(user_input: str):

    tools = [
        get_time,
        get_events,
        set_event,
        delete_event
    ]

    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", 
            """
            You are a friendly and autonomous Google Calendar assistant who helps users manage their schedules effectively

            """
        ),
        ("placeholder", "{agent_scratchpad}"),
        ("user", user_input)
    ]
    )

    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    result = agent_executor.invoke({"input": user_input})
    #print(result.get("output"))
    return result


if __name__ == '__main__':
    service = initialize_service()
    init_calendar_service(service)

    while True:
        user_msg = input("You: ")
        if user_msg.lower() in ["stop", "exit", "quit"]:
            break

        response = execute(user_msg)
        print("Assistant:", response.get("output"))