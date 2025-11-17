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
             print("Código deve ser um número inteiro e positivo. Tente novamente.")
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
                preco = input("Preço: ").replace(",",".")
                precof = float(preco)
                if precof < 0:
                    os.system("cls")
                    print("Preço deve ser um número positivo. Tente novamente.")
                    continue
            except ValueError:
                os.system("cls")
                print("Preço deve ser um número válido. Tente novamente.")
                continue
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
    listar()

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

    with open("beysales.txt", "r", encoding="utf-8") as f:
        linhas = [ln.strip() for ln in f.readlines() if ln.strip()]

    if not linhas:
        print("Nenhum beyblade cadastrado.")
        return

    beyblades = []
    for ln in linhas:
        parts = ln.split(",")
        # garante 5 partes, caso o arquivo esteja corrompido pula a linha
        if len(parts) < 5:
            continue
        codigo = parts[0].strip()
        tipo = parts[1].strip()
        nome = parts[2].strip()
        try:
            preco = float(parts[3].strip())
        except Exception:
            preco = 0.0
        try:
            estoque = int(parts[4].strip())
        except Exception:
            estoque = 0
        beyblades.append([codigo, tipo, nome, preco, estoque])

    if not beyblades:
        os.system('cls')
        print("Nenhum beyblade válido encontrado no arquivo.")
        return

    print("=== 🌀 Beyblades Cadastradas ===")
    for b in beyblades:
        print(f"Código: {b[0]:<6} | Nome: {b[2]:<10} | Tipo: {b[1]:<25} | Preço: R${b[3]:>8} | Estoque: {b[4]:>3}")

    # loop para obter código válido e existente
    while True:
        codigo_busca = input("\nDigite o código da Beyblade que deseja alterar: ").strip()
        if not codigo_busca:
            os.system('cls')
            print("Entrada vazia. Digite um código válido.")
            continue
        if not codigo_busca.isdigit():
            os.system('cls')
            print("Código inválido! Digite apenas números.")
            continue
        encontrada = next((b for b in beyblades if b[0] == codigo_busca), None)
        if not encontrada:
            os.system('cls')
            print("Nenhuma Beyblade encontrada com esse código. Tente novamente.")
            continue
        break

    os.system('cls')
    print("\nBeyblade encontrada:")
    print(f"Código: {encontrada[0]}")
    print(f"Tipo: {encontrada[1]}")
    print(f"Nome: {encontrada[2]}")
    print(f"Preço: R${encontrada[3]:.2f}")
    print(f"Estoque: {encontrada[4]}")

    original_code = encontrada[0]

    # novo código - loop de verificação (vazio mantém)
    while True:
        novo_codigo = input("\nNovo código (deixe vazio para manter): ").strip()
        if not novo_codigo:
            break
        if not novo_codigo.isdigit():
            os.system('cls')
            print("Código inválido. Digite apenas números ou deixe vazio para manter o atual.")
            continue
        if any(b[0] == novo_codigo for b in beyblades if b[0] != original_code):
            os.system('cls')
            print("Código já existe. Informe outro ou deixe vazio para manter o atual.")
            continue
        encontrada[0] = novo_codigo
        break

    # novo tipo - loop de verificação (vazio mantém)
    tipos_validos = ["ataque", "defesa", "equilibrio", "equilíbrio"]
    while True:
        novo_tipo = input("Novo tipo (deixe vazio para manter): ").strip()
        if not novo_tipo:
            break
        if novo_tipo.lower() not in tipos_validos:
            os.system('cls')
            print("Tipo inválido. Use: Ataque, Defesa ou Equilíbrio (ou deixe vazio).")
            continue
        encontrada[1] = novo_tipo
        break

    # novo nome - loop de verificação (vazio mantém)
    while True:
        novo_nome = input("Novo nome (deixe vazio para manter): ").strip()
        if not novo_nome:
            break
        if novo_nome.strip() == "":
            os.system('cls')
            print("Nome inválido. Tente novamente ou deixe vazio para manter.")
            continue
        if not all(ch.isalpha() or ch.isspace() for ch in novo_nome):
            os.system('cls')
            print("Nome deve conter apenas letras e espaços. Tente novamente.")
            continue
        if any(b[2].strip().lower() == novo_nome.lower() for b in beyblades if b[0] != encontrada[0]):
            os.system('cls')
            print("Nome já existe. Tente outro nome ou deixe vazio para manter.")
            continue
        encontrada[2] = novo_nome
        break

    # novo preço - loop de verificação (vazio mantém)
    while True:
        novo_preco = input("Novo preço (deixe vazio para manter): ").strip()
        if not novo_preco:
            break
        try:
            preco_val = float(novo_preco.replace(",", "."))
            if preco_val < 0:
                os.system('cls')
                print("Preço deve ser positivo. Tente novamente ou deixe vazio para manter.")
                continue
            encontrada[3] = preco_val
            break
        except ValueError:
            os.system('cls')
            print("Preço inválido. Digite um número válido ou deixe vazio para manter.")
            continue

    # novo estoque - loop de verificação (vazio mantém)
    while True:
        novo_estoque = input("Novo estoque (deixe vazio para manter): ").strip()
        if not novo_estoque:
            break
        try:
            estoque_val = int(novo_estoque)
            if estoque_val < 0:
                os.system('cls')
                print("Estoque deve ser positivo. Tente novamente ou deixe vazio para manter.")
                continue
            encontrada[4] = estoque_val
            break
        except ValueError:
            os.system('cls')
            print("Estoque inválido. Digite um número inteiro ou deixe vazio para manter.")
            continue

    # Salva de volta no arquivo
    with open("beysales.txt", "w", encoding="utf-8") as f:
        for b in beyblades:
            f.write(f"{b[0]},{b[1]},{b[2]},{b[3]},{b[4]}\n")

    print("\nBeyblade atualizada com sucesso!")
    print(f"Código: {encontrada[0]} | Nome: {encontrada[2]} | Tipo: {encontrada[1]} | Preço: R${encontrada[3]:.2f} | Estoque: {encontrada[4]}")

def excluir():
    with open("beysales.txt", "r", encoding='utf-8') as f:
        beyblades = f.readlines()


    while True:
        try:
            listar()
            e = input("Digite o ID do beyblade que deseja excluir: ").strip()
        
            if e not in [line.split(",")[0].strip() for line in beyblades]:
                os.system('cls')
                print("ID não encontrado, insira um ID existente...")
                continue
                
        except Exception as ex:
            os.system('cls')
            print("Erro ao processar o ID:", ex)
            continue
        
        else:
            filtered = []
            for ln in beyblades:
                if not ln.strip():
                    continue
                parts = ln.strip().split(",")
                if parts[0] != e:
                    filtered.append(ln)
            with open("beysales.txt", "w", encoding="utf-8") as f:
                f.writelines(filtered)
                print("Beyblade removido com sucesso!")
                break

def main():
    while True:
        try:
         print(tit)
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
            elif esc == 3:
               atualizarbeyblade()
               if not tentar_novamente():
                  break
            elif esc == 4:
               excluir()
               if not tentar_novamente():
                  break
            elif esc == 0:
               os.system("cls")
               print("Fim do programa!")
               break
            
main()