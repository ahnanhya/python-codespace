#Dictionaries.py

student = {'name': '', 'class': '', 'marks': {'math': 0, 'science': 0, 'english': 0}}

student['name'] = input('Enter the student\'s name: ')
student['class'] = input('Enter the student\'s class: ')
student['marks']['math'] = float(input('Enter the student\'s Math Marks: '))
student['marks']['science'] = float(input('Enter the student\'s Science Marks:'))
student['marks']['english'] = float(input('Enter the student\'s English Marks:'))

total_marks = sum(student['marks'].values())
percentage = total_marks / 300 * 100

percentage = round(percentage, 2)

print("\n\n*STUDENTMARKSHEET*")
print('Name of the Student:', student['name'])
print('Class of the Student:', student['class'])
print('Math Marks:', student['marks']['math'])
print('Science Marks:', student['marks']['science'])
print('English Marks:', student['marks']['english'])
print('Total Marks:', total_marks)
print('Percentage:', percentage)
print("")
