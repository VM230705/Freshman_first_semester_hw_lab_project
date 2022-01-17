j = 0
while j < 2:
    while True:             #為了讓使用者輸入兩次
        try:
            file = open(input("Enter the file name: "))         #用try和except讓使用者輸入檔案
            break                                               #若檔案找的到就break
        except FileNotFoundError:
            print("Wrong file name")                            #若找不到則用continue重跑迴圈
            continue
    content = file.readlines()                                  #用readlines把string變成list
    i, count, total = 0, 0, 0                                   #定義變數
    while True:
        if i >= len(content):                                   #若i超過list裡面元素的數量就break
            break
        if content[i].startswith("X-DSPAM-Confidence:"):        #用startswith找到字串回傳true或false
            pos = content[i].split(":")                         #用pos存split分割過後的list
            num = float(pos[1].strip())                         #再用num存 strip去掉空格和轉成float後的數字
            total = total + num                                 #用total計算數字加總 count計算次數
            count += 1
        i += 1
    average = total/count                                       #計算平均
    print("Average spam confidence:", round(average, 12))       #用round四捨五入到小數點後12位
    j += 1