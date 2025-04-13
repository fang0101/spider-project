import requests
import csv

url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY"
params = {
    "response": "json",
    "date": "20240401",  
    "stockNo": "2330"    # 台積電代號
}

response = requests.get(url, params=params)
data = response.json()

if data["stat"] == "OK":
    rows = data["data"]
    with open("tsmc_202404.csv", mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["日期", "成交股數", "成交金額", "開盤價", "最高價", "最低價", "收盤價", "漲跌", "成交筆數"])
        writer.writerows(rows)
    print("儲存 tsmc_202404.csv")