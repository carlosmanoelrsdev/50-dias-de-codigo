# Rotina Inteligente - Gerenciador de Rotina com Automação

**Projeto desenvolvido durante o Desafio de 50 Dias de Código - Semana 6**

Aplicativo de terminal para gerenciar sua rotina diária com agendamento de tarefas,
regras de automação baseadas no clima e sistema de lembretes.

---

## Sobre o Projeto

O **Rotina Inteligente** consolida os conhecimentos das semanas anteriores:
- **Semanas 1-2**: Fundamentos de Python, POO e estruturas de dados
- **Semanas 3-5**: Integração com APIs, interface gráfica e organização em módulos
- **Semana 6**: Banco de dados SQLite, regras de automação e arquitetura modular

### Objetivo

Criar um sistema de rotina pessoal que permita cadastrar tarefas recorrentes,
verificar o que está agendado para o dia, receber lembretes no horário certo
e obter sugestões automáticas baseadas nas condições climáticas.

---

## Funcionalidades

### Funcionalidades Principais

1. **Gerenciamento de Tarefas**
   - Criar, listar, atualizar e remover tarefas
   - Categorias (saúde, trabalho, lazer, geral)
   - Agendamento por hora e dias da semana

2. **Agendamento Inteligente**
   - Exibe as tarefas do dia atual automaticamente
   - Filtra por dia da semana em tempo real

3. **Sistema de Lembretes**
   - Verifica tarefas agendadas para o horário atual
   - Notificações no terminal

4. **Regras de Automação Climática**
   - Regras padrão para diferentes condições (chuva, frio, ensolarado, nublado)
   - Possibilidade de adicionar regras personalizadas
   - Avaliação automática das regras com base no clima

5. **Persistência com SQLite**
   - Tarefas e regras salvas em banco de dados local
   - Dados mantidos entre sessões

---

## Estrutura do Projeto

```
Rotina Inteligente/
├── main.py                    # Ponto de entrada
├── nucleo/                    # Orquestrador principal
├── interface/                 # Menus e interação com usuário
├── tarefas/                   # Modelo e CRUD de tarefas
├── agendamento/               # Lógica de agendamento por dia/hora
├── clima/                     # Dados climáticos (simulados)
├── automacao_regras/          # Motor de regras climáticas
├── notificacoes/              # Sistema de lembretes
└── database/                  # Camada de persistência SQLite
```

---

## Como Executar

```bash
cd "Rotina Inteligente"
python main.py
```

Não há dependências externas. Utiliza apenas a biblioteca padrão do Python.

---

## Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| **Python 3.10+** | Linguagem principal |
| **SQLite3** | Banco de dados local |
| **datetime** | Gerenciamento de datas e horários |

---

## Convenções

- Nomes de arquivos e módulos em minúsculo com underscore
- Sem caracteres especiais ou acentos nos identificadores
- Cada módulo tem responsabilidade única (princípio SRP)
