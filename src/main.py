from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import OpenAI
from tools import get_tools
from config import openai_api_key  # <-- import from config.py

openai_llm = OpenAI(openai_api_key=openai_api_key, temperature=0)
tools = get_tools(openai_api_key)

agent = initialize_agent(
    tools=tools,
    llm=openai_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    agent.run("read the my testing case requirements test_data_1_requirement.txt and generate test cases, save them to tests/test_ui.py, and run the test cases.but dont send email ")
