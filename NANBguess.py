def check(ans,guess):
    a = 0
    b = 0
    for i in range(4):
        for j in range(4):
            if ans[i]==guess[j]:
                if i==j:
                    a=a+1
                else:
                    b=b+1
    return a*10+b

def checkRpt(s):
    for i in range(3):
        for j in range(i+1,4):
            if s[i]==s[j]:
                return True
    return False

import random
count = 0 #次數
guess = "" #電腦的答案
ans = 0 #人的回覆幾A幾B
answer=[]
for i in range(123,9877):
    tmp = ""
    if i // 1000 == 0:
        tmp = "0"
    tmp = tmp + str(i)
    if not checkRpt(tmp):
        answer.append(tmp)
while True:
    print("目前答案還有：",len(answer),"個")
    guess = random.choice(answer)
    count += 1
    print(f"第{count}次，我猜的答案是：{guess}")
    ans =int(input("你的回答是："))
    if ans == 40:
        print("我猜對了，答案是：",guess)
        break
    else:
        j = 0
        while (j<len(answer)):
            if check(answer[j],guess)==ans:
                j+=1
            else:
                answer.pop(j)
    if len(answer)==0:
        print("給錯答案了！")
        break

