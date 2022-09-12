import csv_functions as cf
from fpdf import FPDF


class Prices:
    price_min = 10
    price_sms = 1
    price_gb = 100



class User:
    def __init__(self,name,surname,phone_no):
        self.name = name
        self.surname = surname
        self.phone_no = phone_no

    def __init__(self,phone_no):
        header, rows = cf.get_data_from_csv()
        for row in rows:
            if row[2] == phone_no:
                self.surname = row[1]
                self.name = row[0]
                self.phone_no = phone_no
    

class Phone:
    def __init__(self,phone_no,type,balance,min_spent,sms_spent,gb_spent):
        self.phone_no = phone_no
        self.type = type  # 0 pripejd 1 postpaid
        self.balance = balance
        self.min_spent = min_spent
        self.sms_spent = sms_spent
        self.gb_spent = gb_spent

    def __init__(self,phone_no):
        header, rows = cf.get_data_from_csv()
        for row in rows:
            if row[2] == phone_no:
                self.phone_no = phone_no
                self.type = row[3]
                self.balance = row[4]
                self.min_spent = row[5]
                self.sms_spent = row[6]
                self.gb_spent = row[7]
    def check_balance(self):
        if int(self.type)==0:
            return self.balance
        else:
            return 'Ova mogucnosti je moguca samo za pripejd korisnike.'

    def print_pdf(self):
        if int(self.type) == 1:
            total = float(self.min_spent)*Prices.price_min + float(self.sms_spent)*Prices.price_sms + float(self.gb_spent)*Prices.price_gb
            total_txt = 'Vas ukupan racun je ' + str(total) + ' RSD'
            min_txt = 'Portrosili ste ' + str(self.min_spent) + ' minuta, po ceni od ' + str(Prices.price_min) + ' RSD po minutu'
            sms_txt = 'Portrosili ste ' + str(self.sms_spent) + ' poruka, po ceni od ' + str(Prices.price_sms) + ' RSD po poruci'
            gb_txt = 'Portrosili ste ' + str(self.gb_spent) + ' gigabajta interneta, po ceni od ' + str(Prices.price_gb) + ' RSD po gigabajtu'

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size = 15)
            
            pdf.cell(200, 10, txt = "Racun",ln = 1, align = 'C')
            
            pdf.cell(200, 10, txt = min_txt,ln = 2, align = 'L')
            pdf.cell(200, 10, txt = sms_txt,ln = 2, align = 'L')
            pdf.cell(200, 10, txt = gb_txt,ln = 2, align = 'L')
            pdf.cell(200, 10, txt = total_txt,ln = 2, align = 'L')
            
            pdf.output("racun.pdf") 
            return 1
        else:
            return 0

                        
    def send_sms(self):
        if int(self.type) == 0:
            if int(self.balance) < int(Prices.price_sms):
                return 0
            else:
                self.balance = int(self.balance) - Prices.price_sms
                return 1
        else:
            header ,rows = cf.get_data_from_csv()
            for row in rows:
                if row[2] == self.phone_no:
                    row[6] = str(int(row[6]) + 1)
            cf.write_csv(header,data=rows)
            return 1

    def calling(self,min):
        if min < 1:
            if int(self.type) == 0:
                if int(self.balance) < int(Prices.price_min):
                    return 0
                else:
                    self.balance = int(self.balance) - Prices.price_min
                    return 1
            else:
                header ,rows = cf.get_data_from_csv()
                for row in rows:
                    if row[2] == self.phone_no:
                        row[5] = str(int(row[5]) + 1)
                cf.write_csv(header,data=rows)
                return 1
        else:
            for i in range(int(min)):

                if int(self.type) == 0:
                    if int(self.balance) < int(Prices.price_min):
                        return 0
                    else:
                        self.balance = int(self.balance) - Prices.price_min
                        return 1
                else:
                    header ,rows = cf.get_data_from_csv()
                    for row in rows:
                        if row[2] == self.phone_no:
                            row[5] = str(int(row[5]) + 1)
                    cf.write_csv(header,data=rows)
                    return 1

                




