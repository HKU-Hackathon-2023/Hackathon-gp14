import Student
from langchain.schema import SystemMessage, AIMessage, HumanMessage
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate


    
def get_estimated_weeks_format_instructions(student: Student, subject: str) -> list:
    
    prompt = f"""You are a teacher specifying in teacher deaf student. Your student showed interest in learning {subject}. You are now thinking how many weeks would be sufficient and approciate for the student to understand {subject}. Your output must be and can only be an integer.

    First, you should understand the student education level delimited by triple !. 
    Then, you should fully understand his/her education need delimited by double quotatio mark. 
    Then, decide the number of weeks that would be sufficient and approciate for the student to understand base on education level and Special education need

    Subject: {subject}
    Education level: !!!{student.education_level}!!!
    Special Education need: ""{student.special_education_need}""

    Output following the below scheme:
    int
    """

    return [SystemMessage(content="You are a teacher specifying in teacher deaf student. You are now thinking how many weeks would be sufficient and approciate for the student to understand an subject. Your output must be and can only be an integer."),
            HumanMessage(content=prompt)]

def get_weekly_topics_format_instructions(student: Student, subject: str, estimated_weeks: int) -> int:
    output_parser = CommaSeparatedListOutputParser().get_format_instructions()

    prompt = f"""You are a teacher specifying in teacher deaf student. Your student showed interest in learning {subject}. You are now designing the topic to teach each week for the student in a {estimated_weeks} course on {subject}. 

        First, you should understand the student education level delimited by triple !. 
        Then, you should fully understand his/her education need delimited by double quotatio mark. 
        Then, decide the topic for each week that would be sufficient and approciate for the student to understand the subject base on education level and Special education need

        Subject: {subject}
        Estimated weeks: {estimated_weeks}
        Education level: !!!{student.education_level}!!!
        Special Education need: ""{student.special_education_need}

        You must only output the topic name in a comma seperated way. You must follow the output form i.e. str, str, str without week number. Just the name"""


    return [SystemMessage(content="You are a teacher specifying in teacher deaf student. Your output should only contain the topic name without any other things"),
            HumanMessage(content=prompt)]

def get_topic_checklist_instructions(student: Student, subject: str, topic: str, topic_list) -> int:
    prompt = f"""You are a teacher specifying in teacher deaf student. Your student showed interest in learning {subject}. You are now thinking what key concepts should the student understand for {topic} in {subject}.
    Those key concepts must not overlap with the topics that would be covered later in the course. The topic covered in the list is delimited triple "

    Topic List = {topic_list}

    You must only output the key concepts in a comma seperated way. You must follow the output form i.e. str, str, str without any other things possible. Just the name""
    """

    return [HumanMessage(content = prompt)]