zoo = ['bear', 'dog', 'dolphin', 'elephant', 'fox', 'lion',             #建造一個dictionary
'lollipop', 'penguin', 'potato', 'polar bear', 'snake', 'tiger']
del zoo[6], zoo[7]                                                      #delete掉lollipop之後會重新排列 所以potato會變第8個
zoo.insert(6,"monkey")                                                  #把要加入的字串插入到想要的位置上
zoo.insert(9,"seal")
print(zoo)