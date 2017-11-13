# coding:utf-8
import os
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

cf_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"config/mail.ini")
cf = configparser.ConfigParser()
cf.read(cf_path)
f_user = str(cf["mailserver"]["f_user"])
t_user = str(cf["mailserver"]["t_user"])
pwd = str(cf["mailserver"]["pwd"])
port = int(cf["mailserver"]["port"])
smtpserver = str(cf["mailserver"]["smtpserver"])
directory_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
result_path = os.path.join(directory_path,"report/result.html")

def sendmail():

    with open(result_path,'rb') as f:result_data = f.read()
    msg = MIMEMultipart()
    body = result_data
    att = MIMEText(body,'html','utf-8')
    msg.attach(att)
    msg['from'] = f_user
    msg['to'] = t_user
    msg['subject'] = '自动化测试报告'

    att2 = MIMEText(result_data,'base64','utf-8')
    att2["Content-Type"] = "application/octet-stream"
    att2["Content-Disposition"] = 'attachment; filename="result.html"'
    msg.attach(att2)

    smtp = smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(f_user,pwd)
    smtp.sendmail(f_user,t_user,msg.as_string())
    smtp.quit()
if __name__ == '__main__':
    sendmail()