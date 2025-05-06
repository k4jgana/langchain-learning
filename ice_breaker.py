from third_parties.reddit import get_top_post_title
from agents.news_lookup_agent import news_lookup_agent
from output_parsers import article_parser, Article

from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


def ice_break_with(article:str) -> str:
    news_url = news_lookup_agent(article)
    return news_url



if __name__=='__main__':
    load_dotenv()

    summary ="""
    write me a story about this url: {url} and 3 tags that it should be under
    \n{format_instructions} 
    """

    top_post_info = get_top_post_title('news')

    print(top_post_info)

    summ_prompt_temp = PromptTemplate(
        input_variables = ['url'], template = summary,
        partial_variables = {'format_instructions': article_parser.get_format_instructions()}
    )
    news_url = ice_break_with(top_post_info)

    print(news_url)

    llm = ChatOpenAI(model = "gpt-4o-mini")

    # chain = summ_prompt_temp | llm | StrOutputParser()
    chain = summ_prompt_temp | llm | article_parser

    res:Article = chain.invoke(input={'url':news_url})


    print(res.tags)