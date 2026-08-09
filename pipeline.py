import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

# Stops column names from being truncated when printed to terminal
pd.options.display.max_columns = None
pd.options.display.max_rows = None

url = 'https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv.gz'

engine = create_engine('postgresql://root:root@localhost:5432/open_food')

# Extraction
def extract_csv(url, nrows=None):       
    df_iter = pd.read_csv(
        url, 
        sep='\t',
        nrows=nrows,
        iterator=True,
        low_memory=False,
        chunksize=100000
        )
    
    for df_chunk in tqdm(df_iter):
        df_chunk.to_sql(name='open_food', con=engine, if_exists='replace');
    
    return df_iter

# Transform original dataframe to only include certain fields: foods from Australia only, etc.
def transform_dataframe(Dataframe):
    return None

# Load open food df into Postgres DB.
def load_df_to_database(Dataframe):
    for df_chunk in tqdm(Dataframe):
        df_chunk.to_sql(name='open_food', con=engine, if_exists='replace');

def main():
    
    # open_food_df_iter = 

    extract_csv(url, 300000)

    # open_food_dataframe = pd.concat(open_food_df_iter, ignore_index=True)

    # open_food_df = transform_dataframe(open_food_df)

    # load_df_to_database(open_food_df_iter)

    # open_food_columns_list = open_food_dataframe.columns.tolist()

    # for column in open_food_columns_list:
        # print(column)

    print("Finished")

    # open_food_df.to_csv('output.csv', index=False)

if __name__ == "__main__":
    main()

