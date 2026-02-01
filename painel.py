import requests, os, time, base64, re

# Cores
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'

# URL base do Ministério do Trabalho (MTE)
URL_BASE = base64.b64decode('aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA==').decode('ascii')

def clear():
    os.system("clear")

def banner():
    print(f"{B}="*45)
    print(f"{G}      PAINEL DE CONSULTA - SOMOS UMA LEGIÃO")
    print(f"{B}="*45)

def consultar_cpf(cpf):
    try:
        clear()
        banner()
        print(f"\n{C}[{G}*{C}] Consultando CPF: {B}{cpf}{C}...\n")
        
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Host': "www.juventudeweb.mte.gov.br"
        }
        
        # Faz a busca no sistema do governo
        r = requests.post(URL_BASE, headers=headers, data=f'acao=consultar%20cpf&cpf={cpf}', timeout=15).text
        
        # Mostra os dados na tela
        print(f"{G}--- [ RESULTADOS ENCONTRADOS ] ---{C}")
        print(f"{Y}NOME:{C} {re.search('NOPESSOAFISICA=\"(.*?)\"', r).group(1).title()}")
        print(f"{Y}NASCIMENTO:{C} {re.search('DTNASCIMENTO=\"(.*?)\"', r).group(1)}")
        print(f"{Y}MÃE:{C} {re.search('NOMAE=\"(.*?)\"', r).group(1).title()}")
        print(f"{Y}CIDADE:{C} {re.search('NOMUNICIPIO=\"(.*?)\"', r).group(1).title()}-{re.search('SGUF=\"(.*?)\"', r).group(1)}")
        print(f"{G}---------------------------------{C}")

    except:
        print(f"{R}[!] Erro: CPF não encontrado ou sistema instável.{C}")
    
    input(f"\n{G}[+]{C} Pressione Enter para voltar...")

def main():
    while True:
        clear()
        banner()
        print(f"\n{C}[{G} 1 {C}] Consultar CPF")
        print(f"{C}[{G} 0 {C}] Sair")
        
        op = input(f"\n{G}[+]{C} Opção: {B}")
        
        if op == '1':
            num = input(f"{C}[{G}*{C}] Digite o CPF: {B}")
            consultar_cpf(num)
        elif op == '0':
            break

if __name__ == "__main__":
    main()
        
