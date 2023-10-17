from langchain.schema import SystemMessage, AIMessage, HumanMessage

estimate_week_complete_prompt = f"You are a teacher specialising in teaching deaf student. He is a {education_level} student"





class Course:
    
    def __init__(self, subject) -> None:
        self.subject = subject
        self.course_name: str 
        self.estimated_weeks: int 
        self.weekly_teaching_schedule: {
            "week 1": {
                "topic": str, 
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
        
        

    def generate_weekly_teaching_schedule(self, estimated_week = 4):
        """This function generate the weekly topic"""
        # Find the number of weeks needed to complete the course
        self.estimated_weeks = estimate_number_of_weeks_to_complete()
    
    def 













