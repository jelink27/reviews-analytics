data = []

count = 0 #變數 計數器
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        #print(len(data)) #每讀一行就把長度印出來 但print很花時間 讀取時間會比較長
        count += 1 # count =count + 1
        if count % 1000 == 0: # %是一種運算符號 求餘數的意思
            print(len(data))
        
print('檔案讀取完了，一共有', len(data), '筆資料')
print(data[0])
print('--------------')
print(data[1])

#========
#這一百萬筆的留言平均長度是多少
sum_len = 0 #初始等於0

for d in data: #每一筆資料叫d 每個d是一個字串
    sum_len += len(d) # 等於sum_len = sum_len + len(d)
    #讀第一筆的時候把留言長度加回到sum_len裡面存回去
print('平均是', sum_len/len(data)) # 總長度/留言數 就是留言的平均長度

#========

new = [] #新的清單
for d in data:
    if len(d) < 100: #長度小於100
        new.append(d) #把D裝進new清單
print('一共有', len(new), '筆清單')

#========

good = [] #留言中提及good
for d in data:
    if 'good' in d:
        good.append(d)
print(good[0])
print('一共有', len(good),'筆留言提到good')
