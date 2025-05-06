from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.prompts import PromptTemplate
from langchain.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()
react_prompt = hub.pull('hwchase17/react')


@tool
def triple(num:float)->float:
    """
    :param num: a number to triple
    :return: the number tripled -> multiplied by 3
    """

    return float(num)*3


tools = [TavilySearchResults(max_results = 1), triple]
llm = ChatOpenAI(temperature=0,model="gpt-4o-mini")
react_agent_runnable = create_react_agent(llm, tools, react_prompt)
