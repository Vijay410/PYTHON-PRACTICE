class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grades = new_grade
        
    def average(self):
        return sum(self.grades) / len(self.grades)
    
    def __len__(self):
        return len(self.grades)
    
    def __getitem__(self, index):
        return self.grades[index]
    
    def __add__(self,a,b):
        return a + b
    
s1 = Student('Vijay', [34, 56, 78, 99])
s2 = Student('Ved', [70, 88, 90, 99])

print(len(s1))  # Output: 4
print(len(s2))  # Output: 4

print((s1[0]))  # Output: 4
print((s2[1]))  # Output: 4

print(s1(80,90))