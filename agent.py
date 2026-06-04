from langchain.agents import create_agent
from schema import AnalysisResult
from langchain.agents.structured_output import ToolStrategy
from constants import modelName, systemPrompt
from dotenv import load_dotenv
from langchain.messages import HumanMessage,SystemMessage
load_dotenv()

agent = create_agent(
    model= modelName,
    response_format=ToolStrategy(AnalysisResult)
)

query = input("Provide content to get summary and key_entities: ")
conversation = {
        "messages": [
            SystemMessage(content=systemPrompt),
            HumanMessage(content=query)
        ]
    }
result = agent.invoke(conversation)
response = result["structured_response"]
print(response.model_dump_json(indent=4))