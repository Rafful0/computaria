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
 
def tentar_novamente():
    while True:
        t = input("Deseja rodar o programa novamente? (S/N) ")
        if t.lower() == "s":
            os.system("cls")
            print(tit)
            return True
        elif t.lower() == "n":
         os.system("cls")
         print("Fim do programa")
         return False
         
        else:
         print("Insira uma resposta válida")


def cadastrar_beyblade():
    with open("beysales.txt", "a+", encoding="utf-8") as f:
        while True:
            codigo = input("Código do Beyblade: ")
            if codigo in [line.split(",")[0] for line in open("beysales.txt", "r", encoding="utf-8").readlines()]:
             os.system("cls")
             print("Código já existe. Tente novamente ou atualize o beyblade.")
            elif codigo.isdigit() == False:
             os.system("cls")
             print("Código deve ser um número inteiro. Tente novamente.")
            else:
             break
         
        while True:
            tipo = input("Tipo (Ataque, Defesa, Equilíbrio): ")
            if tipo.lower() not in ["ataque","defesa","equilibrio","equilíbrio"]:
             os.system("cls")
             print("Tipo inválido. Tente novamente.")
            else:
             os.system("cls")
             break
         
        while True: 
            nome = input("Nome do Beyblade: ")
            if nome.strip() == "":
             os.system("cls")
             print("Nome não pode ser vazio. Tente novamente.")
            elif nome.lower() in [line.split(",")[2].strip().lower() for line in open("beysales.txt", "r", encoding="utf-8").readlines()]:
             os.system("cls")
             print("Nome já existe. Tente novamente ou atualize o beyblade.")
            elif not all(ch.isalpha() or ch.isspace() for ch in nome):
             os.system("cls")
             print("Nome deve conter apenas letras. Tente novamente.") 
            else:
             os.system("cls")
             break

        while True:
            try:
                preco = float(input("Preço: ").replace(",","."))
                if preco < 0:
                    os.system("cls")
                    print("Preço deve ser um número positivo. Tente novamente.")
            except ValueError:
                os.system("cls")
                print("Preço deve ser um número válido. Tente novamente.")
            else:
               os.system("cls")
               break
            
        while True:
            try:
                quantidade = int(input("Quantidade em estoque: "))
                if quantidade < 0:
                    os.system("cls")
                    print("Quantidade deve ser um número positivo. Tente novamente.")
            except ValueError:
                os.system("cls")
                print("Quantidade deve ser um número inteiro válido. Tente novamente.")
            else:
               os.system("cls")
               break
        
        f.write(f"{codigo},{tipo},{nome},{preco},{quantidade}\n")
    os.system("cls")
    print("Beyblade cadastrado com sucesso!")

def main():
    print(tit)
    while True:
        try:
         esc = int(input("Qual operação deseja realizar? (0-5) "))
         if esc < 0 or esc > 5:
            print("Escolha uma opção entre 0 e 5.")
        except ValueError:
            os.system("cls")
            print("Insira um valor válido")
        else:
            os.system("cls")
            if esc == 1:
                cadastrar_beyblade()
                if not tentar_novamente():
                   break
            elif esc == 0:
               os.system("cls")
               print("Fim do programa!")
               break
            
main()