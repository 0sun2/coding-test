#거스름돈 돌려주기. 그리디

change = int(input())

#동전은 500원 100원 50원 10원
coin = {}
coin["fh_won"] = change//500
change %= 500
coin["oh_won"] = change//100
change %= 100
coin["ft_won"] = change//50
change %= 50
coin["ten_won"] = change//10
change %= 10

print(f'거슬러준 동전의 수는 500원{coin["fh_won"]}개 100원{coin["oh_won"]}개 50원{coin["ft_won"]}개 10원{coin["ten_won"]}개')
#############
#동전 개수 구하기
change = int(input())

coin_list = [500,100,50,10]
count = 0
for i in coin_list:
    coin = change//i
    count += coin
    change %= i

print(count)