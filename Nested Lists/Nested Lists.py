#%%
students = []  # Define the "students" list
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])  

    students.sort(key=lambda x: x[1])  # Sort students based on scores in ascending order
    second_lowest_score = sorted(set([student[1] for student in students]))[1]  # Get the second lowest score
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]  # Get the names of students with the second lowest score
    for student in sorted(second_lowest_students):
        print(student)

# %%
