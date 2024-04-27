#Create an Arrays

#insert value 10 at position 2
#Inserting into Static array
arr = [1, 2, 3, 4, 5] # Initialize the list
pos = 2  # Position to insert the new value
value = 10 # Value to be inserted

# Shift elements to the right from the specified position
for i in range(len(arr) - 1, pos-1, -1): # Iterate backwards
    print(pos-1)
    print('222222',arr[i],arr[i-1])
    arr[i] = arr[i-1] # Replace each element with the preceding one

# After shifting elements, insert the new value at the desired position

# Insert the new value at the desired position
arr[pos] = value
print(arr)





# Output the modified list

# Insert Into Dynamic arrays
arr1 = [1, 2, 3, 4, 5,6]  # Initialize the list
arr1.insert(2,10)

#Insert element at last in dynamic array
arr1.append(20)
print(arr1)

#beggining
arr1.insert(0,20)
print(arr1)