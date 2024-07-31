import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
import pickle

# Load the dataset
path = "team_traditional.csv"  # Update this path
df = pd.read_csv(path)

# Define features and target variable
features = ['PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'PF', '+/-']
aggregated_data = {}

for gameid, group in df.groupby('gameid'):
    team_names = ' vs '.join(group['team'])
    aggregated_data[gameid] = {'teams': team_names}
    for feature in features:
        if feature in ['FG%', '3P%', 'FT%']:
            aggregated_data[gameid][feature] = group[feature].mean()
        else:
            aggregated_data[gameid][feature] = group[feature].sum()

agg_df = pd.DataFrame.from_dict(aggregated_data, orient='index').reset_index()
agg_df.rename(columns={'index': 'gameid'}, inplace=True)

X = agg_df[features]
y = agg_df['PTS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
gbr = GradientBoostingRegressor(random_state=42)
gbr.fit(X_train, y_train)

y_train_pred = gbr.predict(X_train)
y_test_pred = gbr.predict(X_test)

train_rmse = sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = sqrt(mean_squared_error(y_test, y_test_pred))

print(f"RMSE (training): {train_rmse:.6f}")
print(f"RMSE (test): {test_rmse:.6f}")

predictions_df = pd.DataFrame({
    'Actual': y_test,
    'Predicted': y_test_pred
})

print(predictions_df)

# Save the model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(gbr, f)

print("Model saved as model.pkl")
