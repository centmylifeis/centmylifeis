import random
import pygame
###################################################
#기본 초기화 (반드시 해야 하는 것들)
pygame.init() 
#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
#화면 타이틀 설정
pygame.display.set_caption("뼈다귀 피하기 게임")

#FPS
clock = pygame.time.Clock()
###################################################

#1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
#배경 만들기
background = pygame.image.load("C:/Users/Samuel/Desktop/과제/pygame/background.png")

#캐릭터 만들기
character = pygame.image.load("C:/Users/Samuel/Desktop/과제/pygame/character.jpg")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  #화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

#이동 위치
to_x = 0
character_speed = 10

#뼈다귀 만들기
bone = pygame.image.load("C:/Users/Samuel/Desktop/과제/pygame/bone.png")
bone_size = bone.get_rect().size #이미지의 크기를 구해옴
bone_width = bone_size[0] #캐릭터의 가로 크기
bone_height = bone_size[1] #캐릭터의 세로 크기
bone_x_pos = random.randint(0, screen_width - bone_width) #랜덤으로 내려오는 뼈다귀
bone_y_pos = 0
bone_speed = 10
running = True 
while running:
    dt = clock.tick(70) #게임화면 초당 프레임 수를 설정

    #2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 설정되었는가?
            runnung = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += character_speed
        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

       
    #3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    bone_y_pos += bone_speed

    if bone_y_pos > screen_height:
       bone_y_pos = 0
       bone_x_pos = random.randint(0, screen_width - bone_width)

    #4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    bone_rect = bone.get_rect()
    bone_rect.left = bone_x_pos
    bone_rect.top = bone_y_pos

    if character_rect.colliderect(bone_rect):
        print("충돌했어요")
        running = False

    #5.화면에 그리기
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(bone, (bone_x_pos, bone_y_pos))
        
    pygame.display.update() #게임화면을 다시 그리기!


#pygame 종료
pygame.quit()

