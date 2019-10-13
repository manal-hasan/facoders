grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

x=input("Choose one: students_names, student_score, students_count: ")
def students_names():
    print("grade_one student's",list(grade_one))
    print("grade_two student's",list(grade_two))
    print("grade_three student's",list(grade_three))
def student_score():
    grade=input("Enter student's class name: ")
    if grade=="grade_one":
        name=input("Enter student name:")
        if name in grade_one:
            b=grade_one.get(name)
            score=sum(b)
            print(name,score,",","grade one")
    elif grade=="grade_two":
        name=input("Enter student name:")
        if name in grade_two:
            b=grade_two.get(name)
            score=sum(b)
            print(name,",",score,"grade two")
    elif grade=="grade_three":
        name=input("Enter student name:")
        if name in grade_three:
            b=grade_three.get(name)
            score=sum(b)
            print(name,score,",","grade three")
def students_count():
    n=0
    for k in grade_one.keys():
        n +=1
        count1=n
    print("grade_one: ",count1,"students")
    n=0
    for k in grade_two.keys():

        n +=1
        count2=n
    print("grade_two: ",count2,"students")
    n=0
    for k in grade_three.keys():
        n +=1
        count3=n
    print("grade_three: ",count3,"students")
while True:
   if x=="students_names":
       print(students_names())
   elif x=="students_count":
       print (students_count())
   elif x=="student_score":
       print(student_score())
   end=input("if you end print done,else print more:")
   if end=="done":
       print(exit())
   else:
       x=input("Choose one: students_names, student_score, students_count: ")
   continue
