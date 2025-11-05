import os   

tit = f"""
==============================
BEYSALES - Gerente de Estoque
==============================
1 - Cadastrar Beyblade
2 - Listar Beyblades
3 - Atualizar Beyblade
4 - Excluir Beyblade
5 - Relatório por Tipo
0 - Sair 
"""
def cadastrar_beyblade():
    with open("beysales.txt", "a+", encoding="utf-8") as f:
        while True:
            codigo = input("Código do Beyblade: ")
            if codigo in [line.split(",")[0] for line in open("beysales.txt", "r", encoding="utf-8").readlines()]:
             print("Código já existe. Tente novamente ou atualize o beyblade.")
            elif codigo.isdigit() == False:
             print("Código deve ser um número inteiro. Tente novamente.")
            else:
             break
         
        while True:
            tipo = input("Tipo (Ataque, Defesa, Equilíbrio): ")
            if tipo not in [line.split(",")[1] for line in open("beysales.txt", "r", encoding="utf-8").readlines()]:
             print("Tipo inválido. Tente novamente.")
            else:
             break
         
        while True: 
            nome = input("Nome do Beyblade: ")
            if nome.strip() == "":
             print("Nome não pode ser vazio. Tente novamente.")
            elif nome in [line.split(",")[2] for line in open("beysales.txt", "r", encoding="utf-8").readlines()]:
             print("Nome já existe. Tente novamente ou atualize o beyblade.")
            elif nome.isalpha() == False:
             print("Nome deve conter apenas letras. Tente novamente.") 
            else:
             break

        while True:
            try:
                preco = float(input("Preço: "))
                if preco < 0:
                    print("Preço deve ser um número positivo. Tente novamente.")
            except ValueError:
                print("Preço deve ser um número válido. Tente novamente.")
            else:
               break
            
        while True:
            try:
                quantidade = int(input("Quantidade em estoque: "))
                if quantidade < 0:
                    print("Quantidade deve ser um número positivo. Tente novamente.")
            except ValueError:
                print("Quantidade deve ser um número inteiro válido. Tente novamente.")
            else:
               break
        
        f.write(f"{codigo},{tipo},{nome},{preco},{quantidade}\n")
    print("Beyblade cadastrado com sucesso!")

def main():
    print(tit)
    while True:
        try:
         esc = int(input("Qual operação deseja realizar? (0-5)"))
         if esc < 0 or esc > 5:
            print("Escolha uma opção entre 0 e 5.")
        except ValueError:
            print("Insira um valor válido")
        else:
            break
    
    if esc == 1:
     cadastrar_beyblade()

main()