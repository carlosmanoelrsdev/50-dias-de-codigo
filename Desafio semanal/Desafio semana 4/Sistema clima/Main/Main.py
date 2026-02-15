from Frases import FRASES_CLIMA
import customtkinter as ctk
from API.APIClima import buscar_clima

ctk.set_appearance_mode('dark')


class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.resizable(False, False)
        self.title("Sistema de Clima Devs")

        self.frame_telaInicial = FrameTelaInicial(self)
        self.frame_verClima = FrameVerClima(self)

        self.frame_telaInicial.pack(fill="both", expand=True)

    def mostrar_clima(self):
        self.frame_telaInicial.pack_forget()
        self.frame_verClima.pack(fill="both", expand=True)
    
    def botao_voltar_tela(self):
        self.frame_verClima.pack_forget()
        self.frame_telaInicial.pack(fill="both", expand=True)


class FrameTelaInicial(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_cidade = ctk.CTkLabel(self,text='Sua Cidade:')
        self.label_cidade.pack(pady=10)

        self.campo_cidade = ctk.CTkEntry(self, placeholder_text='Digite sua cidade')
        self.campo_cidade.pack(pady=10)

        self.botao_chamar_api = ctk.CTkButton(self, text='Visualizar clima', command=self.entrar)
        self.botao_chamar_api.pack(pady=10)

    def entrar(self):
        cidade = self.campo_cidade.get()
        dados = buscar_clima(cidade)

        self.master.frame_verClima.mostrar_dados(dados)
        self.master.mostrar_clima()
        print("entrou")
    

class FrameVerClima(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_resultadoClima = ctk.CTkLabel(self, text="", font=("Arial", 18), justify="left")
        self.label_resultadoClima.pack(pady=50)

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
        print(frase)
        self.botao_voltar.pack(pady=10)

    def voltar_tela_inicial(self):
        self.master.botao_voltar_tela()
    
    

programa = Interface()
programa.mainloop()

