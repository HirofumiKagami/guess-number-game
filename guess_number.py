import random

print("Guess the Number Game")

min_num = int(input("最小の数を入力してください"))
max_num = int(input("最大の数を入力してください"))

while min_num > max_num:
    print("最小値は最大値以下である必要があります。")
    min_num = int(input("最小の数を入力してください"))
    max_num = int(input("最大の数を入力してください"))

answer = random.randint(min_num,max_num)

while True:
    guess = int(input("数字を予想してください: "))
    if guess == answer:
        print("正解です！")
        break
    elif guess < answer:
        print("もっと大きい数字です")
    else:
        print("もっと小さい数字です")