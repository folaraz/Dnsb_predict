import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
from sklearn import cross_validation, metrics
import pickle as pk
import os

import warnings
warnings.filterwarnings('ignore')

CUR_PATH = os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1])

train = pd.read_csv(os.path.join(CUR_PATH, "Train.csv"))
test = pd.read_csv(os.path.join(CUR_PATH, "Test.csv"))
test["type"] = "test"
train["type"] = "train"
df = train.append(test, ignore_index=True)
df.drop(["S/N"],1, inplace=True)
df.drop(["reason"],1, inplace=True)

l_encode = LabelEncoder()
obj_feat = ["Gender", "Location", "famsize", "Pstatus", "schoolsup", "famsup", "paid",
            "activities", "nursery", "higher", "internet"]
for var in obj_feat:
    df[var] = l_encode.fit_transform(df[var])
train = df.loc[df['type']=='train']
test = df.loc[df['type']=='test']
train.drop(['type'],axis=1,inplace=True)
test.drop(['type','Scores'],axis=1,inplace=True)

# def dev_model(alg, dtrain, predictors, performCV=True, printFeatureImportance=True, cv_folds=5):
#     # Fit the algorithm on the data
#     alg.fit(dtrain[predictors], dtrain["Scores"])
#
#     # Predict training set:
#     dtrain_predictions = alg.predict(dtrain[predictors])
#
#     # Perform cross-validation:
#     cv_score = cross_validation.cross_val_score(alg, dtrain[predictors], dtrain["Scores"], cv=cv_folds,
#                                                 scoring='mean_squared_error')
#     cv_score = np.sqrt(np.abs(cv_score))
#
#     # Print model report:
#     print("\nModel Report")
#     print("RMSE : %.4g" % np.sqrt(metrics.mean_squared_error(dtrain["Scores"].values, dtrain_predictions)))
#     print("CV Score : Mean - %.4g | Std - %.4g | Min - %.4g | Max - %.4g" % (np.mean(cv_score),
#                                                                              np.std(cv_score), np.min(cv_score),
#                                                                              np.max(cv_score)))
#
# predictors = [x for x in train.columns if x not in ["Scores"]]
#
# gbr = GradientBoostingRegressor(learning_rate=0.1, n_estimators=26,max_depth= 5,
#                                 min_samples_leaf= 2, min_samples_split= 16 ,random_state=4,
#                                 max_features= 17, subsample= 0.9)
# dev_model(gbr, train, predictors)
#
# with open("Model.pickle", "wb") as f:
#     pk.dump(gbr, f)
#     f.close()
#




