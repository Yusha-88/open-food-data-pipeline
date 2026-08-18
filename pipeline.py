import pandas as pd
from sqlalchemy import create_engine, Text
from tqdm.auto import tqdm

# Stops column names from being truncated when printed to terminal
pd.options.display.max_columns = None
pd.options.display.max_rows = None

url = 'https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv.gz'

# Postgres parameters
pg_user = 'root'
pg_pass = 'root'
pg_host = 'localhost'
pg_port = 5432
pg_db = 'open_food'

engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

# Removing nutriscore and environmental score since they have invalid text entries in them.
relevant_cols = [
    "product_name",
    "generic_name",
    "brands",
    "origins",
    "countries",
    "allergens",
    # "nutriscore_score",
    "nutriscore_grade",
    "brand_owner",
    # "environmental_score_score",
    "environmental_score_grade",
    "energy-kcal_100g",
    "energy_100g",
    "fat_100g",
    "saturated-fat_100g",
    "trans-fat_100g",
    "cholesterol_100g",
    "carbohydrates_100g",
    "sugars_100g",
    "added-sugars_100g",
    "fiber_100g",
    "proteins_100g",
    "salt_100g",
    "added-salt_100g"
]

# Using this to see where 'en:italy' error happens in a column. The error is in the nutriscore_grade column
testing_cols = [
    "nutriscore_score",
    "nutriscore_grade",
    "brand_owner",
    "environmental_score_score",
    "environmental_score_grade",
]

# Extraction
def extract_transform_csv(url, nrows=None):
    print("Starting...")       
    df_iter = pd.read_csv(
        url, 
        sep='\t',
        nrows=nrows,
        usecols=relevant_cols,
        iterator=True,
        low_memory=False,
        chunksize=100000
        )
    return df_iter

# Load open food df into Postgres DB.
def load_df_to_database(Dataframe):
    for df_chunk in tqdm(Dataframe):
        try:
            df_chunk.to_sql(name='open_food', con=engine, if_exists='append')  
        except pd.errors.DatabaseError:
            pass

def main():
    num_rows_to_extract = 1000000  
    open_food_df = extract_transform_csv(url)
    load_df_to_database(open_food_df)
    print("Finished")

    # open_food_df.to_csv('output.csv', index=False)

if __name__ == "__main__":
    main()

