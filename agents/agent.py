from tools.all_tools import tools
from prompts.aoc_prompt_template import aoc_prompt_template
from langchain.agents import AgentExecutor, create_react_agent


class ChallengeAgent:
    '''This agent will return the answer to a particular AoC Challenge'''

    def __init__(self, llm):
        self.llm = llm

    def __call__(self, query):

        # Create the ReAct agent using the create_react_agent function
        agent = create_react_agent(
            llm=self.llm,
            tools=tools,
            prompt=aoc_prompt_template,
            stop_sequence=True,
        )

        # Create an agent executor from the agent and tools
        agent_executor = AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=tools,
            verbose=False,
        )

        response = agent_executor.invoke({"input": query})
        return response['output']
