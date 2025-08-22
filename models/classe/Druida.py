import models.Classe as C

class Druida(C.Classe):
    def __init__(self):
        habilidades_iniciais = [
            "Herbalismo" 
        ]
        super().__init__("Druida", dado_vida=8, habilidades_iniciais=habilidades_iniciais)
        self.transformacoes = 0  # controle de quantas transformações pode usar
        self.forma_max_dv = 0    # DV máximo da criatura que pode assumir

    def restricoes(self):
        return "O Druida deve ser Neutro e não pode usar armas ou armaduras metálicas."

    def subir_nivel(self, constituicao):
        super().subir_nivel(constituicao)

        # habilidades por lvl
        if self.nivel == 3 and "Previdência" not in self.habilidades:
            self.habilidades.append("Previdência")

        if self.nivel == 6:
            self.transformacoes = 3
            self.forma_max_dv = 6
            if "Transformação" not in self.habilidades:
                self.habilidades.append("Transformação")

        if self.nivel == 10:
            self.forma_max_dv = 10
            if "Transformação Melhorada" not in self.habilidades:
                self.habilidades.append("Transformação Melhorada")

        return self.pontos_de_vida

    def usar_transformacao(self, animal, dv_animal):
        """
        Tenta usar a habilidade de transformação.
        """
        if self.transformacoes <= 0:
            return "Você não pode se transformar agora."

        if dv_animal > self.forma_max_dv:
            return f"O Druida ainda não consegue assumir a forma de um animal com {dv_animal} DV."

        self.transformacoes -= 1
        return f"O Druida se transformou em um {animal} ({dv_animal} DV). Restam {self.transformacoes} transformações hoje."