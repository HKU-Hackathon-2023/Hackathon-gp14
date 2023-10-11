import genCourse

class course:
    Topic = None
    Subtopics = {
        "week1": None,
        "week2": None,
        "week3": None,
        "week4": None,
    }
    week_1_topics={
        "Name":None,
        "Introduction": None,
        "Explanation": None,
        "Examples":None
    }
    week_2_topics = {
        "Name":None,
        "Introduction": None,
        "Explanation": None,
        "Examples": None
    }
    week_3_topics = {
        "Name":None,
        "Introduction": None,
        "Explanation": None,
        "Examples": None
    }
    week_4_topics = {
        "Name":None,
        "Introduction": None,
        "Explanation": None,
        "Examples": None
    }
    learning_materials=None
    history=None
    SubtopicList = genCourse.GenSubtopics()

    for i in range(1,5):
        Subtopics[f"week{i}"]=(SubtopicList[i-1])



print(course.Subtopics)





