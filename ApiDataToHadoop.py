import csv
import requests
import os

from dotenv import load_dotenv
load_dotenv('.env')

key = os.getenv('API_KEY')
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year2month2&apikey=https://mail.google.com/mail/u/0/#sent/QgrcJHsHmZfQrMxXlvMwnVRvfjPcnhXZhVq'
with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)
