import csv  
  
# 打开文件并读取数据  
with open('C:\\Users\\93541\\Desktop\\作业\\数据库\\一带一路\\data.txt', 'r') as file:  
    reader = csv.reader(file, delimiter='\t')  
    data = [row for row in reader]  
print(data)
# 删除 '[' 后的内容并重新组合数据  
# 遍历列表中的每个子列表  
for sublist in data:  
    # 遍历子列表中的每个字符串  
    for i in range(len(sublist)):  
        # 去除字符串中后四个字符  
        sublist[i] = sublist[i][:-4]  

print(data)

with open('new_file.csv', 'w', newline='') as f:  
    writer = csv.writer(f)  
    # 写入数据  
    for row in data:  
        writer.writerow(row)