# 111 [編碼練習二(function運用)]-找出成績第二高
# (二)用    (變數x)將成績先排序再做比較
#     [變數x = sorted(變數x) →數字從小到大]；
#     [變數x = sorted(變數x, reverse = True) →數字從小到大]

students = [
    ['Jerry', 60], ['Justin', 73],
    ['Tom', 94], ['Akriti', 47],
    ['Harsh', 73]
]
def second_highest(students):
    grades = []
    for grade in students:
        grades.append(grade[1])
    grades = sorted(grades, reverse=True) # 由大排序到小
    print('由大到小: ',grades)
    for student in students:
        if student[1] == grades[1]:
            print(student)

second_highest(students)