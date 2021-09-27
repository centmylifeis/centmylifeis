#초단위의 시간을 받아서 ~시간 ~분 ~초인지를 계산하여 봅니다
a=int(input("계산할 초를 입력하세요"))
hours=a//3600
x=a-(hours*3600)
minute=x//60
sec=x-minute*60
print(a,"초를 계산하면",hours,"시",minute,"분",sec,"초 입니다")
