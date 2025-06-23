# loops

# 1. for loop
# countries = ['nepal','india','bhutan']
# for country in countries:
#     print(country.title())
# else:
#     print("Loop terminated")

# else is executed at the end of loop execution
# else is executed if the loop is finished normally(without break) othewise not executed

# for i in range(0,11):
#     print(i**2)
# else:
#     print("Loop terminated")

# dt = {"name":"bigyan","address":"koteshwore"}
# for k,v in dt.items():
#     print(f"{k} = {v}")
# else:
#     print("Loop terminated")

# 2.while loop
# i = 0
# while(i <= 10):
#     i = i + 1 
#     if( i == 5 ):
#         break
#     print(i)
# else:
#     print("Loop terminated")

# i = 0
# while(i <= 10):
#     i = i + 1 
#     if( i == 5 ):
#         continue
#     print(i)
# else:
#     print("Loop terminated")

# # nested loop
# for i in range(1,4):
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}")
#     else:
#         print('\n')

# # list comprehension(list,tuple,set,dictionary)
# # problem
# num = [4,7,9]
# inc_ls = []
# for i in num:
#     inc_ls.append(i +10)
# print(inc_ls)

# # solution
# num = [4,7,9]
# inc_ls = [i + 10 for i in num] #[operation iteration]
# print(inc_ls)

# tuple
# num = (4,7,9) 
# inc_ls = (i + 10 for i in num) #[operation iteration]
# not workin with tuple
# print(inc_ls)

# set
# num = {4,7,9}
# inc_st = {i + 10 for i in num} #[operation iteration]
# print(inc_st)

# num = {4,7,9}
# inc_st = {i + 10 for i in num if i%2 == 1} #[operation iteration condition]
# print(inc_st)


# num = {4,7,9}
# inc_st = {i+10 if i%2 == 1 else i+5 for i in num } #[operation condition iteration ]
# print(inc_st)

# dictionary
dt = {'e1':1000,'e2':2000}
new_dt = {emp : salary * 2 for emp,salary in dt.items()}
print(new_dt)
