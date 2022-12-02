import json

sporting_events = {"Football","Soccer","Hockey","Basketball","Baseball"}
non_sporting_events = {"Spelling Bee","Chess Competition","Trivia Night","School Dance","School Play"}
allStudents = {}
with open('Students.json','r') as file:
    allStudents = json.load(file)

def update_student_points(student,pointsAdded):
    allStudents[student]["points"] = pointsAdded
    with open('Students.json','w') as file:
        json.dump(allStudents,file,indent=2)

def check_student_prizes(student):

def get_random_student_in_grade
update_student_points("Alex",23)