import re
file = open("wifi_log.txt")             #打開檔案
content = file.read()
values = re.findall(r"inputEAPOLFrame: Received non-key EAPOL frame\s\((..)\)", content)    #用regular expression找出所有數值
count, total = 0, 0
for num in values:              #用迴圈讓計算數值加總和次數
    total += int(num)
    count += 1
print("average of the received non-key EAPOL frames:",(total/count).__round__(3))       #印出平均到小數點後三位
#2
Addr = re.findall(r"IP:\s(.*?)\\", content)                 #找到兩種形式的值存到Addr
Addr.extend(re.findall(r"IPV4 Addr:\s(.*?)\\", content))
IP = {}
IP = IP.fromkeys(Addr)                  #把值存到IP的key
for ip in Addr:
    IP[ip] = Addr.count(ip)             #用迴圈把IP的value換成次數
print(IP)

