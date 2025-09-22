from langchain_ollama import ChatOllama


llm  = ChatOllama(model="llama3:latest", temperature=0.5, base_url="http://host.docker.internal:11434")

