import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ids = orders['customerId']
    output = customers[~ customers['id'].isin(ids)]
    output.rename(columns = {'id':'id','name':'Customers'},inplace=True)
    return output[['Customers']]
