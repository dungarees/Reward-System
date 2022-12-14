import json #This is needed in order to be able to read and save to the json files

allStudents = {}
prizes = {}
with open('Students.json','r') as file:
    allStudents = json.load(file) #Loads student data
with open('Prizes.json','r') as file:
    prizes = json.load(file) #Loads prize data

def update_student_points(student,pointsAdded):
    allStudents[student]["points"] = pointsAdded #Sets the students points to the amount in pointsAdded
    with open('Students.json','w') as file: #Opens the Students.json file in order to save
        json.dump(allStudents,file,indent=2) #Saves the students points

def get_random_student_in_grade(grade):
    for student in allStudents: #Loops through all the students in Students.json
        if allStudents[student]["grade"] == grade: #Checks if the student is in the certain grade provided
            return student #Returns student
def get_student_prizes(student):
    student_prize_cost = 0
    student_prize = 0
    for prize in prizes: #Loops through all prizes in Prizes.json
        if allStudents[student]["points"] >= prizes[prize]["points"] and prizes[prize]["points"] >= student_prize_cost: #Makes sure that the student has enough points and makes sure the student gets only one prize with the amount of points they have.
            student_prize_cost = prizes[prize]["points"] #Sets the variable to how many points the previous prize was, so that the prizes can not be lower than the prize they should have, which is checked with the line above
            student_prize = prize  #Sets the students prize to the prize that they won with the amount of points they have
    return(student_prize) #Returns prize
#update_student_points("Alex",23)
#get_random_student_in_grade(12)
get_student_prizes("Alex")