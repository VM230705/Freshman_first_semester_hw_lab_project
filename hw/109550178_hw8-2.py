import re               #為了一次split多個符號
j = 0
while j < 2:            #為了讓使用者輸入兩次
    while True:
        try:                                                            #用try和except讓使用者輸入檔案
            file = open(input("Enter the file name: "))                 #若檔案找的到就break
            break
        except FileNotFoundError:
            print("Wrong file name")                                    #若找不到則用continue重跑迴圈
            continue
    content = file.readlines()                                          #用readlines把string變成list
    i, count = 0, 0                                                     #定義變數
    while True:
        if i >= len(content):                                           #若i超過list裡面元素的數量就break
            break
        if content[i].startswith("Subject: [sakai] svn commit:"):       #用startswith找到字串回傳true或false
            pos = re.split(" |: |- |/", content[i])                     #用pos存split過後的list
            if pos[6] == "in":                                          #若第7個元素==in就輸出第5和第8個元素
                print(pos[4], pos[7])
            else:                                                       #其餘則輸出第5個和第7個元素
                print(pos[4], pos[6])
            count += 1                                                  #count計算次數
        i += 1
    print("There were ", count, " subject lines")
    j += 1