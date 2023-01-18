import json #This is needed in order to be able to read and save to the json files
import random #This is needed in order to choose a random student in a grade
allStudents = {} #Defines allStudents
prizes = {} #Defines prizes
with open('Students.json','r') as file:
    allStudents = json.load(file) #Loads student data
with open('Prizes.json','r') as file:
    prizes = json.load(file) #Loads prize data

def update_student_points(student,pointsAdded,allStudents):
    if not student in allStudents: #Checks if the name provided is not in the allStudents list
        return("Student does not exist")
    elif not str.isnumeric(pointsAdded):
        return("Points must be a valid number")
    else:
        allStudents[student]["points"] = pointsAdded #Sets the students points to the amount in pointsAdded
        with open('Students.json','w') as file: #Opens the Students.json file in order to save
            json.dump(allStudents,file,indent=2) #Saves the students points
        with open('Students.json','r') as file:
            print(file)
            allStudents = json.load(file) #Updates allStudents with the student points saved previously
        return("Updated Points")
def get_student_points(student,allStudents):
    if not student in allStudents: #Checks if the name provided is not in the allStudents list
        return("Student does not exist")
    else:
        return allStudents[student]["points"] #Returns the students points
def get_random_student_in_grade(grade,allStudents):
    students_in_grade = []
    for student in allStudents: #Loops through all the students in Students.json
        if allStudents[student]["grade"] == grade: #Checks if the student is in the certain grade provided
            students_in_grade.append(student) #Adds the student to a list
    if students_in_grade: #Checks if there is a student in the grade provided
        return random.choice(students_in_grade) #Returns random student
    else:
        return("No students in the grade provided")
def get_student_prizes(student,allStudents):
    student_prize_cost = 0
    student_prize = None
    if not student in allStudents: #Checks if the name provided is not in the allStudents list
        return("Student does not exist")
    else:
        for prize in prizes: #Loops through all prizes in Prizes.json
            if int(allStudents[student]["points"]) >= prizes[prize]["points"] and prizes[prize]["points"] >= student_prize_cost: #Makes sure that the student has enough points and makes sure the student gets only one prize with the amount of points they have.
                student_prize_cost = prizes[prize]["points"] #Sets the variable to how many points the previous prize was, so that the prizes can not be lower than the prize they should have, which is checked with the line above
                student_prize = prize  #Sets the students prize to the prize that they won with the amount of points they have
        return(student_prize) #Returns prize

#update_student_points("Alex","23",allStudents)
#get_random_student_in_grade("12",allStudents)
#get_student_prizes("Alex",allStudents)
#get_student_points("Alex",allStudents)