# countries = ["IND", "BAN", "SL", "AUS", "NZ"]

# print(type(countries))

# countries = ("IND", "BAN", "SL", "AUS", "NZ")

# print(type(countries))

# data = tuple("INDIA")

# print(data) # ==> ('I', 'N', 'D', 'I', 'A')

data = (1, 2, 3, 4)

print(type(data))
print(id(data))

# print(tuple(list(data).append(5)))this is wrong

data = list(data)
data.append(5)

print(tuple(data))

print(id(data))