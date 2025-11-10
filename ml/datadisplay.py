import matplotlib.pyplot as plt
import numpy as np
from lineareg import y_train, y_lr_train
from randomfor import y_rf_train

def plot_regression_results():
    plt.figure(figsize=(5, 5))
    plt.scatter(x=y_train,y=y_lr_train, color='blue', alpha=0.5)

    x = np.polyfit(y_train, y_lr_train, 1)
    p = np.poly1d(x)

    plt.plot(y_train, p(y_train), color='red')
    plt.ylabel('Predicted logS - Linear Regression')
    plt.xlabel('Actual logS')

    plt.show()

def plot_random_forest_results():
    plt.figure(figsize=(5, 5))
    plt.scatter(x=y_train,y=y_rf_train, color='green', alpha=0.5)

    x = np.polyfit(y_train, y_rf_train, 1)
    p = np.poly1d(x)

    plt.plot(y_train, p(y_train), color='red')
    plt.ylabel('Predicted logS - Random Forest')
    plt.xlabel('Actual logS')

    plt.show()

def main():
    def novamente():
        while True:
            again = input("Deseja ver outro gráfico? (s/n) ").lower()
            if again == 's':
                return True
            elif again == 'n':
                return False
            else:
                print("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")
    while True:
        a = input("Pressione 1 para ver os resultados da Regressão Linear ou 2 para ver os resultados da Floresta Aleatória: ")

        if a == '1':
            plot_regression_results()
            if not novamente():
                print("Encerrando o programa.")
                break
        elif a == '2':
            plot_random_forest_results()
            if not novamente():
                print("Encerrando o programa.")
                break
        else:
            print("Entrada inválida. Por favor, digite 1 ou 2.")
        
main()