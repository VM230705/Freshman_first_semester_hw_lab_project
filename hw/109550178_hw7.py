while True:
    try:                                                    #確保使用者輸入正確的資料型別
        loan = float(input("Enter amount of loan:"))
        break
    except ValueError:                                      #若輸入錯則重跑迴圈
        print("Error! The input should be numbers.")
while True:
    try:                                                    #確保使用者輸入正確的資料型別
        rate = float(input("Enter interest rate:"))
        break
    except ValueError:                                      #若輸入錯則重跑迴圈
        print("Error! The input should be numbers.")
while True:
    try:                                                    #確保使用者輸入正確的資料型別
        payment = float(input("Enter monthly payment:"))
        break
    except ValueError:                                       #若輸入錯則重跑迴圈
        print("Error! The input should be numbers.")
print("Balance remaining after first payment:", round(loan*(1+rate/12/100)-payment, 2) )
#用round讓算出來的float四捨五入到小數點後2位
