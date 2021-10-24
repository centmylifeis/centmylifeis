import random
answer=random.randrange(1,101,1)
guess=-1
t_cnt=0
print("1~100 숫자 Up&Down 게임을 시작합니다 !")
while guess!=answer:
    guess=int(input("예상되는 숫자를 입력해주세요:"))
    if guess>answer:
        print("down")
    elif guess<answer:
        print("up")

    t_cnt+=1
print("맞았어요",t_cnt,"번만에 맞췄네요.")
