
#This mnethod using simple for loop to double the number
numbers = [2,4,5,6,7]
def double_num(numbers):
    doubled_numbers = []
    for num in numbers:
        res = num * 2
        doubled_numbers.append(res)

    return doubled_numbers

data = double_num(numbers)
print(data)

def double_num_list_comp(numbers):
    double_num = [num * 2 for num in numbers]
    return double_num

data =  double_num_list_comp(numbers)
print(data)

def prime(numbers):
    double_num = [num % 2 == 0 for num in numbers]
    return double_num

data =  prime(numbers)
print(data)

friend_ages = [22,31,42,34,56]
age_strings = [f'My Frind Age is {age} years old.' for age in friend_ages]
print(age_strings)

names = ['Vijay','Ved','Vik','Vin','Mat']
friend_ages = [22,31,42,34,56]
age_strings = {name: f"My friend {name}'s age is {age} years old." for name, age in zip(names, friend_ages)}

print(age_strings)

names = ['Vijay','Ved','Vik','Vin','Mat']
friend_ages = [22,31,42,34,56]
for i in range(len(names)):
    for j in range(i+1, len(names)):

        if friend_ages[i] < friend_ages[j]:
            print(f"{names[i]} is younger than {names[j]}")
        elif friend_ages[i] > friend_ages[j]:
            print(f"{names[i]} is older than {names[j]}")
        else:
            print(f"{names[i]} and {names[j]} are the same age")

names = ['Vijay','Ved','mat','Vik','vian','Mat']
names = sorted(names, key=lambda x:x.lower())
print(names)


names = ['Vijay','Ved','mat','Vik','vian','Mat']
name = [name.lower() for name in names]
print(name)


ages = [12,34,56,7,8,88,99]
odds = [age for age in ages if age % 2 == 1]
even = [age for age in ages if age % 2 == 0]

print(odds,even)

friends = ["Rolf","ruth", "charles","Jen","Vijay"]
guests = ["jose","Bob","Rolf","Charlie","michel","Vijay"]

friends_lower = {n.lower() for n in friends}
guests = {n.lower() for n in guests}

print(guests.intersection(friends_lower))
print(friends_lower.intersection(guests))
print(friends_lower.difference(guests))
print(friends_lower.symmetric_difference(guests))


friends = ["Rolf","ruth", "charles","Jen","Vijay"]
age = [44,28,58,34,27]

friend_ages = {
    friends[i] : age[i]
    for i in range(len(friends))
}
print(friend_ages)
print(list(zip(friends,age)))
print(dict(enumerate(friends)))


numbers = list(range(10))
print(numbers)
doubled = [n*2 for n in numbers]
print(doubled)
