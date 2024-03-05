# Passo a passo do Projeto.

# Passo 1: entrar no sistema da empresa.
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import time
import pyautogui

pyautogui.PAUSE = 2

#abrir o navegador (Chrome)

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

time.sleep(2)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# Passo 2: Fazer login

# inserindo o login
pyautogui.click(x=499, y=337)

pyautogui.write("seuemail@example.com")

#inserindo a senha
pyautogui.press("tab")

pyautogui.write("123")

#clicando no botão de logar
pyautogui.click(x=685, y=462)

time.sleep(3)

# Passo 3: Importar a base de dados.
import pandas

tabela = pandas.read_csv("produtos.csv")

# print(tabela)

# Passo 4: Cadastrar 1 produto.

for linha in tabela.index:

    # clicar no primeiro campo

    pyautogui.click(x=491, y=252)

    #cadastrar o codigo do produto
    
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    #marca
     
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # Tipo
     
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # Categoria
     
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preço
     
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # Custo
     
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # observação
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)


# Passo 5: Repetir o procecsso de cadastramento, até acabar.