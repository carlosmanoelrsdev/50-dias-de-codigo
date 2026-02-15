# Sistema Clima - Aplicativo de Previsão do Tempo

**Projeto desenvolvido durante o Desafio de 50 Dias de Código - Semana 4**

Este é um aplicativo completo de previsão do tempo com interface gráfica moderna, que integra a API do OpenWeatherMap para fornecer informações climáticas atuais e previsões para os próximos dias.

---

## Sobre o Projeto

O **Sistema Clima** é um aplicativo desktop que consolida os conhecimentos das semanas anteriores do desafio:
- **Semana 1-2**: Fundamentos de Python e estruturas de dados
- **Semana 3**: Consumo e integração com APIs externas
- **Semana 4**: Projeto completo com interface gráfica, POO e organização profissional

### Objetivo

Criar uma aplicação funcional que permita ao usuário consultar informações climáticas de qualquer cidade do mundo, visualizar dados atuais e navegar pela previsão dos próximos 5 dias, tudo em uma interface visual moderna e intuitiva.

---

## Funcionalidades

### Funcionalidades Principais (Obrigatórias)

1. ** Busca de Clima Atual**
   - Pesquisa por nome de cidade
   - Exibição de temperatura, descrição, umidade
   - Tratamento de erros (cidade não encontrada, API inválida, etc.)

2. ** Previsão dos Próximos Dias**
   - Visualização da previsão para os próximos 5 dias
   - Navegação entre dias (avançar/voltar)
   - Temperatura mínima e máxima por dia
   - Informações detalhadas de cada dia

3. ** Frases Motivacionais Personalizadas**
   - Sistema de frases criativas baseadas nas condições climáticas
   - Mais de 15 condições mapeadas
   - Humor e personalidade única para desenvolvedores

### Funcionalidades Extras

-  Interface gráfica moderna (Dark Mode)
-  Sistema de navegação entre telas
-  Feedback visual em todas as operações
-  Tradução automática para português (via API)
-  Organização completa em módulos e pacotes
-  Tratamento robusto de erros
-  Estado desabilitado em botões quando apropriado

---

## Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Python** | 3.10+ | Linguagem principal |
| **CustomTkinter** | 5.2.2 | Interface gráfica moderna |
| **Requests** | 2.32.5 | Requisições HTTP para API |
| **python-dotenv** | 1.2.1 | Gerenciamento de variáveis de ambiente |
| **OpenWeatherMap API** | v2.5 | Fonte de dados climáticos |

---


### Organização em Camadas

- **Camada de Apresentação**: `Main.py` - Interface com CustomTkinter (POO)
- **Camada de Serviço**: `APIClima.py` - Lógica de negócio e integração com API
- **Camada de Dados**: `frases_clima.py` - Base de dados de conteúdo

---

## Instalação

### Pré-requisitos

- Python 3.10 ou superior
- Chave de API do OpenWeatherMap (gratuita)

### Passo a Passo

1. **Clone ou baixe o repositório**

```bash
git clone <https://github.com/carlosmanoelrsdev/50-dias-de-codigo>
cd "Sistema clima"
```

2. **Crie um ambiente virtual**

```bash
python -m venv .venv
```

3. **Ative o ambiente virtual**

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

4. **Instale as dependências**

```bash
pip install -r requirements.txt
```

5. **Configure a API Key**

- Crie um arquivo `.env` na raiz do projeto
- Adicione sua chave da OpenWeatherMap:

```env
API_KEY=sua_chave_aqui
```

> **Como obter a API Key:**
> 1. Acesse [OpenWeatherMap](https://openweathermap.org/api)
> 2. Crie uma conta gratuita
> 3. Gere sua API Key no painel
> 4. Cole a chave no arquivo `.env`

---

## Como Usar

1. **Execute o aplicativo**

```bash
python Main/Main.py
```

2. **Tela Inicial**
   - Digite o nome de uma cidade no campo de entrada
   - Clique em "Visualizar clima"

3. **Tela de Clima Atual**
   - Visualize as informações do clima atual
   - Leia a frase motivacional personalizada
   - Clique em "Ver Próximos Dias" para a previsão
   - Ou clique em "Voltar Tela Inicial" para nova busca

4. **Tela de Previsão**
   - Navegue entre os dias usando os botões
   - Veja temperatura mínima/máxima e condições
   - Use "Voltar para Clima Atual" para retornar

---

### Exemplos de Frases por Condição

| Condição | Frase |
|----------|-------|
| Céu limpo | "O sol tá brilhando, DEV! Aproveita antes que o bug apareça." |
| Chuva forte | "Chuva forte! Não saia, DEV, seus circuitos vão fritar!" |
| Trovoada | "Trovoada! Se der tela azul, já sabe o motivo." |
| Névoa | "Névoa densa… igual sua lógica às 3 da manhã." |
| Neblina | "Neblina forte… cuidado pra não confundir variável com função." |

---

## Extras Implementados

### Organização Profissional
- Estrutura modular com separação de responsabilidades
- Uso de pacotes Python (`__init__.py`)
- Código limpo

### Interface Moderna
- Dark mode por padrão
- Layout responsivo e intuitivo
- Feedback visual (botões desabilitados quando apropriado)
- Navegação fluida entre telas

### Programação Orientada a Objetos
- 4 classes principais: `Interface`, `FrameTelaInicial`, `FrameVerClima`, `FrameProximosDias`
- Herança de `ctk.CTkFrame` e `ctk.CTk`
- Encapsulamento de lógica

### Tratamento de Erros Robusto
- Cidade não encontrada (404)
- API Key inválida (401)
- Limite de requisições excedido (429)
- Erros desconhecidos com código de status

### Manipulação Avançada de Dados
- Conversão de Kelvin para Celsius
- Agrupamento de previsões por dia
- Cálculo de temperaturas mínimas e máximas
- Formatação de datas e dias da semana
---

### Técnicos
-  Integração com APIs REST
-  Manipulação de JSON
-  Criação de interfaces gráficas com CustomTkinter
-  Programação Orientada a Objetos em Python
-  Gerenciamento de estados e navegação entre telas
-  Tratamento de exceções e erros de API
-  Organização de projetos em módulos

### Soft Skills
-  Planejamento de arquitetura de software
-  Documentação técnica
-  Resolução de problemas
-  Atenção aos detalhes (UX/UI)

---

## Autor

**Contato:** [Carlosmanoeldev@outlook.com]

---

## Entrega - Semana 4

### Resumo
Implementei um **Sistema Completo de Previsão do Tempo** com interface gráfica moderna. O projeto consome a API do OpenWeatherMap para exibir clima atual e previsão de 5 dias, com sistema personalizado de frases motivacionais para desenvolvedores. Organizei o código usando POO com 4 classes principais, separação em módulos (API, Frases, Interface) e tratamento robusto de erros.

### Funcionalidades Implementadas
1.  **Integração com API** - OpenWeatherMap (clima atual + previsão 5 dias)
2.  **Manipulação de Dados** - Conversão de temperatura, agrupamento por dia, filtros
3.  **Interface Gráfica** - CustomTkinter com 3 telas navegáveis e dark mode
4.  **Sistema de Frases** - 15+ mensagens personalizadas por condição climática

### Extras
-  **POO**: 4 classes com herança e encapsulamento
-  **Arquitetura**: Organização em camadas (Apresentação/Serviço/Dados)
-  **Tratamento de Erros**: Códigos 404, 401, 429 e desconhecidos
-  **UX**: Navegação entre dias, botões com estados, feedback visual
-  **README Completo**: Documentação profissional com instruções detalhadas

### Repositório
https://github.com/carlosmanoelrsdev/50-dias-de-codigo

---
