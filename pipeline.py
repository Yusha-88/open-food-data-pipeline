import pandas as pd

# Stops column names from being truncated when printed to terminal
pd.options.display.max_columns = None
pd.options.display.max_rows = None

url = 'https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv.gz'

# Extraction
def extract_csv(url, nrows=None):       
    open_food_df = pd.read_csv(
        url, 
        sep='\t',
        nrows=nrows,
        low_memory=False
        )
    return open_food_df

# Transform original dataframe to only include certain fields: foods from Australia only, etc.
def transform(Dataframe):
    return None

# Load open food df into Postgres DB.
def load(Dataframe):
    return None

if __name__ == "__main__":

    open_food_df = extract_csv(url, 100000)

    open_food_df = transform(open_food_df)

    # open_food_columns_list = open_food_df.columns.tolist()

    # for column in open_food_columns_list:
    #     print(column)

    open_food_df.to_csv('output.csv', index=False)