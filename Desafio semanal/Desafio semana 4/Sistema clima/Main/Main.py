from Frases import FRASES_CLIMA
import customtkinter as ctk
from API.APIClima import buscar_clima, buscar_previsao_proximos_dias

ctk.set_appearance_mode('dark')


class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.resizable(False, False)
        self.title("Sistema de Clima Devs")
        
        self.cidade_atual = "" 

        self.frame_telaInicial = FrameTelaInicial(self)
        self.frame_verClima = FrameVerClima(self)
        self.frame_proximosDias = FrameProximosDias(self)

        self.frame_telaInicial.pack(fill="both", expand=True)

    def mostrar_clima(self):
        self.frame_telaInicial.pack_forget()
        self.frame_verClima.pack(fill="both", expand=True)
    
    def mostrar_proximos_dias(self):
        self.frame_verClima.pack_forget()
        self.frame_proximosDias.pack(fill="both", expand=True)
    
    def voltar_para_clima_atual(self):
        self.frame_proximosDias.pack_forget()
        self.frame_verClima.pack(fill="both", expand=True)
    
    def botao_voltar_tela(self):
        self.frame_verClima.pack_forget()
        self.frame_telaInicial.pack(fill="both", expand=True)


class FrameTelaInicial(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_titulo = ctk.CTkLabel(self, text="Tela inicial", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=10)

        self.label_cidade = ctk.CTkLabel(self, text='Sua Cidade:', font=("Arial", 18))
        self.label_cidade.pack(pady=10)

        self.campo_cidade = ctk.CTkEntry(self, placeholder_text='Digite sua cidade')
        self.campo_cidade.pack(pady=10)

        self.botao_chamar_api = ctk.CTkButton(self, text='Visualizar clima', command=self.entrar)
        self.botao_chamar_api.pack(pady=10)

    def entrar(self):
        cidade = self.campo_cidade.get()
        self.master.cidade_atual = cidade
        dados = buscar_clima(cidade)

        self.master.frame_verClima.mostrar_dados(dados)
        self.master.mostrar_clima()
    

class FrameVerClima(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_titulo = ctk.CTkLabel(self, text="Previsão Hoje", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=10)

        self.label_resultadoClima = ctk.CTkLabel(self, text="", font=("Arial", 18), justify="left")
        self.label_resultadoClima.pack(pady=30)

        self.botao_proximos_dias = ctk.CTkButton(self, text="Ver Próximos Dias", command=self.ver_proximos_dias)
        self.botao_proximos_dias.pack(pady=5)

        self.botao_voltar = ctk.CTkButton(self, text="Voltar Tela Inicial", command=self.voltar_tela_inicial)
        
    def mostrar_dados(self, dados):
        descricao = dados["descricao"].lower()
        frase = FRASES_CLIMA.get(descricao, "Clima Desconhecido... Mas as contas não se pagam sozinhas")

        resultado = f"""
Cidade: {dados['cidade']}
Temperatura: {dados['temperatura']}°C
Descrição: {dados['descricao']}
Umidade: {dados['umidade']}%

Conselho do Amigão:
{frase}
"""

        self.label_resultadoClima.configure(text=resultado)

        print(f"Frase sistema: {frase}")

        self.botao_voltar.pack(pady=5)
    
    def ver_proximos_dias(self):
        cidade = self.master.cidade_atual
        previsoes = buscar_previsao_proximos_dias(cidade)
        self.master.frame_proximosDias.carregar_previsoes(previsoes)
        self.master.mostrar_proximos_dias()

    def voltar_tela_inicial(self):
        self.master.botao_voltar_tela()


class FrameProximosDias(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.previsoes = []
        self.dia_atual_index = 0
        
        self.label_titulo = ctk.CTkLabel(self, text="Previsão dos Próximos Dias", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=10)
        
        self.label_previsao = ctk.CTkLabel(self, text="", font=("Arial", 15), justify="left")
        self.label_previsao.pack(pady=10)
        
        self.frame_botoes = ctk.CTkFrame(self)
        self.frame_botoes.pack(pady=10)
        
        self.botao_dia_anterior = ctk.CTkButton(self.frame_botoes, text="← Dia Anterior", command=self.dia_anterior, width=100)
        self.botao_dia_anterior.grid(row=0, column=0, padx=10)
        
        self.botao_avancar_dia = ctk.CTkButton(self.frame_botoes, text="Avançar Dia →", command=self.avancar_dia, width=100)
        self.botao_avancar_dia.grid(row=0, column=1, padx=10)
        
        self.botao_voltar = ctk.CTkButton(self, text="Voltar para Clima Atual", command=self.voltar_clima_atual)
        self.botao_voltar.pack(pady=10)
    
    def carregar_previsoes(self, previsoes):
        """Carrega as previsões e mostra o primeiro dia"""
        self.previsoes = previsoes
        self.dia_atual_index = 0
        self.mostrar_dia_atual()
    
    def mostrar_dia_atual(self):
        """Mostra os dados do dia atual selecionado"""
        if not self.previsoes:
            self.label_previsao.configure(text="Nenhuma previsão disponível")
            return
        
        dia = self.previsoes[self.dia_atual_index]
        
        dias_semana = {
            "Monday": "Segunda-feira",
            "Tuesday": "Terça-feira",
            "Wednesday": "Quarta-feira",
            "Thursday": "Quinta-feira",
            "Friday": "Sexta-feira",
            "Saturday": "Sábado",
            "Sunday": "Domingo"
        }
        
        dia_semana = dias_semana.get(dia["dia_semana"], dia["dia_semana"])
        
        descricao = dia["descricao"].lower()
        frase = FRASES_CLIMA.get(descricao, "Clima Desconhecido... Mas as contas não se pagam sozinhas")
        
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
        
        self.botao_dia_anterior.configure(state="normal" if self.dia_atual_index > 0 else "disabled")
        self.botao_avancar_dia.configure(state="normal" if self.dia_atual_index < len(self.previsoes) - 1 else "disabled")
    
    def avancar_dia(self):
        """Avança para o próximo dia"""
        if self.dia_atual_index < len(self.previsoes) - 1:
            self.dia_atual_index += 1
            self.mostrar_dia_atual()
    
    def dia_anterior(self):
        """Volta para o dia anterior"""
        if self.dia_atual_index > 0:
            self.dia_atual_index -= 1
            self.mostrar_dia_atual()
    
    def voltar_clima_atual(self):
        """Volta para a tela do clima atual"""
        self.master.voltar_para_clima_atual()
    
    

programa = Interface()
programa.mainloop()

print("Finalizando programa...")
