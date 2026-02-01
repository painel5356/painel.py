import requests, os, time, base64, re

# Cores
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

# URL Descodificada do MTE (Consulta CPF)
URL_BASE = base64.b64decode('aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA==').decode('ascii')

def clear():
    os.system("clear")

def consultar_cpf(cpf):
    clear()
    print(f"{C}[{G}*{C}] Consultando CPF: {B}{cpf}{C}...")
    
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Host': "www.juventudeweb.mte.gov.br"
    }
    data = f'acao=consultar%20cpf&cpf={cpf}'

    try:
        response = requests.post(URL_BASE, headers=headers, data=data, timeout=10).text
        
        # Extração dos dados usando ReGex (conforme o código que você achou)
        nome = re.search('NOPESSOAFISICA="(.*?)"', response).group(1).title()
        nasc = re.search('DTNASCIMENTO="(.*?)"', response).group(1)
        mae = re.search('NOMAE="(.*?)"', response).group(1).title()
        rua = re.search('NOLOGRADOURO="(.*?)"', response).group(1).title()
        city = re.search('NOMUNICIPIO="(.*?)"', response).group(1).title()
        uf = re.search('SGUF="(.*?)"', response).group(1)

        print(f"\n{G}--- DADOS ENCONTRADOS ---{C}")
        print(f"{Y}NOME:{C} {nome}")
        print(f"{Y}NASCIMENTO:{C} {nasc}")
        print(f"{Y}MÃE:{C} {mae}")
        print(f"{Y}ENDEREÇO:{C} {rua}")
        print(f"{Y}CIDADE:{C} {city}-{uf}")
        print(f"{G}--------------------------{C}")

    except:
        print(f"\n{R}[!] Erro: CPF não encontrado ou sistema fora do ar.{C}")
    
    input(f"\n{Y}Pressione Enter para voltar...{C}")

def menu():
    while True:
        clear()
        print(f"{B}="*40)
        print(f"{G}      PAINEL LEGADO - CONSULTA CPF")
        print(f"{B}="*40)
        print(f"{C}[{G} 1 {C}] Consultar CPF")
        print(f"{C}[{G} 0 {C}] Sair")
        
        op = input(f"\n{Y}Escolha uma opção: {C}")
        
        if op == '1':
            num = input(f"{G}Digite o CPF (apenas números): {C}")
            consultar_cpf(num)
        elif op == '0':
            break

if __name__ == "__main__":
    menu()
  
