
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
response_schemas = [
        ResponseSchema(name="title", description="A catchy title for the post idea."),
        ResponseSchema(name="key_points", description="Key points to cover in the post."),
        ResponseSchema(name="visual_elements", description="Suggested visual elements."),
    ]
post_generate_schema_parser = StructuredOutputParser.from_response_schemas(response_schemas)