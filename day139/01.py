import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('./data/CDNOW_master.txt',header=None,sep='\s+',names=['user_id','order_dt','order_ct','order_amount'])
df.head()
#查看数据类型
df.info()
df['order_dt'] = pd.to_datetime(df['order_dt'],format='%Y%m%d')
df.head()
#在源数据中添加一列表示月份
df['month'] = df['order_dt'].astype('datetime64[M]')




#每一个用户消费总金额和消费总次数
df.groupby(by='user_id')['order_amount'].sum()
df.groupby(by='user_id')['order_product'].sum()

#各个用户消费总金额的直方分布图(消费金额在1000之内的分布)
user_amount_1000 = df.groupby(by='user_id').sum().query('order_amount <= 1000')['order_amount']



#用户第一次消费的月份分布，和人数统计
#分析：用户消费月份的最小值就是用户第一次消费的月份
df.groupby(by='user_id')['month'].min()


#人数统计
df.groupby(by='user_id')['month'].min().value_counts()


#统计每个用户每个月的消费次数
df_purchase = df.pivot_table(index='user_id',values='order_dt',aggfunc='count',columns='month',fill_value=0)
df_purchase.head()