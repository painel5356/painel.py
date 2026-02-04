import requests
import os

def format_title(title):
    print(f"\n{'='*40}")
    print(f"{title.center(40)}")
    print(f"{'='*40}")

def consultar_cep():
    cep = input("\nDigite o CEP (apenas números): ")
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            format_title("RESULTADO CEP")
            print(f"Rua: {dados.get('street')}")
            print(f"Bairro: {dados.get('neighborhood')}")
            print(f"Cidade: {dados.get('city')} - {dados.get('state')}")
        else:
            print("\n[!] CEP não encontrado ou inválido.")
    except Exception as e:
        print(f"\n[!] Erro na conexão: {e}")
    input("\nPressione Enter para voltar...")

def consultar_ddd():
    ddd = input("\nDigite o DDD: ")
    url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            format_title(f"CIDADES DO DDD {ddd}")
            print(", ".join(dados.get('cities', []))[:500] + "...")
        else:
            print("\n[!] DDD não encontrado.")
    except Exception as e:
        print(f"\n[!] Erro na conexão: {e}")
    input("\nPressione Enter para voltar...")

def menu():
    while True:
        os.system('clear')
        print("="*40)
        print("      PAINEL DE CONSULTAS LEGAIS")
        print("="*40)
        print("[1] Consultar CEP")
        print("[2] Consultar DDD")
        print("[3] Consultar Bancos (Lista)")
        print("[0] Sair")
        print("="*40)
        
        opt = input("\nEscolha uma opção: ")
        
        if opt == '1':
            consultar_cep()
        elif opt == '2':
            consultar_ddd()
        elif opt == '3':
            print("\nBuscando lista de bancos...")
            # Exemplo de como pegar o primeiro banco da lista
            r = requests.get("https://brasilapi.com.br/api/banks/v1")
            for banco in r.json()[:10]: # Mostra só os 10 primeiros
                print(f"- {banco['name']}")
            input("\nMostrando apenas os 10 primeiros. Enter para voltar.")
        elif opt == '0':
            break

if __name__ == "__main__":
    menu()
        
