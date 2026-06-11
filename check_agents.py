import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Load environment variables
load_dotenv()
project_endpoint = os.getenv("PROJECT_ENDPOINT")

print(f"Current PROJECT_ENDPOINT: {project_endpoint}\n")

# Extract just the base project URL (everything before /agents)
if "/agents" in project_endpoint:
    base_endpoint = project_endpoint.split("/agents")[0]
    print(f"Corrected endpoint should be: {base_endpoint}\n")
else:
    base_endpoint = project_endpoint

# Try to connect and list agents
try:
    credential = DefaultAzureCredential(
        exclude_environment_credential=True,
        exclude_managed_identity_credential=True
    )
    project_client = AIProjectClient(
        credential=credential,
        endpoint=base_endpoint
    )
    
    print("Available agents:")
    agents = project_client.agents.list()
    for agent in agents:
        print(f"  - {agent.name} (id: {agent.id})")
except Exception as e:
    print(f"Error: {str(e)}")
    print("\nPlease verify:")
    print("1. PROJECT_ENDPOINT is correct (base URL without /agents path)")
    print("2. You have proper authentication set up")
