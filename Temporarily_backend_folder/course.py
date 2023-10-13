import genCourse

class Course:
    course_list: list(str) # list - contain name of all created courses
    course_count: int # int - reprsend course count 

    def __init__(self, subject):
        self.subject: str # String - Subject name from user input
        self.course_name: str # String - name of the course instant
        self.estimated_weeks: int # int - weeks needed/ estimated to complete the course
        self.weekly_teaching_schedule: {
            "week 1": {
                "topic": str, # Topic for the week
                "sub topic": list(), # [[sub_topic_1, completed?], ]
                "chat history": None
            },
            "week 2": {
                "topic": str, # Topic for the week
                "sub topic": list(), # [[sub_topic_1, completed?], ]
                "chat history": None
            },
            "week 3": {
                "topic": str, # Topic for the week
                "sub topic": list(), # [[sub_topic_1, completed?], ]
                "chat history": None
            },
            "week 4": {
                "topic": str, # Topic for the week
                "sub topic": list(), # [[sub_topic_1, completed?], ...]
                "chat history": None
            }
        }
        self.teaching_materials = None

    def create_course(self):
















