00raw/main_table.csv.gz 00raw/keywords_table.csv.gz &:  src/autotest_data/load_data.py
    python src/autotest_data/load_data.py

01interim/main_table_vectorized.csv.gz 01interim/keywords_table_vectorized.csv.gz &:  00raw/main_table.csv.gz 00raw/keywords_table.csv.gz src/autotest_data/vectorize_data.py
    python src/autotest_data/vectorize_data.py
