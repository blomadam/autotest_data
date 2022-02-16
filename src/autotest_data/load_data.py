import pandas as pd
import configparser
import psycopg2


def collect_data(
        study_filter_start: str ='2018-06-01',
        study_filter_end: str = '2018-06-30'
) -> None:
    """
    Connect to AACT database and download two files to data/00raw directory as *.csv.gz.
    main_table.csv.gz has the studies with start_date between given dates (inclusive)
    keywords_table.csv.gz has the keywords listed for the selected studies
    :return:
    """

    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    config.read('credentials.ini')
    connection_string = config["passwords"]["aact_db_connection_string"]
    with psycopg2.connect(connection_string) as conn:
        # collect main data table
        df = pd.read_sql(
            sql=f"""
                select s.nct_id, s.start_date, s.verification_date, s.completion_date, s.completion_date_type,
                s.study_type, s.brief_title, s.official_title, b.description, s.enrollment, s.enrollment_type
                from studies as s
                join brief_summaries as b on s.nct_id = b.nct_id
                where (start_date >= '{study_filter_start}' AND
                   start_date <= '{study_filter_end}')
                order by nct_id;
            """,
            con=conn,
        )
        df.to_csv("data/00raw/main_table.csv.gz", index=False)

        # collect keywords table
        df = pd.read_sql(
            sql=f"""
                select nct_id, name
                from keywords
                where nct_id in (
                    select nct_id
                    from studies
                    where (start_date >= '{study_filter_start}' AND
                        start_date <= '{study_filter_end}')
                )
                order by nct_id;
            """,
            con=conn,
        )
        df.to_csv("data/00raw/keywords_table.csv.gz", index=False)



def load_data(x: float) -> float:
    main_df = pd.read_csv("data/00raw/main_table.csv.gz")
    keyword_df = pd.read_csv("data/00raw/keywords_table.csv.gz")
    return main_df, keyword_df


if __name__ == "__main__":
    collect_data()