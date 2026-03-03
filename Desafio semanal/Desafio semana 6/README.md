# Rotina Inteligente

**Projeto desenvolvido durante o Desafio de 50 Dias de Código - Semana 6**

Sistema modular de gerenciamento de rotina com interface gráfica moderna (dark mode), suporte a tarefas, agendamento, clima, notificações e automação de regras.

---

## Funcionalidades

- Interface gráfica com CustomTkinter (dark mode)
- Gerenciamento de tarefas com prioridade e status
- Agendamento de atividades
- Histórico de notificações
- Consulta e adaptação de rotina ao clima
- Automação por regras configuráveis
- Resumo diário com sugestões do assistente IA
- Persistência de dados em arquivo JSON

---

## Estrutura dos Módulos

| Módulo             | Responsabilidade                              |
|--------------------|-----------------------------------------------|
| `nucleo`           | Configurações centrais do sistema             |
| `tarefas`          | Criação e gestão de tarefas                   |
| `agendamento`      | Criação e gestão de agendamentos              |
| `notificacoes`     | Envio e histórico de notificações             |
| `clima`            | Consulta climática e adaptação de rotina      |
| `usuarios`         | Cadastro e gestão de usuários                 |
| `interface`        | Interface gráfica com CustomTkinter           |
| `assistente_ia`    | Sugestões inteligentes e resumo diário        |
| `automacao_regras` | Criação e execução de regras de automação     |
| `persistencia`     | Leitura e escrita de dados em arquivo JSON    |
| `database`         | Módulo auxiliar de banco de dados             |

---

## Tecnologias Utilizadas

| Tecnologia      | Versão  | Uso                     |
|-----------------|---------|-------------------------|
| **Python**      | 3.10+   | Linguagem principal     |
| **CustomTkinter** | 5.2.2 | Interface gráfica moderna |

---

## Instalação

```bash
cd "Rotina Inteligente"
pip install -r requirements.txt
```

## Como Executar

```bash
python main.py
```

---

**Contato:** Carlosmanoeldev@outlook.com
