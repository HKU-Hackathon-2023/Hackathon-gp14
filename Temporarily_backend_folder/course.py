from langchain.schema import SystemMessage, AIMessage, HumanMessage
import Student

class Course:
    
    def __init__(self, subject) -> None:
        self.subject = subject
        self.course_name: str 
        self.estimated_weeks: int 
        self.weekly_teaching_schedule: {
            "week 1": {
                "topic": str, 
                "Description": str, # Description of the week on what would be included
                "sub topic": list(), 
                "chat history": None
            },
            "week 2": {
                "topic": str,
                "sub topic": list(), 
                "chat history": None
            },
            "week 3": {
                "topic": str, 
                "sub topic": list(), 
                "chat history": None
            },
            "week 4": {
                "topic": str, 
                "sub topic": list(), 
                "chat history": None
            }
        }

    def generate_course_name(self):
        """This will pass the course schedule to GPT to ask it to think a name for the course"""
    
    def estimate_number_of_weeks_to_complete():
        """This function is temporality deactive"""
        pass
        
        
    def generate_weekly_topic(self, student: Student):
        """This function generate the topic that would teach each week"""

        # Create a OpenAI Chat Instant
        chat = 

        # Chat with 
        weekly_topics_list = chat([SystemMessage(content="""You are a teacher specialised in teaching deaf student. You are now designing a 
                                                 course outline for them to learn their interested topics outside of classroom. 
                                                 Consider their education level, and special education need while designing the outline"""),
                                    HumanMessage(content="""Your student is interested in """)])

    def generate_weekly_teaching_schedule(self, estimated_week = 4):
        """This function generate the weekly topic"""
        # Find the number of weeks needed to complete the course
        self.estimated_weeks = 4

        # Generate Weekly Topic
        generate_weekly_topic(Student)
    













