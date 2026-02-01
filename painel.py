import requests, os, time, base64, re

# Cores para o Termux
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'

# URL decodificada do Ministério do Trabalho (MTE)
a = base64.b64decode('aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA==').decode('ascii')

def clear():
    os.system("clear")

def banner():
    print(f"{B}="*45)
    print(f"{G}      PAINEL DE CONSULTA - SOMOS UMA LEGIÃO")
    print(f"{B}="*45)

def consultar(cpf):
    try:
        clear()
        banner()
        print(f"\n{C}[{G}*{C}] Consultando CPF: {B}{cpf}{C}...\n")
        
        h = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Host': "www.juventudeweb.mte.gov.br"
        }
        # Envia a requisição para o site do MTE
        r = requests.post(a, headers=h, data=f'acao=consultar%20cpf&cpf={cpf}', timeout=15).text
        
        # Extração de dados via Regex
        print(f"{G}--- [ RESULTADOS REAIS ] ---{C}")
        print(f"{Y}CPF:{C} {re.search('NRCPF=\"(.*?)\"', r).group(1)}")
        print(f"{Y}Nome:{C} {re.search('NOPESSOAFISICA=\"(.*?)\"', r).group(1).title()}")
        print(f"{Y}Nascimento:{C} {re.search('DTNASCIMENTO=\"(.*?)\"', r).group(1)}")
        print(f"{Y}Nome da Mae:{C} {re.search('NOMAE=\"(.*?)\"', r).group(1).title()}")
        print(f"{Y}Endereco:{C} {re.search('NOLOGRADOURO=\"(.*?)\"', r).group(1).title()}")
        print(f"{Y}Cidade:{C} {re.search('NOMUNICIPIO=\"(.*?)\"', r).group(1).title()}-{re.search('SGUF=\"(.*?)\"', r).group(1)}")
        print(f"{Y}CEP:{C} {re.search('NRCEP=\"(.*?)\"', r).group(1)}")
        print(f"{G}----------------------------{C}")

    except AttributeError:
        print(f"{R}[!] Erro: CPF não encontrado ou base de dados offline.{C}")
    except Exception as e:
        print(f"{R}[!] Erro de conexão.{C}")
    
    input(f"\n{G}[+]{C} Pressione Enter para voltar ao menu...")

def main():
    while True:
        clear()
        banner()
        print(f"\n{C}[{G} 1 {C}] Consultar CPF")
        print(f"{C}[{G} 0 {C}] Sair")
        
        op = input(f"\n{G}[+]{C} Selecione uma opção: {B}")
        
        if op == '1':
            cpf = input(f"{C}[{G}*{C}] Informe o CPF (apenas números): {B}")
            consultar(cpf)
        elif op == '0':
            print(f"\n{G}Somos uma legião.{C}\n")
            break
        else:
            print(f"{R}Opção Inválida!{C}")
            time.sleep(1)

if __name__ == "__main__":
    main()
    
