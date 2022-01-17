article = 'Overturning elections sounds like the stuff of secret deals in '\
          'smoke-filled rooms, but President Donald Trumps not even trying to '\
          'hide his effort to subvert the results of the election as '\
          'President-elect Joe Bidens margin widens to more than 6 million '\
          'votes.Trumps efforts to deny Biden the White House traveled from '\
          'the courts to state legislatures on Friday with Trumps personal '\
          'reception with Republican lawmakers from Michigan -- and their '\
          'counterparts in Pennsylvania may be next on the list. But there '\
          'were signs, even among Republicans, that Trumps efforts need some '\
          'evidence. As legislative leaders, we will follow the law and '\
          'follow the normal process regarding Michigans electors, just as we '\
          'have said throughout this election, Michigan Senate Majority '\
          'Leader Mike Shirkey and Michigan House Speaker Lee Chatfield said '\
          'in a joint statement after their meeting at the White House.'
words = article.split(" ")                              #用split把空白當分隔線存在word這個list
first_letters = []                                      #創建兩個list和一個dictionary
value = []
dict = {}
for word in words:                                      #用迴圈把每個字串的第一個字母存進first_letters這個list
    first_letters.append(word[0])
words.sort(reverse=True)                                #把word排列後印出
print(words)
first_letters.sort(reverse=True)                        #把first_letters排列

for first in first_letters:                             #用迴圈去計算每個字母出現的次數
    value.append(first_letters.count(first))
dict = dict.fromkeys(tuple(first_letters))              #把字首的list存到dict裡的key

i = 0
while True:
    if i >= len(value):                                 #用i防止index超出範圍
        break
    dict[first_letters[i]] = value[i]                   #把dict裡的value替換成list的value
    i += value[i]
print(dict)
