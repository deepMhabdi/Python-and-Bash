#2. Student Grades
students = {"Deep": 90, "dev": 50, "devank": 80, "rohit": 10}
print(students)

while True:
    choice = input("\n1.Add 2.Update 3.Print 4.Exit\n") 
    
    if choice == "1":
        name = input('Name: ')
        grade = int(input("Grade: "))
        students[name] = grade
        
    elif choice == "2":
        name = input("Name to be updated: ")
        if name in students:
            students[name] = int(input("New Grade: "))
            
        else: 
            print("not found!")
            
    elif choice == "3":
        for s, g in students.items():
            print(s, ":", g)
    
    elif choice == "4":
        break
    
    else: 
        print("Invalid  choice!")


