class 검색엔진:
    """
    용도가 다르기 때문에 다르게 작성
    1번 self, name, age
        Dog() 클래스를 사용할 때부터 데이터를 받아와서 시작
        처음부터 강아지 1번과 같은 공간을 생성할 때
        데티터를  넣은 상태에서 만드는 작업을 시작

        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        Dog() 클래스로 무언가를 만들 때
        처음부터 데이터를 넣어서 만들 필요하 없다.
        나중에 데이터를 추가해도 된다.
        def __init__(self):
        self.data = []

        def __init__(self,data):
    """
    def __init__(self):
        # TODO 1 : 페이지 목록을 저장할 빈 리스트를 만드세요.
        self.data = []


    def 페이지추가기능(self, title):
        # TODO 2 : data 리스트에 title을 추가하세요 ( append 사용 )
        self.data.append(title)


    def 검색기능(self, 키워드):
        # TODO 3 : data 리스트를 돌면서 키워드가 제목에 포함된 것만 출력하기
        #print(self.data)
        for page in self.data:
            if 키워드 in page:
                print(page)