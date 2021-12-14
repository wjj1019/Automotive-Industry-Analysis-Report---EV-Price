import numpy as np
import pandas as pd
import xgboost as xgb
import pickle


# Import Data
v_spec = pd.read_csv('vehicle_spec')
v_spec.drop(['Unnamed: 0'], axis=1, inplace=True)
v = v_spec.drop([14,47]).reset_index(drop=True)

# Dependent and Independent Variable (Not Splitting into Train Test)
X = v.iloc[:,2:8] 
y = v['Price(German)'] 

#ML model

ml = xgb.XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
             colsample_bynode=1, colsample_bytree=0.8326308450130173, gamma=0,
             gpu_id=-1, importance_type='gain', interaction_constraints='',
             learning_rate=0.033017161618132056, max_delta_step=0, max_depth=7,
             min_child_weight=1, monotone_constraints='()',
             n_estimators=329, n_jobs=8, num_parallel_tree=1, random_state=42,
             reg_alpha=0, reg_lambda=1, scale_pos_weight=1,
             subsample=0.4458551483938323, tree_method='exact',
             validate_parameters=1, verbosity=None)

ml.fit(X, y)

pickle.dump(ml, open('model.pkl', 'wb'))
