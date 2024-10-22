import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    new_df = students[students['student_id']==101]
    return new_df[['name','age']]
