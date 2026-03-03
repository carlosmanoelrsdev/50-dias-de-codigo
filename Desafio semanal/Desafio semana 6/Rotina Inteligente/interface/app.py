import customtkinter as ctk

ctk.set_appearance_mode("dark")


# Tela principal com barra lateral de navegação e área de conteúdo
class Interface(ctk.CTk):
    def __init__(self, servico_tarefas, servico_agendamento, servico_notificacoes,
                 servico_clima, servico_automacao, assistente):
        super().__init__()
        self.title("Rotina Inteligente")
        self.geometry("900x600")
        self.resizable(False, False)

        # Serviços compartilhados entre os frames
        self.servico_tarefas = servico_tarefas
        self.servico_agendamento = servico_agendamento
        self.servico_notificacoes = servico_notificacoes
        self.servico_clima = servico_clima
        self.servico_automacao = servico_automacao
        self.assistente = assistente

        # Barra lateral
        self.frame_sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.frame_sidebar.pack(side="left", fill="y")
        self.frame_sidebar.pack_propagate(False)

        ctk.CTkLabel(
            self.frame_sidebar, text="Rotina\nInteligente",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        # Botões de navegação
        self.botoes_nav = {}
        secoes = [
            ("Tarefas", self.mostrar_tarefas),
            ("Agendamento", self.mostrar_agendamento),
            ("Notificações", self.mostrar_notificacoes),
            ("Clima", self.mostrar_clima),
            ("Automação", self.mostrar_automacao),
            ("Resumo do Dia", self.mostrar_resumo),
        ]
        for nome, comando in secoes:
            btn = ctk.CTkButton(
                self.frame_sidebar, text=nome, command=comando,
                width=160, height=40, anchor="w"
            )
            btn.pack(pady=5, padx=20)
            self.botoes_nav[nome] = btn

        # Área de conteúdo
        self.frame_tarefas = FrameTarefas(self)
        self.frame_agendamento = FrameAgendamento(self)
        self.frame_notificacoes = FrameNotificacoes(self)
        self.frame_clima = FrameClima(self)
        self.frame_automacao = FrameAutomacao(self)
        self.frame_resumo = FrameResumo(self)

        self.frame_atual = None
        self.mostrar_tarefas()

    def _trocar_frame(self, novo_frame):
        if self.frame_atual:
            self.frame_atual.pack_forget()
        novo_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        self.frame_atual = novo_frame

    def mostrar_tarefas(self):
        self._trocar_frame(self.frame_tarefas)
        self.frame_tarefas.atualizar_lista()

    def mostrar_agendamento(self):
        self._trocar_frame(self.frame_agendamento)
        self.frame_agendamento.atualizar_lista()

    def mostrar_notificacoes(self):
        self._trocar_frame(self.frame_notificacoes)
        self.frame_notificacoes.atualizar_lista()

    def mostrar_clima(self):
        self._trocar_frame(self.frame_clima)

    def mostrar_automacao(self):
        self._trocar_frame(self.frame_automacao)
        self.frame_automacao.atualizar_lista()

    def mostrar_resumo(self):
        self._trocar_frame(self.frame_resumo)
        self.frame_resumo.atualizar_resumo()


# Tela de gerenciamento de tarefas
class FrameTarefas(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Gerenciar Tarefas", font=("Arial", 18, "bold")).pack(pady=10)

        # Formulário de criação
        frame_form = ctk.CTkFrame(self)
        frame_form.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Título:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entrada_titulo = ctk.CTkEntry(frame_form, width=220, placeholder_text="Título da tarefa")
        self.entrada_titulo.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Prioridade:").grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.combo_prioridade = ctk.CTkComboBox(frame_form, values=["baixa", "normal", "alta"], width=120)
        self.combo_prioridade.set("normal")
        self.combo_prioridade.grid(row=0, column=3, padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Descrição:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entrada_descricao = ctk.CTkEntry(frame_form, width=220, placeholder_text="Descrição (opcional)")
        self.entrada_descricao.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkButton(frame_form, text="Criar Tarefa", command=self.criar_tarefa, width=120).grid(
            row=1, column=3, padx=10, pady=5
        )

        # Atualização de status
        frame_status = ctk.CTkFrame(self)
        frame_status.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(frame_status, text="ID:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entrada_id = ctk.CTkEntry(frame_status, width=60, placeholder_text="ID")
        self.entrada_id.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(frame_status, text="Novo status:").grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.combo_status = ctk.CTkComboBox(
            frame_status, values=["pendente", "em andamento", "concluído"], width=160
        )
        self.combo_status.set("pendente")
        self.combo_status.grid(row=0, column=3, padx=10, pady=5)

        ctk.CTkButton(frame_status, text="Atualizar", command=self.atualizar_status, width=100).grid(
            row=0, column=4, padx=5, pady=5
        )
        ctk.CTkButton(
            frame_status, text="Remover", command=self.remover_tarefa, width=100, fg_color="#c0392b"
        ).grid(row=0, column=5, padx=5, pady=5)

        # Label de feedback
        self.label_feedback = ctk.CTkLabel(self, text="", text_color="gray")
        self.label_feedback.pack(pady=2)

        # Lista de tarefas
        self.frame_lista = ctk.CTkScrollableFrame(self, label_text="Tarefas")
        self.frame_lista.pack(fill="both", expand=True, padx=10, pady=5)

    def _feedback(self, mensagem, cor="green"):
        self.label_feedback.configure(text=mensagem, text_color=cor)

    def criar_tarefa(self):
        titulo = self.entrada_titulo.get().strip()
        if not titulo:
            self._feedback("O título é obrigatório!", "red")
            return
        descricao = self.entrada_descricao.get().strip()
        prioridade = self.combo_prioridade.get()
        tarefa = self.master.servico_tarefas.criar_tarefa(titulo, descricao, prioridade)
        self.master.servico_notificacoes.enviar(f"Tarefa '{tarefa.titulo}' criada (ID {tarefa.id}).")
        self.entrada_titulo.delete(0, "end")
        self.entrada_descricao.delete(0, "end")
        self._feedback(f"Tarefa '{tarefa.titulo}' criada com ID {tarefa.id}.")
        self.atualizar_lista()

    def atualizar_status(self):
        try:
            id = int(self.entrada_id.get().strip())
        except ValueError:
            self._feedback("ID inválido!", "red")
            return
        novo_status = self.combo_status.get()
        tarefa = self.master.servico_tarefas.atualizar_tarefa(id, status=novo_status)
        if tarefa:
            self._feedback(f"Tarefa ID {id} atualizada para '{novo_status}'.")
        else:
            self._feedback(f"Tarefa ID {id} não encontrada.", "red")
        self.atualizar_lista()

    def remover_tarefa(self):
        try:
            id = int(self.entrada_id.get().strip())
        except ValueError:
            self._feedback("ID inválido!", "red")
            return
        if self.master.servico_tarefas.remover_tarefa(id):
            self._feedback(f"Tarefa ID {id} removida.")
        else:
            self._feedback(f"Tarefa ID {id} não encontrada.", "red")
        self.atualizar_lista()

    def atualizar_lista(self):
        for widget in self.frame_lista.winfo_children():
            widget.destroy()
        tarefas = self.master.servico_tarefas.listar_tarefas()
        if not tarefas:
            ctk.CTkLabel(self.frame_lista, text="Nenhuma tarefa cadastrada.").pack(pady=10)
            return
        cores_prioridade = {"alta": "#e74c3c", "normal": "#3498db", "baixa": "#2ecc71"}
        for t in tarefas:
            cor = cores_prioridade.get(t.prioridade, "#3498db")
            texto = f"ID: {t.id}  |  {t.titulo}  |  Prioridade: {t.prioridade}  |  Status: {t.status}"
            ctk.CTkLabel(
                self.frame_lista, text=texto, fg_color=cor,
                corner_radius=6, anchor="w", padx=10
            ).pack(fill="x", padx=5, pady=3)


# Tela de agendamentos
class FrameAgendamento(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Agendamentos", font=("Arial", 18, "bold")).pack(pady=10)

        frame_form = ctk.CTkFrame(self)
        frame_form.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Título:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entrada_titulo = ctk.CTkEntry(frame_form, width=220, placeholder_text="Título do agendamento")
        self.entrada_titulo.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Data/Hora:").grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.entrada_data = ctk.CTkEntry(frame_form, width=160, placeholder_text="dd/mm/aaaa hh:mm")
        self.entrada_data.grid(row=0, column=3, padx=10, pady=5)

        ctk.CTkButton(frame_form, text="Agendar", command=self.criar_agendamento, width=120).grid(
            row=0, column=4, padx=10, pady=5
        )

        # Cancelar agendamento
        frame_cancelar = ctk.CTkFrame(self)
        frame_cancelar.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(frame_cancelar, text="ID para cancelar:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entrada_id = ctk.CTkEntry(frame_cancelar, width=80, placeholder_text="ID")
        self.entrada_id.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkButton(
            frame_cancelar, text="Cancelar Agendamento", command=self.cancelar_agendamento,
            width=180, fg_color="#c0392b"
        ).grid(row=0, column=2, padx=10, pady=5)

        self.label_feedback = ctk.CTkLabel(self, text="", text_color="gray")
        self.label_feedback.pack(pady=2)

        self.frame_lista = ctk.CTkScrollableFrame(self, label_text="Agendamentos")
        self.frame_lista.pack(fill="both", expand=True, padx=10, pady=5)

    def _feedback(self, mensagem, cor="green"):
        self.label_feedback.configure(text=mensagem, text_color=cor)

    def criar_agendamento(self):
        titulo = self.entrada_titulo.get().strip()
        data = self.entrada_data.get().strip()
        if not titulo or not data:
            self._feedback("Por favor, preencha o título e a data/hora.", "red")
            return
        a = self.master.servico_agendamento.criar_agendamento(titulo, data)
        self.master.servico_notificacoes.enviar(f"Agendamento '{a.titulo}' criado (ID {a.id}).")
        self.entrada_titulo.delete(0, "end")
        self.entrada_data.delete(0, "end")
        self._feedback(f"Agendamento '{a.titulo}' criado com ID {a.id}.")
        self.atualizar_lista()

    def cancelar_agendamento(self):
        try:
            id = int(self.entrada_id.get().strip())
        except ValueError:
            self._feedback("ID inválido!", "red")
            return
        if self.master.servico_agendamento.cancelar_agendamento(id):
            self._feedback(f"Agendamento ID {id} cancelado.")
        else:
            self._feedback(f"Agendamento ID {id} não encontrado.", "red")
        self.atualizar_lista()

    def atualizar_lista(self):
        for widget in self.frame_lista.winfo_children():
            widget.destroy()
        agendamentos = self.master.servico_agendamento.listar_agendamentos()
        if not agendamentos:
            ctk.CTkLabel(self.frame_lista, text="Nenhum agendamento cadastrado.").pack(pady=10)
            return
        for a in agendamentos:
            status_cor = "#2ecc71" if a.ativo else "#7f8c8d"
            status_txt = "Ativo" if a.ativo else "Cancelado"
            texto = f"ID: {a.id}  |  {a.titulo}  |  {a.data_hora}  |  {status_txt}"
            ctk.CTkLabel(
                self.frame_lista, text=texto, fg_color=status_cor,
                corner_radius=6, anchor="w", padx=10
            ).pack(fill="x", padx=5, pady=3)


# Tela de notificações
class FrameNotificacoes(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Notificações", font=("Arial", 18, "bold")).pack(pady=10)

        ctk.CTkButton(self, text="Atualizar", command=self.atualizar_lista, width=120).pack(pady=5)

        self.frame_lista = ctk.CTkScrollableFrame(self, label_text="Histórico de Notificações")
        self.frame_lista.pack(fill="both", expand=True, padx=10, pady=5)

    def atualizar_lista(self):
        for widget in self.frame_lista.winfo_children():
            widget.destroy()
        historico = self.master.servico_notificacoes.listar_historico()
        if not historico:
            ctk.CTkLabel(self.frame_lista, text="Nenhuma notificação registrada.").pack(pady=10)
            return
        for n in reversed(historico):
            texto = f"[{n['data_hora']}]  [{n['tipo'].upper()}]  {n['mensagem']}"
            ctk.CTkLabel(
                self.frame_lista, text=texto, fg_color="#2c3e50",
                corner_radius=6, anchor="w", padx=10
            ).pack(fill="x", padx=5, pady=3)


# Tela de consulta de clima
class FrameClima(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Consultar Clima", font=("Arial", 18, "bold")).pack(pady=10)

        frame_busca = ctk.CTkFrame(self)
        frame_busca.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(frame_busca, text="Cidade:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entrada_cidade = ctk.CTkEntry(frame_busca, width=240, placeholder_text="Nome da cidade")
        self.entrada_cidade.grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(frame_busca, text="Buscar", command=self.buscar_clima, width=120).grid(
            row=0, column=2, padx=10, pady=10
        )

        self.frame_resultado = ctk.CTkFrame(self)
        self.frame_resultado.pack(fill="both", expand=True, padx=10, pady=10)

        self.label_resultado = ctk.CTkLabel(
            self.frame_resultado, text="", font=("Arial", 14), justify="left"
        )
        self.label_resultado.pack(pady=20, padx=20, anchor="w")

    def buscar_clima(self):
        cidade = self.entrada_cidade.get().strip()
        if not cidade:
            self.label_resultado.configure(text="Digite o nome de uma cidade.")
            return
        dados = self.master.servico_clima.buscar_clima(cidade)
        sugestao = self.master.servico_clima.adaptar_rotina_ao_clima(dados)
        texto = (
            f"Cidade: {dados['cidade']}\n"
            f"Temperatura: {dados['temperatura']}\n"
            f"Descrição: {dados['descricao']}\n"
            f"Umidade: {dados['umidade']}\n\n"
            f"Sugestão para sua rotina:\n{sugestao}"
        )
        self.label_resultado.configure(text=texto)


# Tela de automação de regras
class FrameAutomacao(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Automação de Regras", font=("Arial", 18, "bold")).pack(pady=10)

        frame_form = ctk.CTkFrame(self)
        frame_form.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entrada_nome = ctk.CTkEntry(frame_form, width=180, placeholder_text="Nome da regra")
        self.entrada_nome.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Condição:").grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.entrada_condicao = ctk.CTkEntry(frame_form, width=160, placeholder_text="ex: chuva")
        self.entrada_condicao.grid(row=0, column=3, padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Ação:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entrada_acao = ctk.CTkEntry(frame_form, width=180, placeholder_text="ex: Evitar sair")
        self.entrada_acao.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkButton(frame_form, text="Criar Regra", command=self.criar_regra, width=120).grid(
            row=1, column=3, padx=10, pady=5
        )

        self.label_feedback = ctk.CTkLabel(self, text="", text_color="gray")
        self.label_feedback.pack(pady=2)

        self.frame_lista = ctk.CTkScrollableFrame(self, label_text="Regras Cadastradas")
        self.frame_lista.pack(fill="both", expand=True, padx=10, pady=5)

    def _feedback(self, mensagem, cor="green"):
        self.label_feedback.configure(text=mensagem, text_color=cor)

    def criar_regra(self):
        nome = self.entrada_nome.get().strip()
        condicao = self.entrada_condicao.get().strip()
        acao = self.entrada_acao.get().strip()
        if not nome or not condicao or not acao:
            self._feedback("Preencha todos os campos!", "red")
            return
        regra = self.master.servico_automacao.criar_regra(nome, condicao, acao)
        self.entrada_nome.delete(0, "end")
        self.entrada_condicao.delete(0, "end")
        self.entrada_acao.delete(0, "end")
        self._feedback(f"Regra '{regra.nome}' criada com ID {regra.id}.")
        self.atualizar_lista()

    def atualizar_lista(self):
        for widget in self.frame_lista.winfo_children():
            widget.destroy()
        regras = self.master.servico_automacao.listar_regras()
        if not regras:
            ctk.CTkLabel(self.frame_lista, text="Nenhuma regra cadastrada.").pack(pady=10)
            return
        for r in regras:
            status_cor = "#2ecc71" if r.ativa else "#7f8c8d"
            texto = f"ID: {r.id}  |  {r.nome}  |  Se '{r.condicao}' → {r.acao}"
            ctk.CTkLabel(
                self.frame_lista, text=texto, fg_color=status_cor,
                corner_radius=6, anchor="w", padx=10
            ).pack(fill="x", padx=5, pady=3)


# Tela de resumo diário gerado pelo assistente IA
class FrameResumo(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Resumo do Dia", font=("Arial", 18, "bold")).pack(pady=10)

        ctk.CTkButton(self, text="Gerar Resumo", command=self.atualizar_resumo, width=160).pack(pady=5)

        self.frame_cards = ctk.CTkFrame(self)
        self.frame_cards.pack(fill="x", padx=20, pady=20)

        self.label_total = ctk.CTkLabel(self.frame_cards, text="", font=("Arial", 14))
        self.label_total.grid(row=0, column=0, padx=30, pady=10)

        self.label_concluidas = ctk.CTkLabel(self.frame_cards, text="", font=("Arial", 14))
        self.label_concluidas.grid(row=0, column=1, padx=30, pady=10)

        self.label_pendentes = ctk.CTkLabel(self.frame_cards, text="", font=("Arial", 14))
        self.label_pendentes.grid(row=0, column=2, padx=30, pady=10)

        self.label_agendamentos = ctk.CTkLabel(self.frame_cards, text="", font=("Arial", 14))
        self.label_agendamentos.grid(row=0, column=3, padx=30, pady=10)

        ctk.CTkLabel(self, text="Sugestões do Assistente:", font=("Arial", 14, "bold")).pack(
            pady=(20, 5), anchor="w", padx=20
        )
        self.frame_sugestoes = ctk.CTkScrollableFrame(self, height=180)
        self.frame_sugestoes.pack(fill="x", padx=20, pady=5)

    def atualizar_resumo(self):
        tarefas = self.master.servico_tarefas.listar_tarefas()
        agendamentos = self.master.servico_agendamento.listar_agendamentos()
        resumo = self.master.assistente.gerar_resumo_diario(tarefas, agendamentos)

        self.label_total.configure(
            text=f"Total de Tarefas\n{resumo['total_tarefas']}",
            fg_color="#2c3e50", corner_radius=8, padx=20, pady=10
        )
        self.label_concluidas.configure(
            text=f"Concluídas\n{resumo['concluidas']}",
            fg_color="#27ae60", corner_radius=8, padx=20, pady=10
        )
        self.label_pendentes.configure(
            text=f"Pendentes\n{resumo['pendentes']}",
            fg_color="#e67e22", corner_radius=8, padx=20, pady=10
        )
        self.label_agendamentos.configure(
            text=f"Agendamentos\n{resumo['agendamentos']}",
            fg_color="#2980b9", corner_radius=8, padx=20, pady=10
        )

        for widget in self.frame_sugestoes.winfo_children():
            widget.destroy()
        sugestoes = self.master.assistente.sugerir_tarefas(tarefas)
        for s in sugestoes:
            ctk.CTkLabel(
                self.frame_sugestoes, text=f"• {s}", anchor="w"
            ).pack(fill="x", padx=5, pady=2)
