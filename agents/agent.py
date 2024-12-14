from tools.all_tools import tools
from langchain.agents import AgentExecutor, create_react_agent


class ChallengeAgent:
    '''This agent will return the answer to a particular AoC Challenge'''

    def __init__(self, llm, template):
        self.llm = llm
        self.template = template

    def __call__(self, query):

        # create the ReAct agent using the create_react_agent function
        agent = create_react_agent(
            llm=self.llm,
            tools=tools,
            prompt=self.template,
            stop_sequence=True,
        )

        # create an agent executor from the agent and tools
        agent_executor = AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=tools,
            verbose=False,
        )

        response = agent_executor.invoke({"input": query})
        return response['output']
