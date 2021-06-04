import requests
import json
import xlrd
import pymysql

def header():
    header = {'Content-Type': 'application/json'}
def token_header():
    header = {'Content-Type': 'application/json'}
    con_url = 'http://172.18.1.143:8888/admin/login/verify'
    con_body = {"captcha": "999999",  # 验证码999999
                "phone": "17633607554"}  # 此处phone应该是上面获取到的phone
    Confirm_login = requests.post(headers=header, url=con_url, data=json.dumps(con_body))
    # Authorization = 'Admin ' + Confirm_login.text.split('"')[7]
    token_header = {'Content-Type': 'application/json','Authorization': 'Admin eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaG9uZSI6IjE3NjMzNjA3NTU0IiwiaWQiOjIsInBhc3N3b3JkIjoiMjI0Y2YyYjY5NWE1ZThlY2FlY2ZiOTAxNTE2MWZhNGIiLCJleHAiOjE2MTkyMjgzMzMsImlzcyI6ImdvIHdlYiB0ZW1wbGF0ZSJ9.NcEk7NrD305NEXD2sPqH-RgEIeIL_jyJh7YFYe3fWv0'}
    # token_header = {'Content-Type': 'application/json','Authorization':Authorization}
    return token_header
def commect_table(row,clo):
    data = xlrd.open_workbook(r'/Users/dingyanpan/Desktop/私有云接口自动化/数据管理.xls')
    data.sheet_names()
    table = data.sheet_by_name('Sheet1')
    list = table.cell_value(row,clo)
    return list