from langchain.prompts import ChatPromptTemplate

answer_other_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert on the 2024 edition of Advent of Code."),
        (
            "human",
            "Answer the user's question as best as you can.\n"
            "If the user asks a question related to the Advent of Code, do you best to answer.\n"
            "If the user asks a question not related to the Advent of Code, politely decline to answer.\n\n"
            "Here is the question you need to answer: {input}"
        ),
    ]
)
