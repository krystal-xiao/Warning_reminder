import os,smtplib,commands,time
from email.mime.text import MIMEText
import config
dingding_config = config('dingding')   # 取钉钉的配置信息
mail_config = config('mail')           # 取邮件的配置信息
url = dingding_config.get('url')
access_token = dingding_config.get('access_token')
inform_others = dingding_config.get('at','').split(',')

def send_dingding(msg):
    data = {
        "msgtype": "text",
        "text": {
            "content": msg
        },
        "at":{
            "atMobiles": inform_others,
            "isAtAll": False
        }

    }





# # 邮箱服务器地址,可自定义邮箱服务器
# mailserver = "smtp.126.com"
# # 邮箱用户名和密码
# sender = "krystal_xiao@126.com"
# password = "196203xzh"
# # 收件人
# receiver = 'krystal-xiao@qq.com'
# # 邮件内容
# mail = MIMEText('Disk usage is less than 1T!')
# # 邮件主题
# mail['Subject'] = 'Disk Warning'
# # 发件人
# mail['from'] = sender
# # 收件人
# mail['To'] = receiver
# # 连接邮箱服务器，smtp的端口号是25  (smtp=smtplib.SMTP_SSL('smtp.qq.com',port=465) #QQ邮箱的服务器和端口号)
# smtp = smtplib.SMTP(mailserver,port=25)
# # 登录邮箱
# smtp.login(sender,password)
# # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
# smtp.sendmail(sender,receiver,mail.as_string())
# # 发送完毕后退出smtp
# smtp.quit()

