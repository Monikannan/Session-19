marks = input("Enter the students marks : ")
mark_list = [int(mark) for mark in marks.split(',')]
result = [ ]

for mark in mark_list:
    if mark >=35:
        result.append(" Pass")
    else:
        result.append(" Fail ")

print("Results:")
print(result)
