f=input("찾고싶은 친구의 이름을 입력하세요 :")
friends=["지연","세현","우리","수지","원정","하나","지원"]

if f in friends:
    print(friends.index(f),f)
else:
    print(f,"은","명단에","없네요...")
    print("추가하시겠습니까?")
    print(input("[예/아니오]:"))
    if "예":
        friends.append(f)
        print(friends)
        
