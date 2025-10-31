import requests
import json

class GitHubAPI:
    def __init__(self, username):
        self.username = username
        self.base_url = f"https://api.github.com/users/{username}"
    
    def get_user_info(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            return response.json()
        return None
    
    def get_repositories(self):
        url = f"{self.base_url}/repos"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    
    def salvar_dados(self):
        dados = {
            'user_info': self.get_user_info(),
            'repositories': self.get_repositories()
        }
        
        with open(f'github_{self.username}.json', 'w') as f:
            json.dump(dados, f, indent=2)
        
        print(f"Dados salvos em 'github_{self.username}.json'")

# Exemplo de uso
# github = GitHubAPI('seu-usuario')
# github.salvar_dados()
