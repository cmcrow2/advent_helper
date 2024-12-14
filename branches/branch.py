from langchain.schema.runnable import RunnableBranch
from langchain.schema.output_parser import StrOutputParser
from agents.agent import ChallengeAgent
from prompts.aoc_prompt_template import aoc_prompt_template
from prompts.answer_other import answer_other_template


def define_branches(llm):
    # define challenge agent
    challenge_agent = ChallengeAgent(llm, aoc_prompt_template)

    # define the runnable branches for handling feedback
    branches = RunnableBranch(
        (
            lambda x: "solution" in x,
            challenge_agent | StrOutputParser()
        ),
        answer_other_template | llm | StrOutputParser()
    )

    return branches
