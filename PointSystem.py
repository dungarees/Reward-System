import json

allStudents = {}
with open('Students.json','r') as file:
    allStudents = json.load(file)

def update_student_points(student,pointsAdded):
    allStudents[student]["points"] = pointsAdded
    with open('Students.json','w') as file:
        json.dump(allStudents,file,indent=2)
    

def check_student_prizes(student):
    print("check prize")
def get_random_student_in_grade(grade):
    gradeStudents = []
    for student in allStudents:
        print(allStudents[student]["grade"])
        if allStudents[student]["grade"] == grade:
            gradeStudents.append(student)
    return gradeStudents

print(get_random_student_in_grade(12))
#update_student_points("Alex",23)