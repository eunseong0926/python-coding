import pygame

pygame.init() # pygame 시작 준비
화면 = pygame.display.set_mode((600, 400)) # 가로, 세로 창 크기 설정
pygame.display.set_caption("제목") # tkinter.title과 동일한 효과를 가짐

시계 = pygame.time.Clock() # 게임 속도를 조절하기 위한 트릭
# 게임만들기 = 알고리즘 수학에 대해서 사고 생각을 하게 되는 과정


x = 300
y = 200
while True: # x버튼이나 break return을 만나기 전까지 무한 실행

    # 1. 키보드/미웃 입력 감지
    for 이벤트 in pygame.event.get():
        if 이벤트.type == pygame.QUIT: # X 버튼 = QUIT
            pygame.quit() #소비자가 게임 종료버튼을 클릭하면 게임 중지

    # 2. 화면 그리기
    # fill((0,0,0)) 화면을 특정 색상으로 채우겠다 0,0,0 == 검정

    # 위쪽 방향 키 누르면 위로 이동
    키 = pygame.key.get_pressed() # 키 누름 감지하는 기능
    if 키[pygame.K_UP]:
        y -= 5 # 시작하는 위치에서 점점점 위로 올라가는 상황( 시작하는 위치 200에서 -5만큼 이동 )
    if 키[pygame.K_DOWN]:
        y += 5  # 시작하는 위치에서 점점점 아래로 올라가는 상황( 시작하는 위치 200에서 +5만큼 이동 )

    if 키[pygame.K_LEFT]:
        x -= 5 # 시작하는 위치에서 점점점 왼쪽으로 올라가는 상황( 시작하는 위치 300에서 -5만큼 이동 )
    if 키[pygame.K_RIGHT]:
        x += 5  # 시작하는 위치에서 점점점 오른쪽으로 올라가는 상황( 시작하는 위치 300에서 +5만큼 이동 )

    화면.fill((0,0,0))
    # draw.rectingle = 사각형 그리기
    # pygame.draw.rect( 어디화며에, 색상은,( 가로시작위치, 세로시작위치, 가로크기, 세로크기 ) )
    pygame.draw.rect(화면, (0, 255, 0), (x, y, 30, 100))

    # 화면.fill("blue")
    pygame.display.update() # 매번 키보드를 입력할때마다 화면에서 네모의 위치가 변경된 사항을 다시보여줘라
    시계.tick(60) #키보드를 입력했을 때 속도 ( 숫자가 낮을수록 속도가 느리고, 숫자가 높을수록 속도가 빠르다. )
