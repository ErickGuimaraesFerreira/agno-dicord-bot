from agno.agent import Agent  # Importa a classe Agent do framework Agno
from agno.tools.discord import DiscordTools  # Importa as ferramentas para integração com Discord
from agno.integrations.discord import DiscordClient  # Importa o cliente do Discord para conectar o agente
from agno.models.google import Gemini  # Importa o modelo Gemini da Google
from agno.db.sqlite import SqliteDb  # Importa o banco de dados SQLite para armazenamento
from agno.knowledge.embedder.google import GeminiEmbedder  # Importa o embedder Gemini (não usado explicitamente, mas importado)
from agno.tools.duckduckgo import DuckDuckGoTools  # Importa as ferramentas de busca do DuckDuckGo


from agno.vectordb.chroma import ChromaDb  
import os  # Importa o módulo os para interagir com o sistema operacional

from dotenv import load_dotenv  # Importa a função para carregar variáveis de ambiente
load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

db = SqliteDb(session_table="agent_sessions", db_file="tmp/agent.db")  # Inicializa o banco de dados SQLite para sessões do agente


DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Obtém o token do bot do Discord das variáveis de ambiente
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Obtém a chave da API do Google das variáveis de ambiente


agent = Agent(  # Inicializa o Agente com as configurações especificadas
    name="Discord Agent",  # Define o nome do agente
    description="Bot Discord que responde a mensagens em canais de texto.",  # Define a descrição do agente
    instructions="Você é um assistente de IA que responde a mensagens em canais de texto. Seu objetivo é ajudar os usuários a resolverem suas dúvidas e resolverem problemas.",  # Define as instruções de comportamento do agente
    tools=[DiscordTools(DISCORD_BOT_TOKEN), DuckDuckGoTools()],  # Lista de ferramentas disponíveis para o agente (Discord e DuckDuckGo)
    model=Gemini(id="gemini-2.5-flash", api_key=GOOGLE_API_KEY),  # Define o modelo de IA a ser usado (Gemini 2.5 Flash)
    db=db,  # Define o banco de dados para persistência
    num_history_runs=4,  # Define o número de execuções históricas a serem mantidas
    num_history_messages=10,  # Define o número de mensagens históricas a serem mantidas no contexto
    enable_user_memories=True,  # Habilita a memória de fatos sobre o usuário
    add_memories_to_context=True,  # Adiciona memórias ao contexto da conversa
    

)

discord_client = DiscordClient(agent)  # Inicializa o cliente Discord com o agente configurado

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    discord_client.serve()  # Inicia o serviço do cliente Discord para escutar e responder mensagens
#agent.print_response(f"Send Hello World to channel {channel_id}") # Código comentado (exemplo de uso)

