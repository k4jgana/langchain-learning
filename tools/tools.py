from langchain_community.tools.tavily_search import TavilySearchResults

def get_news_article_url(article:str):
    search = TavilySearchResults()
    res = search.run(f'{article}')
    return res