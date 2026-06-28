num1,num2=map(int,input("enter two numbers separated by space:").split())
operation=input("enter operation (+,-,*,/):")
if operation=="+":
    print("Result:",num1+num2)
elif operation=="-":
    print("Result:",num1-num2)
elif operation=="*":
    print("Result:",num1*num2)
elif operation=="/":
    print("Result:",num1/num2)
else:
    print("invalid operator")    