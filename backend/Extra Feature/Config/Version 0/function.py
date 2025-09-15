# # def foo() -> int :
# #     print("Hello HAXTON")
# #     n1 = 15
# #     n2 = 15
# #     return n1+n2

# # sum = foo()
# # print(sum)

# # def add(n1:int, n2:int) -> int:
# #     return n1+n2

# # n1 , n2 = 10 , 50
# # ans = add(n1,n2)
# # print(ans)

# def evenOdd(x):
#     if(x % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")

# evenOdd(14)
# evenOdd(3)

# # Default Argument
# def myFun(x,y=50):
#     print("x: ", x)
#     print("y: ", y)

# myFun(10,20)

# print("Harshal"," World",sep='*')

# x = str("s1")
# x = str(3.0)
# print(x)
# print(type(x))

string = ""
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)