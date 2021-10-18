def change(m,p):
    change=m-p
    coin500=change//500
    change=change%500
    coin100=change//100
    return(coin500,coin100)

money=int(input("투입한 돈:"))
price=int(input("물건 값:"))
c500,c100=change(money, price)

print("500원 동전의 개수:",c500)
print("100원 동전의 개수:",c100)

#return값이 있을때는 받는 인수가 있어야 한다. 여기에서는 c500=함수 이렇게!!
#없을때는 그냥 바로 change함수써도됨 
#input 안받고 지정할때
'''change(2000,1200)'''

