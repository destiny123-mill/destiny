def calculate_average(scores):
    return sum(scores) /len(scores)

def get_grade(average):
    if average >=70:
        return"A"
    elif average>=60:
        return"B"
    elif average >=50:
        return"C"
    elif average >=45:
        return"D"
    else:
        return"F"
    
    num_students = int(input("how many students are in the class?"))
names = []
averages = []

for i in range(num_students):
    print(f"\nstudent{i+1}")

    name = input("Enter student name:")

    num_subjects=int(input("how many subjects did they take?"))

    scores = []

    for j in range(num_subjects):
        while True:
            try:
                score = float(input(f"enter score for subjects {j + 1}:"))

                if 0<=score <=100:
                    scores.apprend(score)
                    break
                else:
                    print("score must be between 0 and 100.")

            except ValueError:
                print("invalid input.enter a number.")

average = calculate_average(scores)

names.append(name)
averages.append(average)

print("\n---CLASS REPORT---")

for i in range(num_subjects):
    grade=get_grade(averages[i])

    print(f"{names[i]}-average:{averages[i]:2f}-grade:{grade}")

    class_average = calculate_average(averages)

    print(f"{names[i]} - average:{average[i]:2f} -grade:{grade}")

    class_average = calculate_average(averages)

    print(f"\nClass Average:{class_average:.2f}")

    highest_average=averages[0]
    topper = names[0]

    for i in range (i,num_students):
        if averages[1]>highest_average:
           highest_average=averages[1]
           topper = names[i]
print(f"class topper":{topper}with an average of {highest_average:>2f}")
      
