class MenuPrincipal:
    """Interface de linha de comando para a Rotina Inteligente."""

    OPCOES = {
        "1": "Gerenciar Usuários",
        "2": "Gerenciar Tarefas",
        "3": "Agendamentos",
        "4": "Notificações",
        "5": "Clima",
        "6": "Assistente IA",
        "7": "Regras de Automação",
        "0": "Sair",
    }

    def __init__(self, app):
        self._app = app
        self._ativo = True

    def _exibir_menu(self):
        print("\n===== Rotina Inteligente =====")
        for chave, descricao in self.OPCOES.items():
            print(f"  [{chave}] {descricao}")
        print("==============================")

    def _processar_opcao(self, opcao):
        acoes = {
            "1": self._menu_usuarios,
            "2": self._menu_tarefas,
            "3": self._menu_agendamentos,
            "4": self._menu_notificacoes,
            "5": self._menu_clima,
            "6": self._menu_assistente_ia,
            "7": self._menu_automacao,
            "0": self._sair,
        }
        acao = acoes.get(opcao)
        if acao:
            acao()
        else:
            print("Opção inválida. Tente novamente.")

    def executar(self):
        while self._ativo:
            self._exibir_menu()
            opcao = input("Escolha uma opção: ").strip()
            self._processar_opcao(opcao)

    def _menu_usuarios(self):
        print("\n-- Gerenciar Usuários --")
        print("  [1] Cadastrar usuário")
        print("  [2] Listar usuários")
        print("  [0] Voltar")
        opcao = input("Opção: ").strip()
        if opcao == "1":
            nome = input("Nome: ").strip()
            email = input("E-mail: ").strip()
            try:
                usuario = self._app.servico_usuarios.cadastrar(nome, email)
                print(f"Usuário cadastrado: {usuario}")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "2":
            usuarios = self._app.servico_usuarios.listar()
            if usuarios:
                for u in usuarios:
                    print(f"  {u}")
            else:
                print("Nenhum usuário cadastrado.")

    def _menu_tarefas(self):
        print("\n-- Gerenciar Tarefas --")
        print("  [1] Criar tarefa")
        print("  [2] Listar tarefas")
        print("  [0] Voltar")
        opcao = input("Opção: ").strip()
        if opcao == "1":
            titulo = input("Título: ").strip()
            descricao = input("Descrição: ").strip()
            tarefa = self._app.servico_tarefas.criar(titulo, descricao)
            print(f"Tarefa criada: {tarefa}")
        elif opcao == "2":
            tarefas = self._app.servico_tarefas.listar()
            if tarefas:
                for t in tarefas:
                    print(f"  {t}")
            else:
                print("Nenhuma tarefa cadastrada.")

    def _menu_agendamentos(self):
        print("\n-- Agendamentos --")
        print("  [1] Agendar item")
        print("  [2] Listar agendamentos")
        print("  [0] Voltar")
        opcao = input("Opção: ").strip()
        if opcao == "1":
            titulo = input("Título: ").strip()
            horario = input("Horário (AAAA-MM-DD HH:MM): ").strip()
            try:
                item = self._app.servico_agendamento.agendar(titulo, horario)
                print(f"Agendado: {item}")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "2":
            agendamentos = self._app.servico_agendamento.listar()
            if agendamentos:
                for a in agendamentos:
                    print(f"  {a}")
            else:
                print("Nenhum agendamento encontrado.")

    def _menu_notificacoes(self):
        print("\n-- Notificações --")
        nao_lidas = self._app.servico_notificacoes.listar_nao_lidas()
        if nao_lidas:
            print(f"Você tem {len(nao_lidas)} notificação(ões) não lida(s):")
            for n in nao_lidas:
                print(f"  [{n.tipo.upper()}] {n.mensagem}")
        else:
            print("Nenhuma notificação não lida.")

    def _menu_clima(self):
        print("\n-- Clima --")
        cidade = input("Informe a cidade: ").strip()
        dados = self._app.servico_clima.buscar_clima_atual(cidade)
        print(f"Cidade: {dados['cidade']}")
        print(f"Temperatura: {dados['temperatura']}")
        print(f"Descrição: {dados['descricao']}")

    def _menu_assistente_ia(self):
        print("\n-- Assistente IA -- (digite 'sair' para voltar)")
        while True:
            mensagem = input("Você: ").strip()
            if mensagem.lower() == "sair":
                break
            resposta = self._app.servico_assistente_ia.perguntar(mensagem)
            print(f"Assistente: {resposta}")

    def _menu_automacao(self):
        print("\n-- Regras de Automação --")
        regras = self._app.servico_automacao.listar_regras()
        if regras:
            for r in regras:
                estado = "ativa" if r.ativa else "inativa"
                print(f"  {r} [{estado}]")
        else:
            print("Nenhuma regra cadastrada.")

    def _sair(self):
        print("Encerrando a aplicação. Até mais!")
        self._ativo = False
