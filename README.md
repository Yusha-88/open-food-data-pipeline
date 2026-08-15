# open-food-data-pipeline
A simple ETL pipeline that ingests an Open Food Data CSV into a Postgres database. Uses Python, Docker, and SQL.

### Change log:
15/08/26 - Decided to load 1 million rows of data from original CSV into Postgres.

11/08/26 - Fixed issue where only 100,000 records were uploaded to the database at a time. Using a few select columns from original CSV's 155 columns.

10/08/26 - Setup Postgres DB and extract_csv now can input some data to it.