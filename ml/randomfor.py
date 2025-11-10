import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from lineareg import X_train, X_test, y_train, y_test, results

rf = RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(X_train, y_train)

y_rf_train = rf.predict(X_train)
y_rf_test = rf.predict(X_test)

rf_train_mse = mean_squared_error(y_train, y_rf_train)
rf_train_r2 = r2_score(y_train, y_rf_train)

rf_test_mse = mean_squared_error(y_test, y_rf_test)
rf_test_r2 = r2_score(y_test, y_rf_test)

rf_results = pd.DataFrame({
    'Method': ['Random Forest'],
    'Train MSE': [rf_train_mse],
    'Train R2': [rf_train_r2],
    'Test MSE': [rf_test_mse],
    'Test R2': [rf_test_r2]
})

# Comparando os modelos

df_models = pd.concat([results, rf_results], ignore_index=True)

if __name__ == "__main__":
    print(df_models)