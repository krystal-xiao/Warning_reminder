import os,time,logging
import hmac,hashlib,base64
from urllib.parse import quote
import config

dingding_config = config('dingding') # 取钉钉的配置文件
secret_authen = dingding_config.get("secret")

def create_sign():
    secret = secret_authen
    timestamp = int(time.time() * 1000)
    sign_before = '&s\%n%s' % (timestamp,secret)
    hsha265 = hmac.new(secret.encode(),sign_before.encode(),hashlib.sha256())
    sign_sha256 =hsha265.digest()
    sign_b64 = base64.b64encode(sign_sha256)
    sign = quote(sign_b64)
    return {"timestamp":timestamp,"sign":sign}

def spaceMonitorJob():
    '''当磁盘（切片存储的目录）利用率超过90%，程序退出：return'''
    try:
        st = os.statvfs('/')
        # f_blocks:文件系统数据块总数；f_frsize: 分栈大小
        total = st.f_blocks * st.f_frsize
        # f_bfree: 可用块数；f_frsize: 分栈大小
        used = (st.f_blocks-st.f_bfree) * st.f_frsize

    except FileNotFoundError:
        print('check webroot space error')

def analyze(self,data):
    arr = data.split('\n')
    i = 1
    format_data = []
    for row in arr:
        if(i==1):
            i+=1
            continue
        data_row = []
        row_arr = row.split('')
        for item in row_arr:
            if(item == ''):
                continue
            data_row.append(item)
            if(len(data_row) > 0):
                format_data.append(data_row)
    return format_data


if __name__ == '__main__':
    connect = create_sign()