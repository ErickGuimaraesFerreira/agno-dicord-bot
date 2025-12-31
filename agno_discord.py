from agno.agent import Agent  
from agno.tools.discord import DiscordTools  
from agno.integrations.discord import DiscordClient 
from agno.models.google import Gemini  
from agno.db.sqlite import SqliteDb  
from agno.knowledge.embedder.google import GeminiEmbedder  
from agno.tools.duckduckgo import DuckDuckGoTools  #


from agno.vectordb.chroma import ChromaDb  
import os  

from dotenv import load_dotenv  
load_dotenv()  

db = SqliteDb(session_table="agent_sessions", db_file="tmp/agent.db")  


DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")  
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  


agent = Agent( 
    name="Discord Agent",  
    description="Bot Discord que responde a mensagens em canais de texto.",  
    instructions="Você é um assistente de IA que responde a mensagens em canais de texto. Seu objetivo é ajudar os usuários a resolverem suas dúvidas e resolverem problemas.",  
    tools=[DiscordTools(DISCORD_BOT_TOKEN), DuckDuckGoTools()],  
    model=Gemini(id="gemini-2.5-flash", api_key=GOOGLE_API_KEY),  
    db=db,  
    num_history_runs=4,  
    num_history_messages=10,  
    enable_user_memories=True, 
    add_memories_to_context=True,  
    

)

discord_client = DiscordClient(agent)  # inicia o cliente Discord com o agente configurado

if __name__ == "__main__":  
    discord_client.serve()  
#agent.print_response(f"Send Hello World to channel {channel_id}")



