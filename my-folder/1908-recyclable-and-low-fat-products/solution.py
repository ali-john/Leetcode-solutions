import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    ids = products[(products['low_fats']=='Y') & (products['recyclable']=='Y')]
    return ids[['product_id']]
