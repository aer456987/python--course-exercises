# 111 [編碼練習二(function運用)]-找出成績第二高
# (一)用if比較數字大小的方式算出排名第一、二

students = [
    ['Jerry', 85], ['Justin', 85],
    ['Tom', 100], ['Akriti', 82],
    ['Harsh', 85]
]
# students[0] = 名字; students[1] = 成績
# 先算出第一、二名
def second_highest(students):
    one = students[0]
    two = students[1]
    for student in students:
        if student[1] > one[1]:            #如果成績大於one就取代one
            one = student
        elif one[1] > student[1] > two[1]: # 如果成績大於two就取代two
            two = student
# 把成績拿出來再比一次，看有幾個二名
    for grades in students:         
        if grades[1] == two[1]:     # 如果成績 = two就印出
            print('第二名有: ', grades)

second_highest(students)