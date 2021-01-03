#importação Das Blibiotecas
import PySimpleGUI as sg
from faker import Faker
import os

print("""
   █████████  ███████████   ██████████   █████████   ███████████ ██████████ ██████████      ███████████  █████ █████
  ███░░░░░███░░███░░░░░███ ░░███░░░░░█  ███░░░░░███ ░█░░░███░░░█░░███░░░░░█░░███░░░░███    ░░███░░░░░███░░███ ░░███ 
 ███     ░░░  ░███    ░███  ░███  █ ░  ░███    ░███ ░   ░███  ░  ░███  █ ░  ░███   ░░███    ░███    ░███ ░░███ ███  
░███          ░██████████   ░██████    ░███████████     ░███     ░██████    ░███    ░███    ░██████████   ░░█████   
░███          ░███░░░░░███  ░███░░█    ░███░░░░░███     ░███     ░███░░█    ░███    ░███    ░███░░░░░███   ░░███    
░░███     ███ ░███    ░███  ░███ ░   █ ░███    ░███     ░███     ░███ ░   █ ░███    ███     ░███    ░███    ░███    
 ░░█████████  █████   █████ ██████████ █████   █████    █████    ██████████ ██████████      ███████████     █████   
  ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░░░░░░ ░░░░░   ░░░░░    ░░░░░    ░░░░░░░░░░ ░░░░░░░░░░      ░░░░░░░░░░░     ░░░░░    
                                                                                                                    
                                                                                                                    
                                                                                                                    
 ██████████   ██████████ █████   ████ ██████████                                                                    
░░███░░░░███ ░███░░░░░░█░░███   ███░ ░███░░░░░░█                                                                    
 ░███   ░░███░███     ░  ░███  ███   ░███     ░                                                                     
 ░███    ░███░█████████  ░███████    ░█████████                                                                     
 ░███    ░███░░░░░░░░███ ░███░░███   ░░░░░░░░███                                                                    
 ░███    ███  ███   ░███ ░███ ░░███   ███   ░███                                                                    
 ██████████  ░░████████  █████ ░░████░░████████                                                                     
░░░░░░░░░░    ░░░░░░░░  ░░░░░   ░░░░  ░░░░░░░░                                                                      
                                                                                                                    
""")

input()

sg.theme("Dark")
#Layout ou Esqueleto da Aplicação
layout = [
    [sg.Button("Gerar Nome", size=(20, 0)),sg.Input(key="nome", size=(60, 0))],
    [sg.Button("Gerar Profissão", size=(20, 0)),sg.Input(key="profissao", size=(60, 0))],
    [sg.Button("Gerar Endereço", size=(20, 0)),sg.Input(key="endereco", size=(60, 0))],
    [sg.Button("Gerar Placa", size=(20, 0)),sg.Input(key="placa", size=(60, 0))],
    [sg.Button("Gerar Cartão de Credito", size=(20, 0)),sg.Input(key="cartao_credito", size=(60, 0))],
    [sg.Button("Gerar Email", size=(20, 0)),sg.Input(key="email", size=(60, 0))],
    [sg.Button("Gerar Phone", size=(20, 0)),sg.Input(key="phone", size=(60, 0))],
    [sg.Output(size=(85,20))],
    [sg.Button("Imprimir Perfil Completo"),sg.Button("Salvar Perfil Em Arquivo")]
]
#Criando a Janela, Usando Layout Que Foi Definidos
janela = sg.Window("Faker - Gerador de Dados",layout=layout)
#Lendo as Eventos da Tela e Gerar os Dados Fakes
fake = Faker("pt_BR")
Faker.seed(0)
while True:
    event, valores = janela.Read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Gerar Nome":
        janela["nome"].update(fake.name())
    elif event == "Gerar Profissão":
        janela["profissao"].update(fake.job())
    elif event == "Gerar Endereço":
        janela["endereco"].update(fake.address())
    elif event == "Gerar Placa":
        janela["placa"].update(fake.license_plate())
    elif event == "Gerar Cartão de Credito":
        janela["cartao_credito"].update(fake.credit_card_full())
    elif event == "Gerar Email":
        janela["email"].update(fake.email())
    elif event == "Gerar Phone":
        janela["phone"].update(fake.phone_number())
    elif event == "Imprimir Perfil Completo":
        print(f"NOME: {fake.name()}{os.linesep}PROFISSÃO: {fake.job()}{os.linesep}ENDEREÇO: {fake.address()}{os.linesep}PLACA: {fake.license_plate()}{os.linesep}CARTÃO DE CREDITO: {fake.credit_card_full()}{os.linesep}EMAIL: {fake.email()}{os.linesep}PHONE: {fake.phone_number()}{os.linesep}")
    elif event == "Salvar Perfil Em Arquivo":
        with open("dados_de_teste.txt", "a", encoding="utf-8", newline="") as arquivo:
            arquivo.write(f"NOME: {fake.name()}{os.linesep}PROFISSÃO: {fake.job()}{os.linesep}ENDEREÇO: {fake.address()}{os.linesep}PLACA: {fake.license_plate()}{os.linesep}CARTÃO DE CREDITO: {fake.credit_card_full()}{os.linesep}EMAIL: {fake.email()}{os.linesep}PHONE: {fake.phone_number()}{os.linesep}")
