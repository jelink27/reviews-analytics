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


wc = {}  #word_count
for d in data:
    words = d.split(' ') #用空白鍵分割
    print(words)
    for word in words:
        if word in wc:
            wc[word] += 1 #去wc字典中查找word，然後加1                                     
        else:
            wc[word] = 1 #新增新的key進字典 然後次數是1
    break
for word in wc:
    if wc[word] > 2:
        print(word, wc[word]) #把key跟查找次數給印出來 去wc字典中找[word] 會得到數字

print(len(wc))
print(wc['are'])

while True:
    word = input('請問你想查什麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為:', wc[word], '次')
    else:
       print(word, '沒有出現過:')
print('感謝使用本查詢功能')