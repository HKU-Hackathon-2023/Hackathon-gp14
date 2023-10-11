import os
os.environ["OPENAI_API_KEY"] = "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"
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

def GenSubtopics():

    class CommaSeparatedListOutputParser(BaseOutputParser):
        """Parse the output of an LLM call to a comma-separated list."""


        def parse(self, text: str):
            """Parse the output of an LLM call."""
            return text.strip().split(", ")

    chat_model = ChatOpenAI(temperature=0.9)
    template =  """You are a helpful assistant who generates comma separated lists.
                A user will pass in a category, and you should generate 4 subtopics under a 4-week course of that category in a comma separated list.
                ONLY return a comma separated list, and nothing more."""

    human_template="{text}"

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", human_template),
    ])

    chain = chat_prompt | ChatOpenAI() | CommaSeparatedListOutputParser()
    subtopics = chain.invoke({"text": "I want to learn data structures"})
    return subtopics

