#fnGuide에서 재무장보 가지고 오는 소스

import pandas as pd
import requests
from tabulate import tabulate

pd.set_option("display.expand_frame_repr", False)

fs_url='https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=D&NewMenuID=11&stkGb=&strResearchYN='
fs_page= requests.get(fs_url)
fs_table = pd.read_html(fs_page.text)

'''
for i,df in enumerate(fs_table):
    print(f"데이터프레임 {i+1}:")
#    print(df, "\n")  # 개행 추가  1안
    print(tabulate(df, headers="keys", tablefmt="psql")) #2안
'''

#temp_df = fs_table[0]

#temp_df = fs_table[['1','2','3']]


temp_df = fs_table[11]
temp_df = temp_df.set_index('IFRS(연결)')
#print(temp_df.columns)
print(temp_df.axes)

temp_df = temp_df[[('Annual', '2022/12'),('Annual', '2023/12'),('Annual', '2024/12'),('Annual', '2025/12(E)')]]
#temp_df = temp_df[[temp_df.columns[0],temp_df.columns[1],temp_df.columns[2],temp_df.columns[3]]] #성공

temp_df=temp_df.loc[[('매출액',),('영업이익',),('당기순이익',),('자산총계',),('부채총계',),('자본총계',)]]
print(tabulate(temp_df, headers="keys", tablefmt="psql"))

temp_df1 = fs_table[9]