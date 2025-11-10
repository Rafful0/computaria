import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score    

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/delaney_solubility_with_descriptors.csv")

# Separando os dados

y = df['logS']
x = df.drop('logS', axis=1)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

# Construindo e treinando o modelo

lr = LinearRegression()
lr.fit(X_train, y_train)

# Aplicando o modelo

y_lr_train = lr.predict(X_train)
y_lr_test = lr.predict(X_test)

# Avaliando o modelo

lr_train_mse = mean_squared_error(y_train, y_lr_train)
lr_train_r2 = r2_score(y_train, y_lr_train)

lr_test_mse = mean_squared_error(y_test, y_lr_test)
lr_test_r2 = r2_score(y_test, y_lr_test)

print(f"""
LR MSE (treino): {lr_train_mse:.4f}
LR R2 (treino): {lr_train_r2:.4f}
LR MSE (teste): {lr_test_mse:.4f}
LR R2 (teste): {lr_test_r2:.4f}
""")

results = pd.DataFrame({
    'Method': ['Linear Regression'],
    'Train MSE': [lr_train_mse],
    'Train R2': [lr_train_r2],
    'Test MSE': [lr_test_mse],
    'Test R2': [lr_test_r2]
})

if __name__ == "__main__":
    print(results)