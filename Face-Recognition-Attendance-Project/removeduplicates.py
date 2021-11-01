import pandas as pd

df = pd.read_csv('Attendance.csv')

new_df = df[['Name','Time']].drop_duplicates()

new_df.to_csv('out.csv', index=False)