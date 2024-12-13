from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from prompts.aoc_prompt_template import aoc_prompt_template
from tools.all_tools import tools

# Load environment variables from .env file
load_dotenv()

# Initialize a ChatOpenAI model
llm = ChatOpenAI(
    model="gpt-4o", temperature=0
)

# Dynamically create tool names
tool_names_list = ", ".join([tool.name for tool in tools])

# Create the ReAct agent using the create_react_agent function
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=aoc_prompt_template,
    stop_sequence=True,
)

# Create an agent executor from the agent and tools
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

# Chat loop
while True:
    # Get user input
    query = input("You: ")
    if query.lower() == "exit":
        break

    # Pass the query directly to the agent
    try:
        response = agent_executor.invoke({"input": query})
        print(f"AI: {response['output']}")

    except Exception as e:
        print(f"Error: {e}")
