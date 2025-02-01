import pandas as pd
import glob

def merge_csv_files(path, output_file):
    """
    Merges all CSV files from the given path into one DataFrame and saves it to a new CSV file.
    
    Parameters:
    - path: str, path to the directory containing the CSV files.
    - output_file: str, outputs the merged CSV file.
    """
    # Get a list of all CSV files in the path
    file_list = glob.glob(f"{path}/*.csv")
 
    # Loop through each file, read it into a dataframe, and append it 
    dfs = []
    for file in file_list:
            df = pd.read_csv(file)
            dfs.append(df)
    
    # Merge the dataframes, set index as year, and save it 
    merge_df = pd.concat(dfs, ignore_index=True)
    merge_df.set_index("Year", inplace=True)      
    merge_df.to_csv(output_file)

merge_csv_files("data/player_stats", "data/player_stats/merge2000-2024.csv")
merge_csv_files("data/advanced_stats", "data/advanced_stats/merge2000-2024.csv")
merge_csv_files("data/team_stats", "data/team_stats/merge2000-2024.csv")