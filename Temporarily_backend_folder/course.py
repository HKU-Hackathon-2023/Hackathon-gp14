import genCourse

class Course:

    def __init__(self, topic):
        self.Topic = topic
        self.Subtopics = {
            "week1": None,
            "week2": None,
            "week3": None,
            "week4": None,
        }
        self.week_1_topics={
            "Name":None,
            "Introduction": None,
            "Explanation": None,
            "Examples":None
        }
        self.week_2_topics = {
            "Name":None,
            "Introduction": None,
            "Explanation": None,
            "Examples": None
        }
        self.week_3_topics = {
            "Name":None,
            "Introduction": None,
            "Explanation": None,
            "Examples": None
        }
        self.week_4_topics = {
            "Name":None,
            "Introduction": None,
            "Explanation": None,
            "Examples": None
        }
        learning_materials=None
        history=None


        def genSubtopics(topic):
            SubtopicList = genCourse.GenSubtopics(topic)
            for i in range(1, 5):
                self.Subtopics[f"week{i}"] = (SubtopicList[i - 1])

        def gen_week_1_topics(name):
            self.week_1_topics["Name"]=name
            self.week_1_topics["Introduction"], self.week_1_topics["Explanation"], self.week_1_topics["Examples"] = \
                genCourse.genContents(name)

        def gen_week_2_topics(name):
            self.week_2_topics["Name"]=name
            self.week_2_topics["Introduction"], self.week_2_topics["Explanation"], self.week_2_topics["Examples"] = \
                genCourse.genContents(name)
        def gen_week_3_topics(name):
            self.week_3_topics["Name"]=name
            self.week_3_topics["Introduction"], self.week_3_topics["Explanation"], self.week_3_topics["Examples"] = \
                genCourse.genContents(name)
        def gen_week_4_topics(name):
            self.week_4_topics["Name"]=name
            self.week_4_topics["Introduction"], self.week_4_topics["Explanation"], self.week_4_topics["Examples"] = \
                genCourse.genContents(name)

        genSubtopics(self.Topic)
        gen_week_1_topics(self.Subtopics["week1"])
        gen_week_2_topics(self.Subtopics[1])
        gen_week_3_topics(self.Subtopics[2])
        gen_week_4_topics(self.Subtopics[3])














