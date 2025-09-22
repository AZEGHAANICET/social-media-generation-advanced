from langchain_ollama import ChatOllama
from typing import Dict, Any, List
from langchain_core.output_parsers import ListOutputParser
from langchain.output_parsers import ResponseSchema, CommaSeparatedListOutputParser, StructuredOutputParser
from  ..utils.llm import llm
from app.utils.prompts import post_prompt, hashtags_prompt, caption_prompt
import json
from ..utils.parsers import post_generate_schema_parser


class ContentGenerator:
    def __init__(self, model="llama3:latest"):
        self.llm = llm

    async def generate_caption(self, prompt:str, platform:str, tone:str, max_length:int=200)->Dict[str, Any]:
        system_prompt = caption_prompt(platform, tone, max_length)

        messages = [
            ("system", system_prompt),
            ("user", prompt)
        ]

        result  =  self.llm.invoke(messages)

        response = result.content

        return {
            "content": response
        }

    async def generate_hashtags(self, content:str, platform:str, count:int=10)-> List[str]:
        user_prompt = hashtags_prompt(count=count, content=content, platform=platform)
        messages = [("user", user_prompt)]
        result =   self.llm.invoke(messages)

        list_parsers = CommaSeparatedListOutputParser()
        hastags = list_parsers.parse(result.content)

        return hastags

    async def generate_post_idea(self, topic:str, platform:str, count:int=5)-> List[Dict[str, Any]]:

        user_prompt = post_prompt(count, topic, platform)


        messages = [("user", user_prompt)]

        response =  self.llm.invoke(messages)
        ideas = json.loads(response.content)
        print(ideas)

        return ideas




