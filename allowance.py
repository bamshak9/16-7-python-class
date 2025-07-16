starting_allowance = 2000
books = 400
current_allowance = float(starting_allowance) -float(books)
found = 100
current_allowance = float(current_allowance) + float(found)
snacks = 250
current_allowance = float(current_allowance) - float(snacks)
siblings = float(current_allowance) * 0.25
current_allowance = float(current_allowance) - float(siblings)
data = (1/3) * float(current_allowance)
current_allowance = float(current_allowance) - float(data)
savings = float(current_allowance) //2
remainder = float(savings) % 100
print(remainder)




allowance = 2000
allowance -= 400
allowance += 100
allowance -= 250
allowance *= 0.75
allowance *= (2/3)
allowance //= 2
allowance %= 100
print(allowance)


