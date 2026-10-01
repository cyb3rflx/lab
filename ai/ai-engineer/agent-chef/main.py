from langchain.agents import create_agent
from langchain.tools import tool
from typing import Dict, Any
from langchain.messages import HumanMessage, SystemMessage
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
tavily_client = TavilyClient()

@tool
def web_search(query: str) -> Dict[str, Any]:
    """Search the web for information"""

    return tavily_client.search(query)

agent = create_agent(
    "openai:gpt-5", 
    tools=[web_search],
    system_prompt=SystemMessage("Du bist ein Chef Koch und suchst mir passende Rezepte die ich mit den Zutaten die ich dir gebe zubereiten kann. Diese Rezepte müssen mit genau diesen Zutaten zubereitet werden können und benötige keine weiteren Zutaten. Du lieferst mir maximal 3 passende Rezepte. Nutze das web_search tool um nach passenden Rezepten zu suchen")  
)


def main():
    print("Hello from agent-chef!")
    ingredients = input("Welche Zutaten hast du zur Verfügung?: ")

    message = [
        HumanMessage(f"Hier sind alle Zutaten die ich zur Verfügung habe: {ingredients}")
    ]

    response = agent.invoke(
        {"messages": message}
    )

    print(response["messages"][-1].content)


if __name__ == "__main__":
    main()
