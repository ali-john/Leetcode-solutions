import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views.drop_duplicates(subset = ['article_id','author_id','viewer_id','view_date'],inplace=True)
    filtered_data = views[views['author_id']==views['viewer_id']]
    filtered_data.sort_values(by = 'author_id',inplace=True)
    filtered_data.drop_duplicates(subset = ['author_id'],inplace=True)
    filtered_data.rename(columns = {'author_id':'id'},inplace=True)
    return filtered_data[['id']]
