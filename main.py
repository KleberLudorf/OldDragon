from models.estilos.EstiloAventureiro import Estilo_Aventureiro
from models.estilos.EstiloClassico import Estilo_Classico
from models.estilos.EstiloHeroico import Estilo_Heroico

from models.racas.Humano import Humano
from models.racas.Elfo import Elfo
from models.racas.Anao import Anao
from models.racas.Halfling import Halfling
from models.racas.Gnomo import Gnomo
from models.racas.Meio_Elfo import Meio_Elfo


from models.classe.Mago import Mago
from models.classe.Druida import Druida
from models.classe.Ladrao import Ladrao


import utils.Console_Utils as Cons
import time

nome = input("DIGITE O NOME DO INVOCADOR: ")
# --- Escolha de Raça ---
while True:
    Cons.limpar_tela()
    print("\nEscolha a raça do personagem:")
    print("1 - Humano")
    print("2 - Elfo")
    print("3 - Anão")
    print("4 - Meio-Elfo")
    print("5 - Gnomo")
    print("6 - Halfling")
    

    raca_opcao = input("Opção: ")

    if raca_opcao == "1":
        raca = Humano()
        break
    elif raca_opcao == "2":
        raca = Elfo()
        break
    elif raca_opcao == "3":
        raca = Anao()
        break
    elif raca_opcao == "4":
        raca = Meio_Elfo()
        break
    elif raca_opcao == "5":
        raca = Gnomo()
        break
    elif raca_opcao == "6":
        raca = Halfling()
        break
    else:
        print("Opção inválida!.")
        time.sleep(0.9)


# --- Escolha do Estilo ---
while True:
    Cons.limpar_tela()
    print("\nEscolha o estilo de geração:")
    print("1 - Clássico (3d6 direto nos atributos)")
    print("2 - Aventureiro (6 valores, você distribui)")
    print("3 - Heroico (4d6 dropa o menor, você distribui)")

    estilo = input("Opção: ")

    if estilo == "1":
        Player = Estilo_Classico(nome, raca)
        break
    elif estilo == "2":
        Player = Estilo_Aventureiro(nome, raca)
        Player.Definindo_Atributos()
        break
    elif estilo == "3":
        Player = Estilo_Heroico(nome, raca)
        Player.Definindo_Atributos()
        break
    else:
        print("Opção inválida")
        time.sleep(0.9)
    
#Escolha de Classe
while True:
    Cons.limpar_tela()
    print("\nEscolha a classe do personagem:")
    print("1 - Mago")
    print("2 - Ladrão")
    print("3 - Druida")

    classe_opcao = input("Opção: ")

    if classe_opcao == "1":
        classe = Mago()
        break
    elif classe_opcao == "2":
        classe = Ladrao()
        break
    elif classe_opcao == "3":
        classe = Druida()
        break
    else:
        print("Opção inválida.")
        time.sleep(0.9)

Player.escolher_classe(classe)

# --- Mostrando ficha ---
Player.Mostrando_Jogador()
