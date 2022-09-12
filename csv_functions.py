import csv

header = ['name', 'surname','phone no', 'type', 'balance' , 'mins', 'sms', 'gb', 'pass']
data = [['desimir', 'dimovic','0655555', 0, 0, 0, 0, 0,'123'], ['petar', 'pertovic','0654444', 1, 0, 11, 12, 3,'123'], ['petar', 'pertovic','0653333', 0, 1000, 0, 0, 0,'123']]

filename = 'user_data.csv'
def write_csv(header,data):
    with open(filename, 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        csvwriter.writerows(data)

def get_data_from_csv():
    with open(filename,'r') as file:
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)
        
        rows = []
        for row in csvreader:
            rows.append(row)

    return header,rows


#write_csv(header,data)
