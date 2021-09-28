r=int(input("반지름을 입력하세요 :"))
h=int(input("높이를 입력하세요 :"))
pi=3.141592

print("="*30)
print("반지름:",r)
print("높이:",h)

volumn=pi*r**2*h
print("부피:",round(volumn,2))
print("부피:","%.2f" %volumn)
