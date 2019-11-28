import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

def provide_cleaned_df(filename):
    data = pd.read_csv(filename, index_col=False, low_memory=False) #the low_memory argument accounts for blank cells
    clean_data = pd.DataFrame({'posteam': data['posteam'], 'play_type': data['play_type']})
    clean_data['down'] = data['down']
    clean_data['game_seconds_remaining'] = data['game_seconds_remaining']
    clean_data['quarter_seconds_remaining'] = data['quarter_seconds_remaining']
    clean_data['yardline_100'] = data['yardline_100']
    clean_data['ydstogo'] = data['ydstogo']
    clean_data['score_differential'] = data['score_differential']
    # clean_data_old['timeout'] = old_data['timeout']

    clean_data = clean_data.dropna()
    # clean_data_old = clean_data_old[(clean_data_old['posteam'] == team)]
    clean_data = clean_data[(clean_data['play_type'] != 'no_play')]
    clean_data = clean_data[(clean_data['ydstogo'] != 0)]
    return clean_data


# file2016 = "reg_pbp_2009.csv"
oldfile = "reg_pbp_2016.csv"    #the old year used for training
newfile = "reg_pbp_2017.csv"    #the new year used for testing
old_year = oldfile[-8:-4]
new_year = newfile[-8:-4]
team = "NE"

#Getting a model that can predict team plays in the old year

clean_data_old = provide_cleaned_df(oldfile)
clean_data_old = clean_data_old[(clean_data_old['posteam'] == team)]
# print(clean_data_old)
y = clean_data_old['play_type']
X = clean_data_old.drop(['play_type', 'posteam'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y)
# print(X_train)

#Trying to use weights to get a better score. This did not help.
# weights = [0.0000001, 0.0000001, 0.0000001, 1, 1]
# weights_matrix = np.tile(weights, (len(X_train.index), 1))
# print(weights_matrix)

model = GaussianNB()
model.fit(X, y)
# score = model.score(X_test, y_test)
# print(old_year, team, "score", score)

#The below 3 variables were used to see the kind of predictions the model was making
predictions = model.predict(X_test)
real = y_test.values
real_counts = y_test.value_counts()


#Does this model work to predict new year data?

clean_data_new = provide_cleaned_df(newfile)
team_data_new = clean_data_new[(clean_data_new['posteam'] == team)]

y_team_new = team_data_new['play_type']
X_team_new = team_data_new.drop(['play_type', 'posteam'], axis=1)
score_team_new = model.score(X_team_new, y_team_new)
print(new_year, team, "score", score_team_new)


#Are we really finding patterns in the team's play, or just football patterns in general?
#Let's use this model to test all teams in the new year.

y_new = clean_data_new['play_type']
X_new = clean_data_new.drop(['play_type', 'posteam'], axis=1)
score_new = model.score(X_new, y_new)
print(new_year, "NFL score", score_new)