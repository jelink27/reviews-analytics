data = []
count = 0 #變數 計數器
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        #print(len(data)) #每讀一行就把長度印出來 但print很花時間 讀取時間會比較長
        count += 1 # count =count + 1
        if count % 1000 == 0:
            print(len(data))
        
print(len(data))
print(data[0])
print('--------------')
print(data[1])