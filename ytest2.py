import pandas as pd
import os

def make_code(x):
    x=str(x)
    return 'A'+'0'*(6-len(x)) + x

path = r'c:\Users\KRX\source\python\data_4505_20250411.xlsx'
code_data = pd.read_excel(path)

code_data = code_data[['단축코드','한글 종목명']]
code_data['단축코드'] = code_data['단축코드'].apply(make_code)
print(code_data)