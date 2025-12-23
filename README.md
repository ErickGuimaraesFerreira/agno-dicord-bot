# Agno Discord Bot

Um bot de Discord inteligente construído com o framework **Agno**, alimentado pelo modelo **Gemini 2.5 Flash** da Google. O bot é capaz de responder perguntas, realizar buscas na web e manter memória contextual das conversas.

---

## Visão Geral

Este projeto implementa um assistente de IA para Discord que combina:

- **Processamento de linguagem natural** via Google Gemini
- **Busca integrada na web** através do DuckDuckGo
- **Memória persistente** com SQLite para contexto entre conversas
- **Arquitetura modular** usando o framework Agno

O bot foi desenvolvido para ajudar usuários em canais de texto, respondendo dúvidas e auxiliando na resolução de problemas de forma conversacional.

---

## Tecnologias

| Tecnologia | Propósito |
|------------|-----------|
| [Agno](https://github.com/agno-agi/agno) | Framework de agentes de IA |
| [Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) | Modelo de linguagem |
| [Discord.py](https://discordpy.readthedocs.io/) | Integração com Discord |
| [DuckDuckGo](https://duckduckgo.com/) | Ferramenta de busca na web |
| [SQLite](https://www.sqlite.org/) | Persistência de sessões e memória |
| [ChromaDB](https://www.trychroma.com/) | Banco de vetores (disponível para uso) |

---

## Pré-requisitos

- Python 3.13 ou superior
- [uv](https://github.com/astral-sh/uv) (gerenciador de pacotes recomendado)
- Token de bot do Discord
- Chave de API do Google (Gemini)

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/agno-discord.git
cd agno-discord
```

### 2. Configure o ambiente virtual

```bash
uv venv
uv sync
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DISCORD_BOT_TOKEN=seu_token_do_discord
GOOGLE_API_KEY=sua_chave_api_google
```

> **Nota:** O arquivo `.env` está incluído no `.gitignore` por segurança.

---

## Como Executar

Ative o ambiente virtual e execute o bot:

```bash
# Usando uv
uv run python agno_discord.py
```

Ou diretamente:

```bash
python agno_discord.py
```

O bot se conectará ao Discord e começará a escutar mensagens nos canais de texto configurados.

---

## Estrutura do Projeto

```
agno-discord/
├── agno_discord.py    # Código principal do bot
├── main.py            # Entry point alternativo
├── pyproject.toml     # Configuração do projeto e dependências
├── .env               # Variáveis de ambiente (não versionado)
├── .gitignore         # Arquivos ignorados pelo Git
├── tmp/               # Arquivos temporários e banco de dados
│   └── agent.db       # SQLite com sessões e memórias
└── README.md          # Documentação
```

---

## Funcionalidades

### Assistente Conversacional
O bot responde mensagens em canais de texto do Discord de forma natural, utilizando o modelo Gemini para gerar respostas contextualizadas.

### Busca na Web
Através da integração com DuckDuckGo, o bot pode pesquisar informações atualizadas na internet para complementar suas respostas.

### Memória Persistente
O sistema mantém:
- **Histórico de conversas** (últimas 10 mensagens e 4 execuções)
- **Memórias de usuário** para personalização do atendimento
- **Contexto entre sessões** armazenado em SQLite

---

## Configuração do Bot no Discord

1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications)
2. Crie uma nova aplicação
3. Na seção **Bot**, crie um bot e copie o token
4. Em **OAuth2 > URL Generator**, selecione os escopos `bot` e `applications.commands`
5. Defina as permissões necessárias (leitura/envio de mensagens)
6. Use a URL gerada para adicionar o bot ao seu servidor

---

## Dependências

```toml
agno>=2.3.19
chromadb>=1.3.7
ddgs>=9.10.0
discord-py>=2.6.4
google-genai>=1.56.0
python-dotenv>=1.2.1
sqlalchemy>=2.0.45
```

---

## Licença

Este projeto é distribuído para fins educacionais e de desenvolvimento.

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
