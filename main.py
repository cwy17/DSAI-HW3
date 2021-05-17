if __name__ == '__main__':
    import csv
    import numpy as np
    import pandas as pd
    import datetime
    def Agent(bidresult,consumption,generation):
        #開啟 CSV 檔案
        consumption_value = 0.0
        generation_value = 0.0
        today = ''
        with open(consumption, newline='',encoding="utf-8") as csvfile:
            # 讀取 CSV 檔案內容
            rows = csv.reader(csvfile)
            index1 = 0
            for row in rows:
                if(index1 > 0):
                    consumption_value = consumption_value + float(row[1:2][0])
                    today = row[0:1][0].split()
                    today = today[0]
                index1 = index1 + 1
            # print(consumption_value/168)
            # print(today)
        with open(generation, newline='',encoding="utf-8") as csvfile:
            rows = csv.reader(csvfile)
            index2 = 0
            for row in rows:
                if(index2 > 0):
                    generation_value = generation_value + float(row[1:2][0])
                index2 = index2 + 1
            # print(generation_value/168)
        with open('Output.csv', 'w', newline='',encoding="utf-8") as csvfile1:   #X_train
            # 建立 CSV 檔寫入器
            writer = csv.writer(csvfile1)
            writer.writerow(['time','action','target_price','target_volume'])
            today = today.replace("/", " ")
            today = today.split(' ')
            date = datetime.datetime(int(today[0]),int(today[1]),int(today[2])) + datetime.timedelta(days=1)
            date = str(date)
            date = date.split(' ')
            date = date[0]
            date = date.replace("-", "/")
            # print(date)
            writer.writerow([date,'buy',2.5,round(generation_value/168,2)])
            writer.writerow([date,'sell',3,round(consumption_value/168,2)])
    Agent('bidresult.csv','consumption.csv','generation.csv')