data = []
count = 0
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print("loading完了,トータル", len(data), "コメントあります。")

sum_len = 0
for d in data:
	sum_len += len(d)
print("平均コメントの長さは", sum_len/len(data))