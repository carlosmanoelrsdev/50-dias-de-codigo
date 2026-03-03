from automacao_regras.modelo import Regra


class ServicoAutomacaoRegras:
    def __init__(self):
        self.regras = {}
        self.proximo_id = 1

    def criar_regra(self, nome, condicao, acao):
        id = self.proximo_id
        self.proximo_id += 1
        regra = Regra(id, nome, condicao, acao)
        self.regras[id] = regra
        return regra

    def listar_regras(self):
        return list(self.regras.values())

    def executar_regras(self, contexto):
        """Executa regras ativas de acordo com o contexto fornecido."""
        resultados = []
        for regra in self.regras.values():
            if regra.ativa and self._avaliar_condicao(regra.condicao, contexto):
                resultados.append({"regra": regra.nome, "acao": regra.acao})
        return resultados

    def _avaliar_condicao(self, condicao, contexto):
        """Avalia se a condição da regra é satisfeita pelo contexto."""
        return condicao in contexto

    def desativar_regra(self, id):
        regra = self.regras.get(id)
        if regra:
            regra.ativa = False
            return True
        return False
