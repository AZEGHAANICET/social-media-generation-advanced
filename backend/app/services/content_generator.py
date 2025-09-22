from langchain_ollama import ChatOllama
from typing import Dict, Any, List
from langchain_core.output_parsers import ListOutputParser
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from  ..utils.llm import llm
from backend.app.utils.prompts import post_prompt, hashtags_prompt, caption_prompt


class ContentGenerator:
    def __init__(self, model="llama3:latest"):
        self.llm = llm

    async def generate_caption(self, prompt:str, platform:str, tone:str, max_length:int=200)->Dict[str, Any]:
        system_prompt = caption_prompt(platform, tone, max_length)

        messages = [
            ("system", system_prompt),
            ("user", prompt)
        ]

        result  = await self.llm.invoke(messages)

        response = result.content

        return {
            "content": response
        }

    async def generate_hashtags(self, content:str, platform:str, count:int=10)-> List[str]:
        user_prompt = hashtags_prompt(count=count, content=content, platform=platform)
        messages = [("user", user_prompt)]
        result = await  self.llm.invoke(messages)

        list_parsers = ListOutputParser()
        hastags = list_parsers.parse(result.content)

        return hastags

    async def generate_post_idea(self, topic:str, platform:str, count:int=5)-> List[Dict[str, Any]]:

        response_schemas = [
            ResponseSchema(name="title" , description="A catchy title for the post idea."),
            ResponseSchema(name="key_points", description="Key points to cover in the post."),
            ResponseSchema(name="visual_elements", description="Suggested visual elements."),
        ]
        user_prompt = post_prompt(count, topic, platform)
        parser = StructuredOutputParser.from_response_schemas(response_schemas)

        messages = [("user", user_prompt)]

        response = await self.llm.invoke(messages)

        parsed_output = parser.parse(response.content)

        ideas = parsed_output if isinstance(parsed_output, list) else [parsed_output]
        return ideas




