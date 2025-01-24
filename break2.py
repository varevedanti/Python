no = int(input("Enter the number"))
number =[23,33,45,65,22,88,44,67,70]

for i in number:
    if (i==no):
        print ("Number Found in the List")
        break
else:
    print("Number not found in the List")
