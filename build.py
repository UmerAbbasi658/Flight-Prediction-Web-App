import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split

df=pd.read_csv('deploy_df')

df.drop('Unnamed: 0',axis=1,inplace=True)

x=df.drop('Price',axis=1)
print(x.head())

y=df['Price']

#splitting the dataset
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 50)



from catboost import CatBoostRegressor

cat=CatBoostRegressor()
cat.fit(x_train,y_train)

y_predict=cat.predict(x_test)

#Use pickle to save our model so that we can use it later

import pickle
# Saving model
pickle.dump(cat, open('model.pk1','wb'))
model=pickle.load(open('model.pk1','rb'))
print(y_predict)