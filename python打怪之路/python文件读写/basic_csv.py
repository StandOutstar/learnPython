import csv

question = []
answer = []

with open("newdata.csv", "r", encoding="utf-8") as csvfile:
    # 读取csv文件，返回的是迭代类型
    read = csv.DictReader(csvfile)
    for i in read:
        question.append(i['question'])
        answer.append(i['answer'])
    print(question)
    print(answer)