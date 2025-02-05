from langchain.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
import os, os.path
from dotenv import load_dotenv
load_dotenv()


from langchain.tools import tool
from datetime import datetime
from typing import List


llm=ChatOpenAI(model="gpt-4o", temperature=0, api_key=os.getenv("OPENAI_API_KEY"))

@tool
def get_time(input: str = None) -> List[str]:
    """Returns the current day of the week and thecurrent date, useful tool to get anything time related
    First elemenet is the current day of the week and the second element is the current date and time
    Use this tool to calculate the from_where parameter for get_events tool and find out the date or day of the week"""

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    day_of_week = datetime.now().strftime("%A")  # Get the full weekday name
    return [day_of_week, current_time]

def execute(user_input: str):

    tools = [
        get_time
    ]

    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", 
            """
            You are a funny and friendly Google Calendar assistant who helps users manage their schedules effectively and can engage in a conversation. 

            """
            
        ),
        ("placeholder", "{agent_scratchpad}"),
        ("user", user_input)
    ]
    )



    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)



    result = agent_executor.invoke({"input": user_input})
    print(result.get("output"))



if __name__ == '__main__':
    while(True):
        user_input = input("What can i get for you?: ")
        if user_input.lower() == "stop": break
        execute(user_input)
