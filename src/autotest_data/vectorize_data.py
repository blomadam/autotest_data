import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline, FeatureUnion
from autotest_data.helper_functions import SampleExtractor, DenseTransformer

def vectorize_datasets():
    df = pd.read_csv("../data/00raw/main_table.csv.gz")
    kw_df = pd.read_csv("../data/00raw/keywords_table.csv.gz")

    # filter data for only complete studies (final enrollment)
    df = df[df["completion_date_type"]=="Actual"]
    kw_df = kw_df[kw_df["nct_id"].isin(df["nct_id"].unique())]

    # Vectorize the keywords database
    cvec = CountVectorizer(
        stop_words="english",
        max_features=50,
        ngram_range=(1,3),
        binary=True,
    )
    cvec.fit(kw_df["name"])
    X = pd.DataFrame(
        cvec.transform(kw_df["name"]).todense(),
        columns=cvec.get_feature_names_out()
    )
    # remove index from kw_df version since filtered rows won't match X index
    X["nct_id"] = kw_df["nct_id"].values
    X = X.groupby("nct_id").sum()
    X.to_csv("../../data/01interim/keywords_table_vectorized.csv.gz",index=False)


    # create a pipeline to convert text columns to token count columns
    # Using simple counts to be safe with no train/test split
    binary = False
    feats = 50


    def text_pipeline(column_name, binary_flag, max_feats):
        return Pipeline([
                          ('text',SampleExtractor([column_name])),
                          ('dummify', CountVectorizer(binary=binary_flag,
                                                      max_features=max_feats,
                                                      stop_words="english")),
                          ('densify', DenseTransformer()),
                         ])


    pipeline = Pipeline([
        ('features', FeatureUnion([
            ('brief_title', text_pipeline("brief_title", binary, feats)),
            ('official_title', text_pipeline("official_title", binary, feats)),
            ('description', text_pipeline("description", binary, feats)),
            ('cont_features', Pipeline([
                          ('continuous', SampleExtractor(['nct_id','enrollment'])), # potential bug when extracting single column
                          ])),
            ])),
    ])
    # learn the vocabularies for each column
    pipeline.fit(df)

    # create column headers from vocabularies
    col_names = []
    col_names.extend(["brief_title_" + col for col in pipeline.steps[0][1].transformer_list[0][1].steps[1][1].get_feature_names_out()])
    col_names.extend(["official_title_" + col for col in pipeline.steps[0][1].transformer_list[1][1].steps[1][1].get_feature_names_out()])
    col_names.extend(["description_" + col for col in pipeline.steps[0][1].transformer_list[2][1].steps[1][1].get_feature_names_out()])
    col_names.extend(["nct_id", "enrollment"])

    # generate transformed data_frame
    X = pd.DataFrame(pipeline.transform(df), columns=col_names)
    X.to_csv("../../data/01interim/main_table_vectorized.csv.gz",index=False)


if __name__ == "__main__":
    vectorize_datasets()
