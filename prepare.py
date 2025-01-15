import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

from env import user, password, host, db, protocol
import os
# from acquire import wrangle_store_data

import warnings
warnings.filterwarnings("ignore")

# plotting defaults
plt.rc('figure', figsize=(13, 7))
plt.style.use('seaborn-whitegrid')
plt.rc('font', size=16)


def prepare_store_data(df):
    df = df.fillna(method='ffill')
    df['sale_date'] = pd.to_datetime(df.sale_date)
    df = df.set_index('sale_date').sort_index()
    df['month']= df.index.month_name()
    df['day_of_week'] = df.index.day_name()
    df['sales_total']= df['sale_amount'] * df['item_price']
    df = df.rename(columns={'sale_amount': 'quantity'})
    return df