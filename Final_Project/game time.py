data = open("nba_schedule").read()
date_dict = data.split(";")
j = 0
for a in date_dict:
    date_dict[j] = a.replace("@ ", "")
    j += 1

date = ""
game_dict = []
while True:
    try:
        year = int(input("Enter year:"))
        month = int(input("Enter month:"))
        day = int(input("Enter day:"))
        expected_date = str(day)+"/"+str(month)+"/"+str(year)
        print(expected_date)
        i, flag = 0, 0
        for date in date_dict:
            date = date.split("\n")

            i += 1
            if expected_date == date[0]:
                game_dict.append((str.upper(date_dict[i-3]),str.upper(date_dict[i-2])))
                flag = 1
        if flag == 0:
            print("The date doesn't have any game")
        else:
            break
    except ValueError:
        print("Wrong Input")
#if flag == 1:
  #  for game in game_dict:


