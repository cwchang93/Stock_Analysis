#測試CSV檔案開啟
import csv
csv_file = '/Users/cwchang/Desktop/test.csv'
out_csv = csv.writer(open(csv_file, 'w'))
