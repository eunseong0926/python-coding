from 학생 import Student
# 학생.py 내에 존재하는 class 나 method Student를 사용한다.

학생1 = Student("철수",17)
print(학생1.정보호출기능())

학생1.성적추가기능(90)
학생1.성적추가기능(100)
학생1.성적추가기능(80)
print(학생1.평균계산기능())


#학생2 = Student()
#print(학생2.정보호출기능())
# TypeError : Student.__init__() missing 2
# required poditional aguments : 'name' and 'age'