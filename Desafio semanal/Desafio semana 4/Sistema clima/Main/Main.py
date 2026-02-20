# Módulos para interface gráfica e requisições climáticas
from Frases import FRASES_CLIMA
import customtkinter as ctk
from API.APIClima import buscar_clima, buscar_previsao_proximos_dias

ctk.set_appearance_mode("dark")

# Interface principal responsável por gerenciar a navegação entre telas
class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.resizable(False, False)
        self.title("Sistema de Clima Devs")

        # Armazena a cidade para compartilhar dados entre os frames
        self.cidade_atual = ""

        # Inicializa os três estados principais da aplicação
        self.frame_telaInicial = FrameTelaInicial(self)
        self.frame_verClima = FrameVerClima(self)
        self.frame_proximosDias = FrameProximosDias(self)

        self.frame_telaInicial.pack(fill="both", expand=True)

    def mostrar_clima(self):
        """Navega para a tela de clima atual"""
        self.frame_telaInicial.pack_forget()
        self.frame_verClima.pack(fill="both", expand=True)

    def mostrar_proximos_dias(self):
        """Navega para a tela de previsão dos próximos dias"""
        self.frame_verClima.pack_forget()
        self.frame_proximosDias.pack(fill="both", expand=True)

    def voltar_para_clima_atual(self):
        """Retorna da tela de próximos dias para o clima atual"""
        self.frame_proximosDias.pack_forget()
        self.frame_verClima.pack(fill="both", expand=True)

    def botao_voltar_tela(self):
        """Retorna à tela inicial"""
        self.frame_verClima.pack_forget()
        self.frame_telaInicial.pack(fill="both", expand=True)


# Tela inicial para capturar entrada do usuário
# Responsabilidade: Coletar o nome da cidade e requisitar dados climáticos
class FrameTelaInicial(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_titulo = ctk.CTkLabel(
            self, text="Tela inicial", font=("Arial", 20, "bold")
        )
        self.label_titulo.pack(pady=10)

        self.label_cidade = ctk.CTkLabel(self, text="Sua Cidade:", font=("Arial", 18))
        self.label_cidade.pack(pady=10)

        # Campo de entrada para o usuário digitar a cidade
        self.campo_cidade = ctk.CTkEntry(self, placeholder_text="Digite sua cidade")
        self.campo_cidade.pack(pady=10)

        # Botão que dispara a busca de dados climáticos
        self.botao_chamar_api = ctk.CTkButton(
            self, text="Visualizar clima", command=self.entrar
        )
        self.botao_chamar_api.pack(pady=10)

    def entrar(self):
        """Busca o clima da cidade inserida e navega para a tela de resultado"""
        cidade = self.campo_cidade.get()
        # Armazena para permitir acesso em outras telas
        self.master.cidade_atual = cidade
        # Busca dados da API OpenWeather
        dados = buscar_clima(cidade)

        # Passa dados para o frame de visualização
        self.master.frame_verClima.mostrar_dados(dados)
        # Navega automaticamente para mostrar os resultados
        self.master.mostrar_clima()


# Tela de visualização do clima atual
# Responsabilidade: Exibir dados climáticos do dia e permitir navegação
class FrameVerClima(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_titulo = ctk.CTkLabel(
            self, text="Previsão Hoje", font=("Arial", 20, "bold")
        )
        self.label_titulo.pack(pady=10)

        # Exibe os dados climáticos e frase personalizada
        self.label_resultadoClima = ctk.CTkLabel(
            self, text="", font=("Arial", 18), justify="left"
        )
        self.label_resultadoClima.pack(pady=30)

        # Botão para expandir visualização para próximos dias
        self.botao_proximos_dias = ctk.CTkButton(
            self, text="Ver Próximos Dias", command=self.ver_proximos_dias
        )
        self.botao_proximos_dias.pack(pady=5)

        # Botão para retornar à busca inicial
        self.botao_voltar = ctk.CTkButton(
            self, text="Voltar Tela Inicial", command=self.voltar_tela_inicial
        )

    def mostrar_dados(self, dados):
        """Formata e exibe os dados climáticos com mensagem personalizada"""
        descricao = dados["descricao"].lower()
        # Busca frase temática correspondente ao clima, com fallback
        frase = FRASES_CLIMA.get(
            descricao, "Clima Desconhecido... Mas as contas não se pagam sozinhas"
        )

        # Formata os dados em texto legível para o usuário
        resultado = f"""
Cidade: {dados['cidade']}
Temperatura: {dados['temperatura']}°C
Descrição: {dados['descricao']}
Umidade: {dados['umidade']}%

Conselho do Amigão:
{frase}
"""

        self.label_resultadoClima.configure(text=resultado)
        self.botao_voltar.pack(pady=5)

    def ver_proximos_dias(self):
        """Carrega previsão dos próximos dias e navega para o frame correspondente"""
        cidade = self.master.cidade_atual
        previsoes = buscar_previsao_proximos_dias(cidade)
        self.master.frame_proximosDias.carregar_previsoes(previsoes)
        self.master.mostrar_proximos_dias()

    def voltar_tela_inicial(self):
        """Retorna à tela inicial para nova busca"""
        self.master.botao_voltar_tela()


# Tela de navegação entre previsões diárias
# Responsabilidade: Exibir previsão para um dia e permitir navegação entre dias
class FrameProximosDias(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Armazena lista de previsões e índice do dia atual
        self.previsoes = []
        self.dia_atual_index = 0

        # Componentes visuais
        self.label_titulo = ctk.CTkLabel(
            self, text="Previsão dos Próximos Dias", font=("Arial", 20, "bold")
        )
        self.label_titulo.pack(pady=10)

        # Exibe dados da previsão do dia selecionado
        self.label_previsao = ctk.CTkLabel(
            self, text="", font=("Arial", 18), justify="left"
        )
        self.label_previsao.pack(pady=10)

        # Container para botões de navegação
        self.frame_botoes = ctk.CTkFrame(self)
        self.frame_botoes.pack(pady=10)

        # Botão para retroceder dias
        self.botao_dia_anterior = ctk.CTkButton(
            self.frame_botoes,
            text="← Dia Anterior",
            command=self.dia_anterior,
            width=100,
        )
        self.botao_dia_anterior.grid(row=0, column=0, padx=10)

        # Botão para avançar dias
        self.botao_avancar_dia = ctk.CTkButton(
            self.frame_botoes, text="Avançar Dia →", command=self.avancar_dia, width=100
        )
        self.botao_avancar_dia.grid(row=0, column=1, padx=10)

        # Botão para voltar aos dados do clima atual
        self.botao_voltar = ctk.CTkButton(
            self, text="Voltar para Clima Atual", command=self.voltar_clima_atual
        )
        self.botao_voltar.pack(pady=10)

    def carregar_previsoes(self, previsoes):
        """Carrega as previsões e inicia exibição no primeiro dia"""
        self.previsoes = previsoes
        self.dia_atual_index = 0
        self.mostrar_dia_atual()

    def mostrar_dia_atual(self):
        """Exibe previsão do dia selecionado e atualiza estado dos botões"""
        if not self.previsoes:
            self.label_previsao.configure(text="Nenhuma previsão disponível")
            return

        dia = self.previsoes[self.dia_atual_index]

        # Mapeia dia da semana do inglês (retornado pela API) para português
        dias_semana = {
            "Monday": "Segunda-feira",
            "Tuesday": "Terça-feira",
            "Wednesday": "Quarta-feira",
            "Thursday": "Quinta-feira",
            "Friday": "Sexta-feira",
            "Saturday": "Sábado",
            "Sunday": "Domingo",
        }

        dia_semana = dias_semana.get(dia["dia_semana"], dia["dia_semana"])

        descricao = dia["descricao"].lower()
        # Busca mensagem personalizada para o tipo de clima
        frase = FRASES_CLIMA.get(
            descricao, "Clima Desconhecido... Mas as contas não se pagam sozinhas"
        )

        texto = f"""
{dia_semana} - {dia['data']}
Cidade: {dia['cidade']}

Temperatura Mínima: {dia['temp_min']:.1f}°C
Temperatura Máxima: {dia['temp_max']:.1f}°C
Descrição: {dia['descricao']}
Umidade: {dia['umidade']}%

Conselho do Amigão:
{frase}

Dia {self.dia_atual_index + 1} de {len(self.previsoes)}
"""

        self.label_previsao.configure(text=texto)

        # Ativa/desativa botões conforme posição no array de previsões
        self.botao_dia_anterior.configure(
            state="normal" if self.dia_atual_index > 0 else "disabled"
        )
        self.botao_avancar_dia.configure(
            state=(
                "normal"
                if self.dia_atual_index < len(self.previsoes) - 1
                else "disabled"
            )
        )

    def avancar_dia(self):
        """Avança para o próximo dia se disponível"""
        if self.dia_atual_index < len(self.previsoes) - 1:
            self.dia_atual_index += 1
            self.mostrar_dia_atual()

    def dia_anterior(self):
        """Retrocede para o dia anterior se disponível"""
        if self.dia_atual_index > 0:
            self.dia_atual_index -= 1
            self.mostrar_dia_atual()

    def voltar_clima_atual(self):
        """Retorna à tela de clima atual"""
        self.master.voltar_para_clima_atual()


# Inicia e executa a aplicação
programa = Interface()
programa.mainloop()

print("Finalizando programa...")
