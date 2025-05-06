from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Article(BaseModel):
    description:str = Field(description='description')
    tags : List[str] = Field(description='tags for news article')

    def to_dict(self)->Dict[str, Any]:
        return {"description": self.description, "tags":self.tags}


article_parser = PydanticOutputParser(pydantic_object = Article)