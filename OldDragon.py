import random
import os

# Utils
class ConsoleUtils():
    @staticmethod
    def limpar_tela():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux, macOS, etc.
            os.system('clear')

class Rola_Dados():
    @staticmethod
    def rolando_d6():
        return random.randint(1, 6)
    
    @staticmethod
    def rolagem_atributo():
        soma = 0
        for i in range(3):
            dado = Rola_Dados.rolando_d6()
            soma += dado
        return soma

class Personagem():
    def __init__(self, nome):
        self.nome = nome
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        self.valores = []

    def Definindo_Atributos(self):
        atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]
        
        for atributo in atributos:
            while True:
                print(f"\nValores disponíveis: {self.valores}\n")
                valorUser = input(f"{atributo.capitalize()} = ")

                if valorUser.isdigit():
                    valor = int(valorUser)
                    if valor in self.valores:
                        setattr(self, atributo, valor)
                        self.valores.remove(valor)
                        print(f"{atributo.capitalize()} atribuído = {valor}")
                        break
                print(f"O valor '{valorUser}' não é válido.")

    def Mostrando_Jogador(self):
        ConsoleUtils.limpar_tela()
        print("\n---- FICHA DO JOGADOR ----")
        print(f"Nome: {self.nome}")
        print(f"Força: {self.forca}")
        print(f"Destreza: {self.destreza}")
        print(f"Constituição: {self.constituicao}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Sabedoria: {self.sabedoria}")
        print(f"Carisma: {self.carisma}")

class Estilo_Classico(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = Rola_Dados.rolagem_atributo()
        self.destreza = Rola_Dados.rolagem_atributo()
        self.constituicao = Rola_Dados.rolagem_atributo()
        self.inteligencia = Rola_Dados.rolagem_atributo()
        self.sabedoria = Rola_Dados.rolagem_atributo()
        self.carisma = Rola_Dados.rolagem_atributo()

class Estilo_Aventureiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.valores = self.Vetorizacao_Rolagem()

    def Vetorizacao_Rolagem(self):
        valores = []
        for i in range(6):
            soma = 0
            for j in range(3):
                d6 = Rola_Dados.rolando_d6()
                soma += d6
            valores.append(soma)
        return valores

class Estilo_Heroico(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.valores = self.TiraMenor()

    def TiraMenor(self):
        valores = []

        for qntd_roll in range(6):
            d6 = []
            soma = 0
            for dados_in_roll in range(4):
                dados_in_roll = Rola_Dados.rolando_d6()
                d6.append(dados_in_roll)
                soma += dados_in_roll

            d6 = sorted(d6, key = None, reverse=False)
            menor = d6.pop(0)
            soma -= menor
            valores.append(soma)

        return valores

    def Definindo_Atributos(self):
        atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]
        
        for atributo in atributos:
            while True:
                print(f"\nValores disponíveis: {self.valores}\n")
                valorUser = input(f"{atributo.capitalize()} = ")

                if valorUser.isdigit():
                    valor = int(valorUser)
                    if valor in self.valores:
                        setattr(self, atributo, valor)
                        self.valores.remove(valor)
                        print(f"{atributo.capitalize()} atribuído = {valor}")
                        break
                print(f"O valor '{valorUser}' não é válido.")

    def Mostrando_Jogador(self):
        ConsoleUtils.limpar_tela()
        print("\n---- FICHA DO JOGADOR ----")
        print(f"Nome: {self.nome}")
        print(f"Força: {self.forca}")
        print(f"Destreza: {self.destreza}")
        print(f"Constituição: {self.constituicao}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Sabedoria: {self.sabedoria}")
        print(f"Carisma: {self.carisma}")
        
#Main
nome = input("Digite um nome: ")

print("\nEscolha o estilo de geração:")
print("1 - Clássico (3d6 direto nos atributos)")
print("2 - Aventureiro (6 valores, você distribui)")
print("3 - Heroico (4d6 dropa o menor, você distribui)")

estilo = input("Opção: ")

if estilo == "1":
    Player = Estilo_Classico(nome)
elif estilo == "2":
    Player = Estilo_Aventureiro(nome)
    Player.Definindo_Atributos()
elif estilo == "3":
    Player = Estilo_Heroico(nome)
    Player.Definindo_Atributos()
else:
    print("Opção inválida, gerando no modo clássico por padrão.")
    Player = Estilo_Classico(nome)

Player.Mostrando_Jogador()