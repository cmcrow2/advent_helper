from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from prompts.aoc_prompt_template import aoc_prompt_template
from agents.agent import ChallengeAgent

# load environment variables from .env file
load_dotenv()

# initialize a ChatOpenAI model
llm = ChatOpenAI(
    model="gpt-4o", temperature=0
)

# create our custom agent
challenge_agent = ChallengeAgent(llm, aoc_prompt_template)

# create the chain
chain = challenge_agent | StrOutputParser()

# chat loop
while True:
    # get user input
    query = input("You: ")
    if query.lower() == "exit":
        break

    # pass the query directly to the agent
    try:
        response = chain.invoke({"input": query})
        print(f"AI: {response}")

    except Exception as e:
        print(f"Error: {e}")
