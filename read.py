data = []
count = 0
with open ('reviews.txt','r') as f :
	for line in f :
		data.append(line)
		count += 1
		if count % 10000 == 0 :
			print(len(data))
print("檔案讀取完了共有",len(data),"筆資料")


sum_len = 0
for d in data :
	sum_len = sum_len + len(d)

print ("留言的平均長度為:",sum_len/len(data))

new = []
for d in data :
	if len(d) < 100 :
		new.append(d)
print("一共有", len(new),"筆長度小於100")
print(new[0])
print(new[1])


#文字記數

wc = {} #word_count
num = 0
for d in data :
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進字典

for word in wc:
	if wc[word] >100:
		print(word, wc[word])

print(len(wc))
while True:
	word = input("請輸入想查找的字:")
	if word == "q":
		print("881")
		break
	if word in wc:
		print(word, "出現過的次數為", wc[word])
	else:
		print("這個字沒有出現過喔")
	




