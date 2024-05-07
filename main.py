from selenium import webdriver
import requests
import json
from print_color import print
from MySQLDatabase import MySQLDatabase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import usuario as u
import moeda as mo
import time

def IncluirNome(nome):
   
    u.incluir(nome)

def AdicionaMoeda():
    dados = requests.get('https://brasilbitcoin.com.br/API/v2/summary').json()
   # with open('dados.json') as arquivo:
   #  dados = json.load(arquivo)
    json_str = json.dumps(dados, indent=4)
    dados_symbol = dados["symbols"]
    
    for x in range(len(dados_symbol)):
       c = MySQLDatabase()
       sql = f'Insert Into moeda(nome, moedaCorrente, isFrozen, MoedaBase, volume )'
       sql += f'Values("{dados_symbol[x]["symbol"]}", "{dados_symbol[x]["baseCurrency"]}","{dados_symbol[x]["isFrozen"]}", "{dados_symbol[x]["baseCurrency"]}", "{dados_symbol[x]["volume"]}" )'
      # c.executa_DML(sql)
   
def ValorMoeda(moeda):
    #dados = requests.get('https://brasilbitcoin.com.br/API/v2/summary').json()
    try:
        
        r = 'https://brasilbitcoin.com.br/API/prices/'+ moeda +''
        dados = requests.get(r).json()
    except:
        return 0 
   # with open('dados.json') as arquivo:
   #  dados = json.load(arquivo)
    return dados["buy"]
   #print(dados["buy"])
def GetDados():
    url = "https://brasilbitcoin.com.br/api/my_wallets"

    payload={}
    files={}
    headers = {
        'Authentication': 'Q1dwiGflm3WRzUQMmmM6Kf4acUPYHz5tsw9LCzzZRSQURy6xgYZAxVU2LjkaejhN'
    }

    response = requests.request("GET", url, headers=headers, data=payload, files=files).json()

    print(response)    

def InserirValorMoeda():
    dados = requests.get('https://brasilbitcoin.com.br/API/v2/summary').json()
   # with open('dados.json') as arquivo:
   #  dados = json.load(arquivo)
    json_str = json.dumps(dados, indent=4)
    dados_symbol = dados["symbols"]

    for x in range(len(dados_symbol)):
       c = MySQLDatabase()
       nome = dados_symbol[x]["baseCurrency"]
       valor = ValorMoeda(nome)
       mo.incluir(nome, valor)
       
def GetMoedas():
    url = "https://brasilbitcoin.com.br/api/get_balance"

    payload={}
    files={}
    headers = {
    'Authentication': 'Q1dwiGflm3WRzUQMmmM6Kf4acUPYHz5tsw9LCzzZRSQURy6xgYZAxVU2LjkaejhN'
    }

    response = requests.request("GET", url, headers=headers, data=payload, files=files)
    json_str = json.dumps(response.json(), indent=4)
    
    valores = json.loads(json_str)
    for x in valores:
        if(x != 'user_cpf' and x != 'brl' and x != 'link' and x != 'invi'):
            v = ValorMoeda(str.upper(x))
            if(type(v) == str):
                myvf = float(response.json()[x])
                vf = float(v)
                valoremR = vf * myvf 
                if(valoremR > 0):
                    print(x, '=', myvf)

               
                
def vender():
    print("")



def transation():
    url = "https://brasilbitcoin.com.br/api/my_transactions"
    payload={}
    headers = {
    'Authentication': 'Q1dwiGflm3WRzUQMmmM6Kf4acUPYHz5tsw9LCzzZRSQURy6xgYZAxVU2LjkaejhN'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    json_str = json.dumps(response.json(), indent=4)
    print(json_str)

def Conexao(Navegador):
    
    Navegador.get('https://brasilbitcoin.com.br/dashboard')
    Navegador.maximize_window()
    url = Navegador.current_url
    ##while(url == 'https://brasilbitcoin.com.br/entrar'):
    ##   url = Navegador.current_url
        ## print('espera')
    Navegador.implicitly_wait(1)

    Navegador.find_element(by = By.NAME, value="cpf").send_keys('27759535813')
    Navegador.find_element(by = By.XPATH, value='//*[@id="password"]').send_keys('Arjona13@#$')
    Navegador.find_element(by=By.XPATH, value='//*[@id="submit"]').click()
    Navegador.implicitly_wait(10)
    time.sleep(45)
    menus = Navegador.find_elements(by=By.CLASS_NAME, value='subMenu')

    menus[1].click()
    opt = Navegador.find_elements(by=By.XPATH, value='//*[@id="testmenu"]/div/div[1]/div')
    cont = 0

    for x in opt:
        x.click()
        print(x.text)
        print(cont)
        cont = cont + 1
    return Navegador

if __name__ == '__main__':

   #GetMoedas()
   #for x in range(250):
        #ValorMoeda()
    #    InserirValorMoeda()
    #IncluirNome("Valdirene Maria")
    



    #try:
        #c = MySQLDatabase()
        #sql = f'Insert Into usuario(nome) Values("Marcelo Arjona")'
        #c.executa_DML(sql)
    #except ConnectionError as err:
     #   raise f"Erro during the connection .Message: {err}"

    Caminho = r"C:\Users\31370\Documents\Phyton\Trend\Infra\Drive\chromedriver.exe"

    Navegador = webdriver.Chrome(executable_path=Caminho)

    Conexao(Navegador)

    btc = Navegador.find_element(by=By.CLASS_NAME, value='first')
    btc.click()
    time.sleep(5)
    filtro = Navegador.find_element(by=By.NAME, value='filter')
    filtro.send_keys('Ethereum')
    filtro.send_keys(Keys.ENTER)
    select = Navegador.find_element(by=By.CLASS_NAME, value='paymentCoin')
    for xo in select:
       print(xo)


 
#
#print(data)
#json_str = json.dumps(data, indent=4)
#with open("dados.json", "w") as arquivo:
#    arquivo.write(json_str)
#print(f'last: {data["last"]}, max: {data["max"]}, min: {data["min"]}')

    
     #print(json.dumps(dados_symbol, indent=4))
     #print(len(dados_symbol))
'''
   
      
'''       

    #nome = 1

    #print(json_str)


		