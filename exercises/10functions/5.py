def is_prime(num):
    prime = True
    if num == 1:
        prime = False
        return prime
    elif num == 2 or num == 3:
        prime = True
        return prime
    else:
        for i in range(4, num):
            if num % i == 0:
                prime = False
                break
        return prime


# x = 13
# print(f"{x} is prime = {is_prime(x)}")

first15_prime = []
i = 1
while len(first15_prime) < 15:
    if is_prime(i):
        first15_prime.append(i)
    i = i + 1

print(first15_prime)
