# # function
# # dry = donot repeat yourslef
# def cal_sqr(x):
#     """returns the square of the given number"""
#     return x**2 , x

# print(cal_sqr(5))



# # variable scope
# # 1.global scope
# # 2.local scope
# x = 10
# def outerfunc():
#     y = 5
#     def innerfunc():
#         print(x)
#         print(y)
#     innerfunc()
#     print(x)
#     print(y)

# outerfunc()

# # changing global variable from inner func = closure
# x = 10
# def outerfunc():
#     global x # this x references tp global 'x'
#     x = 2
#     def innerfunc():
#         print(x)
#     innerfunc()
#     print(x)

# outerfunc()
# print(x)


# default arg

# # arbitary arguments
# def product(*args):
#     print(args)
#     prod = 1
#     for num in args:
#         prod = prod * num
#     return prod
# print(product(2,4,6))
# print(product(45,6))

# keyword arguments

# # keyword arbitary arguments
# def product(**kwargs):
#     print(kwargs)
#     prod = 1
#     for num in kwargs.values():
#         prod = prod * num
#     return prod
# print(product(a=2,b=4,c=6))
# print(product(a=45,b=6))








# recursion



# lamba function = anonymous fn
product = lambda x,y:x*y
print(product(5,2))

# filter fn
user_age = [15,16,18,13,20,19]
filtered_age = list(filter(lambda x:x>=16,user_age))  #

# map fn
movies = [' avatar','Thor ','aVengers']
cleaned_list = list(map(lambda movie:movie.strip().upper(),movies))
print(cleaned_list)

# reduce fn