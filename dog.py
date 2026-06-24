class Dog:
    # 클래스 변수 (모든 인스턴스가 공유)
    species = "강아지"

    # 생성자 : 객체가 만들어질 때 자동 실행
    def __init__(self, name, age):
        self.name = name
        self.age = age
# 자바에서는 위와 같은 생성자를 아래와 같이 표현
# public Dog(String name, int age){
#        this.name = name;
#        this.age = age;
#}
    # 메서드(기능)
    def 짖는기능(self): # 현재 클래스 위치에서 해당 이름을 사용하겠다.
        return f"{self.name}이(가) 멍멍 짖습니다."

    def 정보호출기능(self):
        return f"이름 : {self.name}, 나이 : {self.age}살"