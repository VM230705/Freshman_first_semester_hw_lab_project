while True:                                             # 為了讓使用者輸入兩次
    try:
        file = open(input("Enter the file name: "))     # 用try和except讓使用者輸入檔案
        break  # 若檔案找的到就break
    except FileNotFoundError:
        print("Wrong file name")                        # 若找不到則用continue重跑迴圈
        continue
content = file.readlines()                              # 用readlines把string變成list

hours = []
for line in content:                                    #每次讀一行若找到From則split掉空白
    if line.startswith("From"):
        line = line.split(" ")
        if len(line) > 4:                               #為了區別其他From開頭的句子
            time = line[6].split(":")                   #取出小時的部分
            hours.append(time[0])
hours.sort()        #讓小時list照順序排
temp = ""
for hour in hours:                          #若temp==hour代表重複處理過了就不執行進入下一次迴圈
    if hour != temp:
        print(hour, hours.count(hour))      #印出 小時和 次數
    temp = hour
