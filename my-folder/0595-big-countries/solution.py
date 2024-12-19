import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_country = world[(world['area']>=3000000) | (world['population']>=25000000)]
    return big_country[['name','population','area']]
