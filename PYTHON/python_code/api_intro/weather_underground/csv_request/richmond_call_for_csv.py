import csv
import requests
#from contextlib import closing

filename = 'richmond_jan_2018.csv'
CSV_URL = 'http://api.wunderground.com/api/f52d82a80ed10e46/history_20180107/q/VA/Richmond.csv'
download = requests.get(CSV_URL)

with open(filename, 'w') as f:
	f.writelines(download.content)
	
with open(filename, 'rU') as f:
	csv_reader = csv.reader(f, dialect=csv.excel_tab)
	header_row = next(csv_reader)
#	for line in csv_reader:
#		print line
	for index, column_header in enumerate(header_row):
		print(index, column_header)
		
	
#	reader = csv.reader(f)
#	header_row = next(reader)
#	print(header_row)
	
	
#r = requests.get(CSV_URL)

#with closing(requests.get(CSV_URL, stream=True)) as f:
#	reader = csv.reader(f.iter_lines(), delimiter=',')
#	for row in reader:
#		print(row)
	
	#header_row = next(reader)
	#print(header_row)
	
	#for index, column_header in enumerate(header_row):
		#print(index, column_header)	
