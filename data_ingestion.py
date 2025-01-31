import pandas as pd
import glob

# Get a list of all CSV files in the player stats
player_list = glob.glob("data/player_stats/*.csv")

# Create an empty dataframe to store the merged data
merged_df = pd.DataFrame()

# Loop through each file, read it into a dataframe, and append it to the merged dataframe
for file in player_list:
    df = pd.read_csv(file)
    merged_df = pd.concat([merged_df, df], ignore_index=True)

merged_df.set_index("Year", inplace = True)
    
merged_df.to_csv("data/player_stats/merged2000-2024.csv")


advanced_list = glob.glob("data/advanced_stats/*.csv")

print(advanced_list)

# merged_df2 = pd.DataFrame()

# for files in advanced_list:
#     df2 = pd.read_csv(files)
#     merged_df2 = pd.concat([merged_df2, df2], ignore_index=True)

# print(merged_df2)

# merged_df2.set_index("Year", inplace = True)
    
# merged_df2.to_csv("data/advanced_stats/merged2000-2024.csv")