# pip install pyautogui
# pip install pandas openpyxl
# Passo 1: Entrar no sistema da empresa
    # Abrir o navegador
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos
'''
pyautogui.click --> clica em uma coordenada da tela
pyautogui.write --> escreve um texto
pyautogui.press --> aperta uma tecla
pyautogui.hotkey --> aperta uma combinação de teclas (um atalho)
pyautogui.sleep --> pausa o código por alguns segundos
'''
import pyautogui 
import time
import pandas

pyautogui.PAUSE = 1  # pausa de 1 segundo após cada comando
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)  # espera 3 segundos para a página carregar


pyautogui.click(x=1130, y=616)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha muito muito muito dificilima")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(4)  

tabela = pandas.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    # codigo
    pyautogui.click(x=995, y=449)  # clica no menu de produtos
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")  
    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # preco
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)

