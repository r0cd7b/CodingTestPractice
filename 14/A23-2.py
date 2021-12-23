# 국영수
from sys import stdin

n, students = int(stdin.readline()), []
for _ in range(n):
    students.append(stdin.readline().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])

"""
입력 예시
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sungyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
출력 예시
Donghyuk
Sangkeun
Sungyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
"""
