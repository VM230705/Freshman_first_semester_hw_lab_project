# Lab-10
# Exercise 1
# 'X-DSPAM-Confidence:0.8475'
test_string = "X-DSPAM-Confidence:0.8475"
print(float(test_string[test_string.find(":")+1:]))                  #用find找出字串"0"的位置,再slice string轉成float

# Exercise 2-1
test_data = [
    "1. The lyrics are bad!",
    "2. The lyrics are not bad!",
    "3. The lyrics are not that bad!",
    "4. The lyrics are poor!",
    "5. The lyrics are not poor!",
    "6. The lyrics are not that poor!",
    "7. The lyrics are good!",
    "8. The lyrics are not good!",
    "9. The lyrics are not that good!",
    "10.I'm not sure if he's good."
]

# Exercise 2-2
test_data_2 = [
    "1. I'm not sure he's good.",
    "2. I'm not sure it's a good idea"
]

i = 0
for data in test_data:
    '''
    print('Loop: ', i)
    print('not is at index: ', data.find('not'))
    print('bad is at index: ', data.find('bad'))
    print('poor is at index: ', data.find('poor'))
    print('good is at index: ', data.find('good'))
    '''
    data = data.replace(" ", " ")                                    #把 換成空白
    if data.find('not') > 0:                                            #若字串中找不到"not"會回傳-1 找的到則執行
        if data.find('bad') > 0 or data.find('poor') > 0:               #若字串中找不到"bad"或"poor"會回傳-1 找的到則執行
            data = data.replace(data[data.find('not'):], "good!")       #從not開始後的部分字串都換成"good!"
        elif data.find('sure') > 0:                                     #若字串中找不到"sure"會回傳-1 找的到代表是第10句
            data = data.replace(data[data.find('not'):], "bad.")        #從"not"開始後的部分字串都換成"bad!"
        else:
            data = data.replace(data[data.find('not'):], "bad!")        #其餘的都從"not"開始後的部分字串都換成"bad!"
    print(data)
    i += 1
for data in test_data_2:
    print(data.replace("not ","").replace("good","bad").replace(" ",""))
    #把"not"換成空白,"good"換成"bad"," "換成空白
