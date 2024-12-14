from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from prompts.aoc_prompt_template import aoc_prompt_template
from agents.agent import ChallengeAgent
from branches.branch import define_branches
from prompts.classification import classification_template

# debugging tools
# from langchain.globals import set_debug, set_verbose
# set_debug(True)
# set_verbose(True)

# load environment variables from .env file
load_dotenv()

# initialize a ChatOpenAI model
llm = ChatOpenAI(
    model="gpt-4o", temperature=0
)

# initialize branches
branches = define_branches(llm)

# create classification chain
classification_chain = classification_template | llm | StrOutputParser()

# create our chain
chain = classification_chain | branches

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
