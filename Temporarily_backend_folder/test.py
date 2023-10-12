import course
import genCourse

Course1 = course.Course("data structures")
print(Course1.Topic)
print(Course1.Subtopics)
print(Course1.week_1_topics["Name"])
print(Course1.week_1_topics["Introduction"])
print(Course1.week_1_topics["Explanation"])
print(Course1.week_1_topics["Examples"])

print("-----------------------------------------------------------------------------")

print(Course1.week_1_topics["Introduction"])
print(Course1.week_1_topics["Explanation"])
print(Course1.week_1_topics["Examples"])