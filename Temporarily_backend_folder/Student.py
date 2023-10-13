class Student:
    number_of_students = 0 # ignore for now

    def __init__(self, name: str, age: int, gender: chr, education_level: str, special_need: str) -> None:
        # Personal Information & Education needs
        self.name = name
        self.age = age
        self.gender = gender
        self.education_level = education_level
        self.special_education_need = special_need

        # Course
        self.courses_database = dict() # dict(course_name: course object)

    def retrieve_courses_list(self) -> list:
        """return a list that contain all courses that created by the student"""
        return self.courses_storage.keys()
    
    def delete_course(self, course_name: str = None) -> None:
        """delete the course from the student course database"""
        del self.courses_storage['course_name']
    
    def create_course(self, subject: str):
        pass
