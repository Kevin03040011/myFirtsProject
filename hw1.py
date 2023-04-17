#設定tuple,list
issue_tuple = ("烏俄戰爭", "還稅於民", "台海和平", "全球暖化", "通貨膨脹")
score_list = [[0 for i in range(10)]for j in range(5)]
title = ["議題／分數｜1 2 3 4 5 6 7 8 9 10｜平均"]

#輸入主程式
times = 0
while True:
    print("請您協助提供您對下列議題的寶貴意見，給分從1（最重要）到10（最不重要）。")
    for i in range(len(issue_tuple)):
        score = int(input(str(i+1)+". 請問您對"+str(issue_tuple[i])+"的看法是："))
        score_list[i][score-1] += 1
    print("謝謝您的寶貴意見!") 
    yesOrNo = int(input("是否進行下一位使用者的問卷調查 (1: Yes; 2:No) "))
    if yesOrNo == 1:
        times += 1
        continue
    else:
        times+=1
        break

#算平均
sum_lsit = []
averageScore = []
for column in range(5):
    sum = 0
    for row in range(10):
        sum += score_list[column][row]*(row+1)
    sum_lsit.append(sum)
    average = round(sum/times,2)
    averageScore.append(average)

#印表格
for word in title:
    print(word)
print("－"*20)
for column in range(5):
    print(issue_tuple[column]+"　｜", end='')
    print(str(score_list[column][0]), end='')
    for row in range(1,10):
        print(" "+str(score_list[column][row]), end='')
    print(" ｜"+str(averageScore[column]))
    print("－"*20)

#找最高最低分
max = max(sum_lsit)
maxIndex = [x for x in range(5) if sum_lsit[x] == max]
min = min(sum_lsit)
minIndex = [x for x in range(5) if sum_lsit[x] == min]
if len(maxIndex) == len(minIndex) == 5:
    print("全部議題皆同分，總分為："+str(sum_lsit[0]))
else:
    for index in maxIndex:
        print("最高分的議題為："+issue_tuple[index]+" 總分為："+str(sum_lsit[index]))
    for index1 in minIndex:
        print("最低分的議題為："+issue_tuple[index1]+" 總分為："+str(sum_lsit[index1]))