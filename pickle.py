# https://www.youtube.com/watch?v=eWrTSBIQess

import pickle
import os;os.system("cls")


data1 = {"name":"Mike",
         "age":26,
         "hair color":"brown"}

print("data1")
print(type(data1))
print(data1)
print()


with open("data.pkl","wb") as file:
    pickle.dump(data1,file)

