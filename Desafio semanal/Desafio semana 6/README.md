# Rotina Inteligente

**Projeto desenvolvido durante o Desafio de 50 Dias de Código - Semana 6**

Sistema modular de gerenciamento de rotina com suporte a tarefas, agendamento, clima, notificações e automação de regras.

---

## Funcionalidades

- Gerenciamento de tarefas com prioridade e status
- Agendamento de atividades
- Notificações com histórico
- Consulta e adaptação de rotina ao clima
- Automação por regras
- Resumo diário com assistente IA (esqueleto inicial)
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
| `interface`        | Menus interativos via terminal                |
| `assistente_ia`    | Sugestões inteligentes e resumo diário        |
| `automacao_regras` | Criação e execução de regras de automação     |
| `persistencia`     | Leitura e escrita de dados em arquivo JSON    |
| `database`         | Módulo auxiliar de banco de dados             |

---

## Tecnologias Utilizadas

- Python 3.x

---

## Como Executar

```bash
cd "Rotina Inteligente"
python main.py
```

---

**Contato:** Carlosmanoeldev@outlook.com
