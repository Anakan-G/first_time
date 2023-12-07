import random
import os; os.system("cls")

#random.seed(123)

num_trials = 1000
x = []
y = []


for num_people in range(1,51):
    matching_birthdays = 0

    for trial in range(num_trials):
        birthdays = set()

        for person_num in range(num_people):
            birthdays.add(random.randint(1,365))

        if len(birthdays) != num_people:
            matching_birthdays += 1

    probability = matching_birthdays / num_trials
    print(f"Current number of people: {num_people:2}   Probability: {probability:.2%}")

    x.append(num_people)
    y.append(probability*100)


import matplotlib.pyplot as plt

plt.plot(x,y)
plt.title("Birthday Paradox",fontsize=36,weight="bold")
plt.xlabel("Number of People",fontsize=16,weight="bold")
plt.ylabel(f"Probability ({num_trials: ,} trials)",fontsize=16,weight="bold")
plt.xticks([0,5,10,15,20,25,30,35,40,45,50])
plt.yticks([0,10,20,30,40,50,60,70,80,90,100])
plt.grid(which="both")
plt.xlim(0,50)
plt.ylim(0,100)
plt.show()