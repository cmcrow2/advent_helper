from langchain.prompts import ChatPromptTemplate

classification_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert on the 2024 edition of Advent of Code."),
        (
            "human",
            "If the user asks a question about a solution to a particular day and part,  classify the question as \"solution\".\n"
            "If the user asks a question about a prompt or problem for a particular day or part, classify the question as \"prompt\"\n"
            "If the user asks a question about any other topic, classify the question as \"other\".\n\n"
            "Here is the question you need to classify: {question}"
        ),
    ]
)
