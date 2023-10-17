import os
from dotenv import load_dotenv
load_dotenv()
from langchain.schema import SystemMessage, AIMessage, HumanMessage
import Student
import prompt
from langchain.chat_models import ChatOpenAI
from langchain.llms import AzureOpenAI
import openai
import time

class Course:
    
    def __init__(self, subject) -> None:
        self.subject = subject
        self.course_name: str 
        self.estimated_weeks: int 
        self.topic_list: list
        self.weekly_teaching_schedule = dict()

    def estimate_weeks_required(self, student: Student, subject: str) -> int:
        """"""
        LLM = ChatOpenAI() # Create OpenAI instant 
        
        while True:
            try:
                estimated_week = int(LLM(prompt.get_estimated_weeks_format_instructions(student, subject)).content) # Pass the prompt into OpenAI and convert response into 
            except Exception as e: 
                print("estimate week required fails. Reason: ", e)
            
            if estimated_week > 0:
                break
        print("Estimated_week: ", estimated_week)
        return estimated_week

    def generate_weekly_topics(self, student: Student, subject: str, estimated_weeks: int) -> None:
        """"""
        LLM = ChatOpenAI() # Create OpenAI instant 

        response = LLM(prompt.get_weekly_topics_format_instructions(student, subject, estimated_weeks)).content
        weekly_topics = response.split(",")

        for index in range(0, len(weekly_topics)):
            self.weekly_teaching_schedule[f"week_{index}"] = {
                "Topic": weekly_topics[index],
                "Check_List": list,
                "Process": 0
            }
        
        self.topic_list = weekly_topics
        self.estimated_weeks = len(weekly_topics)
        print("Weekly topic generated: ", weekly_topics)
        
    
    def generate_topic_checklist(self, student: Student):
        """"""
        LLM = ChatOpenAI() 
        for index in range(0, self.estimated_weeks):
            response = LLM(prompt.get_topic_checklist_instructions(student, self.subject, self.weekly_teaching_schedule[f"week_{index}"]["Topic"], self.topic_list)).content

            check_list = response.split(",")

            self.weekly_teaching_schedule[f"week_{index}"]["Check_list"] = check_list
            print(f"week_{index} Checklist: ", check_list)
            time.sleep(60)

student = Student.Student("Stephen", 10, "Male", "Primary School - 1", "Slow in learning")
course = Course("Data Structure")
estimated_weeks = course.estimate_weeks_required(student, "Data Structure")
course.generate_weekly_topics(student, "Data Structure", estimated_weeks)
course.generate_topic_checklist(student)











        













