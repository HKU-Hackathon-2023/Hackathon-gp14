from langchain.schema import SystemMessage, AIMessage, HumanMessage
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from typing import List

from langchain.llms import OpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.pydantic_v1 import BaseModel, Field, validator

def get_weekly_topics_format_instructions(student_education_level, student_special_education_need , subject: str) -> int:
    output_parser = CommaSeparatedListOutputParser().get_format_instructions()

    prompt = f"""You are a teacher specifying in teacher deaf student. Your student showed interest in learning {subject}. You are now designing the topic to teach each week for the student in a course on {subject}. 

    First, you should understand the student education level delimited by triple !. 
    Then, you should fully understand his/her education need delimited by double quotatio mark. 
    Then, decide the topic for each week that would be sufficient and approciate for the student to understand the subject base on education level and Special education need

    Subject: {subject}
    Education level: !!!{student_education_level}!!!
    Special Education need: ""{student_special_education_need}

    You must only output the topic name in a comma seperated way. You must follow the output form i.e. str, str, str without week number. Just the name"""


    return [SystemMessage(content="You are a teacher specifying in teacher deaf student. Your output should only contain the topic name without any other things"), HumanMessage(content=prompt)]

def get_topic_checklist_instructions(topic: str) -> int:

    my_list = ['Introduction to Data Structure', ' Arrays', ' Linked Lists', ' Stacks', ' Queues', ' Trees', ' Graphs', ' Sorting Algorithms', ' Searching Algorithms'] 
    item_to_exclude = topic

    result = ', '.join([item for item in my_list if item != item_to_exclude])
    prompt = f"""Your student is an extreme beginner. If you are asked to make a teaching plan on {topic}, as the topic of week 1 of the course. What are the items would you teach in this two hour? 
    
    Don't not overlap with other week topics: {result}

    You must output your response item by item seperate by comma. Each item should be just 30 word long description with how deep it should be or it is just an introduction. 
    
    """ 

    return [SystemMessage(content="Output your response item by item seperate by comma."), HumanMessage(content=prompt)]


def get_teaching_instruction(student_special_education_need, teaching_instruction: str):
    system_prompt = f"""You are now teaching a student with {student_special_education_need}
    
    Follow this teaching schedule, {teaching_instruction} to teach. You should teach one item by one item.

    Determine the progress by reading the chat history.

    Response as if you are really teaching the student. Ask whether the student can understand after each output
    """

    return SystemMessage(content = system_prompt)

def get_speech_convertion_system_instruction(student_education_level: str, student_special_education_need: str):
    prompt = f"""You are a personal assistant of a deaf student. You are helping him/ her to convert what a teacher said into a level that can be understand by a {student_education_level} student.
    Note that he/she also has {student_special_education_need}.

    Understand what was said by the teacher and the history to output your response.
    """

    return [SystemMessage(content = prompt)]