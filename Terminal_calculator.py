def add(lst):
    a = lst[0]
    for i in range(1,len(lst)):
        a = a + lst[i]
    return a

def subtract(lst):
    a = lst[0]
    for i in range(1,len(lst)):
        a = a - lst[i]
    return a

def multiply(lst):
    a = lst[0]
    for i in range(1,len(lst)):
        a = a * lst[i]
    return a

def divide(lst):
    a = lst[0]
    for i in range(1,len(lst)):
        if lst[i] == 0:
            return "Error: Cannot divide by zero"
        a = a / lst[i]
    return a

def main():
        result = None
        lst = []
        print("=============Terminal Calculator=============")
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
        op = int(input("Enter action to perform:"))

        if op not in [1,2,3,4]:
            print("The choice which u have entered is not valid, please enter valid action number(1 to 4 only)")
            return

        n = int(input(f"Enter how many numbers to calculate:"))
        for i in range(1,n+1):
                l = float(input(f"Enter {i} number:"))
                lst.append(l)

        print(f"The entered elements in list format is as follows:-")
        print(lst)
        match op:
             case 1:
                result = float(add(lst))
             case 2:
                result = float(subtract(lst))
             case 3:
                result = float(multiply(lst))
             case 4:
                result = divide(lst)

        if result is not None: 
         if isinstance(result , str):
            print(f"Final answer is: {result}")       
        else:
            print(f"Final answer is: {result:.3f}")

while True:
    main()
    ans = input("do you want to continue using terminal calculator[Y/N]:")
    if ans.lower() != 'y':
        print("Thank you for using the calculator")
        print("Byeeeeeeeeeeeeeeeeeee👋👋👋👋👋!")
        break