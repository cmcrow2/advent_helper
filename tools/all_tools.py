from langchain.tools import Tool
from tools.tool_functions.day_01 import location_ids, similarity_score

tools = [
    Tool(
        name="Location Id's",
        func=location_ids,
        description="Solution for Day One, Part One."
    ),
    Tool(
        name="Similarity Score",
        func=similarity_score,
        description="Solution for Day One, Part Two."
    )
]
