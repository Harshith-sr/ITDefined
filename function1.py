# def greeting(cls_name: str):
#     # cls_name = int (cls_name)
#     print(f"Good morning, Welcome to {cls_name} class")

# # greeting(1)

# greeting("mern")

# greeting("python")

# greeting("C++")
    
# def add2Number(num1, num2):
#     out = num1 + num2
#     # print(out)
#     return out


# x = add2Number(10,20)

# print(x)


# lst = [22, 34, 64, 5, 33, 52, 76]

# lst.sort(reverse=True)

# print(lst)


# data = "Good Morning"

# out = data.replace("Morning", "Evening")

# print(data)

# print(out)


# def add2Number(num1, num2):
#     out = num1 + num2
    
#     # total = out + 10

#     print(out)
#     return 10


# y = add2Number(20,40)

# print(y)

# def fun1():
#     print("function 1")

# def main():
#     fun1()
#     fun2()

# main()

# def fun2():
#     print("function 2")


# def main():
#     fun1()
#     fun2()

# main()

# sum(2,3)
# print(sum(2,3))

#nested function

# def main():
#     x = 20
#     def func1():
#         nonlocal x
#         x += 10
#         print(f"the value of x is {x}")
#     print(f"the value of x is {x}")
#     func1()

# main()

# def outer(x):
#     # x = 30
#     def inner(y):
#         # nonlocal x
#         # y = 40
#         return x + y
#     return inner

# out = outer(30)
# print(out)


# def power(x):
#     def value(y):
#         return y ** x
#     return value

# value = power(3)

# print(value(4))
    
# def outer():
#     x = 10
#     print(x)
#     def inner():
#         # nonlocal x
#         print(x)
#         y = 20
#         return  x + y 
#     return inner

# value = outer()

# print(value())

# def outer(x):
#     x = 30
#     def inner(y):
#         nonlocal x
#         y = 40
#         return x + y
#     return inner

# out = outer(30)
# print(out)

# def outer(x):
#     print(x)
#     def inner(y):
#         print(x)
#         print(y)
#         print(x+y)
#     return inner

# def main():
#     res = outer(10)
#     res(20)

# main()
    

def outer(inner_func):
    out = inner_func()
    print(out)

def greet():
    return "Good Morning"

def Wishes():
    return "Happu Birthday"

outer(greet)
outer(Wishes)
    
    