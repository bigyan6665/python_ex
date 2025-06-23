# baaki xa
# st = {1,4,5,7,8,11,12,15,18}
# new_list = [num*3 if num%2==0 else num*2 for num in st]
# print(new_list)

st = {1,4,5,7,8,11,12,15,18} 
# ya bata double wa triple garda 5 aaune case nai xaina ta??? tesiale == 5 check nagarda ni hunca
new_list = []
for num in st:
    if num == 15: # stops further calculation
        break
    else:
        if num%2==0:
            tripled = num*3
            if tripled == 5: # ya == 5 check nagarda ni hunca
                continue
            else:
                new_list.append(tripled)
        else:
            doubled = num*2
            if doubled == 5: # ya == 5 check nagarda ni hunca
                continue
            else:
                new_list.append(doubled)
print(new_list)