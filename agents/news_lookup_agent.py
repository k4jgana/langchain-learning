import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain import hub

from tools.tools import get_news_article_url



def news_lookup_agent(article: str) -> str:
    llm = ChatOpenAI(temperature=0,model="gpt-4o-mini")
    template = """
        Given the article {article}, please give me one url of a news article connected with that.
        Your answer should only return URL
    """

    prompt_template = PromptTemplate(template=template, input_variables = ['article'])

    tools_for_agent = [
        Tool(
            name = 'crawl Google 4 news article',
            func=get_news_article_url,
            description='useful to find url of given news article'
        )
    ]

    react_prompt = hub.pull('hwchase17/react')
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent = agent,tools= tools_for_agent, verbose=True)
    res = agent_executor.invoke(
        input = {"input":prompt_template.format_prompt(article = article)}
    )

    return res['output']


if __name__=='__main__':
    res = news_lookup_agent("united_airlines_cuts_35_daily_flights_at_newark")
    print(res)

