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

def listar():
   with open("beysales.txt", "r+", encoding="utf-8") as f:
        beyblades = f.readlines()
        if not beyblades:
             print("Nenhum beyblade cadastrado.")
        else:
             for line in beyblades:
                codigo, tipo, nome, preco, quantidade = line.strip().split(",")
                preco = f"{float(preco):.2f}"
                print(f"{codigo:<6} | {tipo:<10} | {nome:<25} | R${preco:>8} | {quantidade:>3}")

def atualizarbeyblade():
    # Lista de beyblades existentes
    beyblades = [
        [1727, "Ataque", "Valkyrie Turbo", 89.90, 10],
        [1885, "Defesa", "Kerbeus Guard", 74.50, 5],
        [4932, "Equilíbrio", "Spriggan Requiem", 99.00, 8],
        [3445, "Ataque", "Dragon Vortex", 85.00, 12],
        [5983, "Defesa", "Phoenix Shield", 92.30, 6]
    ]

   
    print("=== 🌀 Beyblades Cadastradas ===")
    for b in beyblades:
        print(f"Código: {b[0]} | Nome: {b[2]} | Tipo: {b[1]} | Preço: R${b[3]:.2f} | Estoque: {b[4]}")

   
    codigo = input("\nDigite o código da Beyblade que deseja alterar: ").strip()

    if not codigo.isdigit():
        print(" Código inválido! Digite apenas números.")
        return

    codigo = int(codigo)
    encontrada = None

   
    for b in beyblades:
        if b[0] == codigo:
            encontrada = b
            break

    if not encontrada:
        print("Nenhuma Beyblade encontrada com esse código.")
        return

    
    print("\n Beyblade encontrada:")
    print(f"Código: {encontrada[0]}")
    print(f"Tipo: {encontrada[1]}")
    print(f"Nome: {encontrada[2]}")
    print(f"Preço: R${encontrada[3]:.2f}")
    print(f"Estoque: {encontrada[4]}")
    
    novo_codigo = input("\nNovo código (deixe vazio para manter): ")
    novo_tipo = input("\nNovo tipo (deixe vazio para manter): ").strip()
    novo_nome = input("Novo nome (deixe vazio para manter): ").strip()
    novo_preco = input("Novo preço (deixe vazio para manter): ").strip()
    novo_estoque = input("Novo estoque (deixe vazio para manter): ").strip()

    if novo_codigo:
       try:
         encontrada[0] = int(novo_codigo)
       except ValueError:
          print(" Código inválido. Mantendo o anterior.")
          
          
    if novo_tipo:
        encontrada[1] = novo_tipo
    if novo_nome:
        encontrada[2] = novo_nome
    if novo_preco:
        try:
            encontrada[3] = float(novo_preco)
        except ValueError:
            print(" Preço inválido. Mantendo o anterior.")
    if novo_estoque:
        try:
            encontrada[4] = int(novo_estoque)
        except ValueError:
            print(" Estoque inválido. Mantendo o anterior.")

    print("\n Beyblade atualizada com sucesso!")
    print(f"Código: {encontrada[0]} | Nome: {encontrada[2]} | Tipo: {encontrada[1]} | Preço: R${encontrada[3]:.2f} | Estoque: {encontrada[4]}")

    
    with open("beysales.txt", "w", encoding="utf-8") as f:
        for b in beyblades:
            f.write(f"{b[0]},{b[1]},{b[2]},{b[3]},{b[4]}\n")

    print("\n💾 Alterações salvas no arquivo 'beysales.txt' com sucesso!")

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
            elif esc == 2:
               listar()
               if not tentar_novamente():
                    break
            elif esc == 0:
               os.system("cls")
               print("Fim do programa!")
               break
            
main()