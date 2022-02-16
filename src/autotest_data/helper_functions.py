from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd


class ModelTransformer(BaseEstimator, TransformerMixin):
    """Allows passing models as arguments in pipelines (for grid search)"""
    def __init__(self, model=None):
        self.model = model

    def fit(self, *args, **kwargs):
        self.model.fit(*args, **kwargs)
        return self

    def transform(self, X, **transform_params):
        return self.model.transform(X)


class SampleExtractor(BaseEstimator, TransformerMixin):
    """Takes in varaible names as a **list** - returns Series for single entry list, otherwise DataFrame"""

    def __init__(self, vars):
        self.vars = vars  # e.g. pass in a column names to extract

    def transform(self, X, y=None):
        if len(self.vars) > 1:
            return pd.DataFrame(X[self.vars])  # where the actual feature extraction happens
        else:
            return pd.Series(X[self.vars[0]])

    def fit(self, X, y=None):
        return self  # generally does nothing


class DenseTransformer(BaseEstimator, TransformerMixin):
    """converts sparse matrix from vectorizer into dense matrix for pandas / modeling"""
    def transform(self, X, y=None, **fit_params):
        #         print X.todense()
        return X.todense()

    def fit_transform(self, X, y=None, **fit_params):
        self.fit(X, y, **fit_params)
        return self.transform(X)

    def fit(self, X, y=None, **fit_params):
        return self