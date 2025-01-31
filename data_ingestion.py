import pandas as pd
import glob

# Get a list of all CSV files in the specified directory
file_list = glob.glob("data/player_stats/*.csv")

# Create an empty dataframe to store the merged data
merged_df = pd.DataFrame()

# Loop through each file, read it into a dataframe, and append it to the merged dataframe
for file in file_list:
    df = pd.read_csv(file)
    merged_df = pd.concat([merged_df, df], ignore_index=True)

merged_df.set_index("Year", inplace = True)
    
merged_df.to_csv("data/player_stats/merged2000-2024.csv")