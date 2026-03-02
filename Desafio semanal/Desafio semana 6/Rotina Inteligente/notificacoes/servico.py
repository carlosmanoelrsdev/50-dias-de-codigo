import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from persistencia.repositorio_base import RepositorioBase
from .modelo import Notificacao


class ServicoNotificacoes:
    """Serviço responsável pelo envio e controle de notificações."""

    def __init__(self):
        self._repositorio = RepositorioBase()

    def enviar(self, mensagem, usuario_id=None, tipo=Notificacao.TIPO_INFO):
        notificacao = Notificacao(mensagem=mensagem, usuario_id=usuario_id, tipo=tipo)
        notificacao = self._repositorio.salvar(notificacao)
        print(f"[{notificacao.tipo.upper()}] {notificacao.mensagem}")
        return notificacao

    def marcar_como_lida(self, notificacao_id):
        notificacao = self._repositorio.buscar_por_id(notificacao_id)
        if notificacao:
            notificacao.lida = True
            self._repositorio.atualizar(notificacao)
        return notificacao

    def listar_nao_lidas(self, usuario_id=None):
        todas = self._repositorio.listar_todos()
        nao_lidas = [n for n in todas if not n.lida]
        if usuario_id is not None:
            nao_lidas = [n for n in nao_lidas if n.usuario_id == usuario_id]
        return nao_lidas
