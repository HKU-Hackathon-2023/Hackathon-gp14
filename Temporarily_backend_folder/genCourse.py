import os
os.environ["OPENAI_API_KEY"] = "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"
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

def GenSubtopics(topic):

    class CommaSeparatedListOutputParser(BaseOutputParser):
        """Parse the output of an LLM call to a comma-separated list."""


        def parse(self, text: str):
            """Parse the output of an LLM call."""
            return text.strip().split(", ")

    ChatOpenAI(temperature=0.9)
    template =  """You are a helpful assistant who generates comma separated lists.
                A user will pass in a category, and you should generate 4 subtopics under a 4-week course of that category in a comma separated list.
                ONLY return a comma separated list, and nothing more."""

    human_template="{text}"

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", human_template),
    ])

    chain = chat_prompt | ChatOpenAI() | CommaSeparatedListOutputParser()
    subtopics = chain.invoke({"text": f"I want to learn {topic}"})
    return subtopics


def genContents(topics):

    ChatOpenAI(temperature=0.9)
    template = '''You are a virtual teaching assistant designed to support deaf students in understanding teacher's speech.
                You should engage with them,  provide deaf individuals learning resources that align with their interests and personal
                development goals. The student will pass in an interested topic , and you should teach him the topics.
                explain each part as clear as you can. Please answer the question in an objective but easy way.'''

    human_template="{text}"

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", human_template),
    ])
    llm = ChatOpenAI()
    introduction = llm(chat_prompt.format_messages(text=f"Simple introduction of {topics} within 100 words."))
    explanation = llm(chat_prompt.format_messages(text=f"Explain {topics} as clear as you can, at least 500 words."))
    examples = llm(chat_prompt.format_messages(text=f"Provide 3 examples of {topics} and explain the examples clearly, step by step"))

    return introduction.content, explanation.content, examples.content



