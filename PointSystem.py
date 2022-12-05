import json

allStudents = {}
prizes = {}
with open('Students.json','r') as file:
    allStudents = json.load(file)
with open('Prizes.json','r') as file:
    prizes = json.load(file)

def update_student_points(student,pointsAdded):
    allStudents[student]["points"] = pointsAdded
    with open('Students.json','w') as file:
        json.dump(allStudents,file,indent=2)

def get_random_student_in_grade(grade):
    for student in allStudents:
        if allStudents[student]["grade"] == grade:
            return student
def get_student_prizes(student):
    for prize in prizes:
        if allStudents[student]["points"] >= prizes[prize]["points"]:
            print(prize)
#update_student_points("Alex",23)
#get_random_student_in_grade(12)
get_student_prizes("Alex")
