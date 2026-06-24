class Student:
    # 반드시 init이나 main과 같은 명칭을 사용할 때는 양옆에 __를 각각 적어줘야한다.
    def __init__(self, name, age):
        # name 과 age는 처음부터 데이터를 넣어서 Student 클래스를 활용해야한다. 는 개념
        self.name = name
        self.age = age

        # Student() 클래스를 사용할 때 처음부터 추가하지 않나도 되는것
        self.성적 = []

    def 정보호출기능(self):
        return f"이름 : {self.name}, 나이 : {self.age}살"
    
    def 성적추가기능(self, 점수):
        self.성적.append(점수)

    def 평균계산기능(self):
        if len(self.성적) == 0: # 성적 데이터가 하나도 없을 경우
            return "기입된 성적이 존재하지 않습니다."
        return sum(self.성적) /len(self.성적)
        