import time

import requests
import schedule
from bs4 import BeautifulSoup

from Poupanca import modelspoupanca


def job():

    try:
        requisicao = requests.get("http://www.portalbrasil.net/poupanca_mensal.htm")
        soup = BeautifulSoup(requisicao.content, 'html.parser')
        titulo = soup.title
        dois = soup.find_all("td")

        print(titulo.prettify())

        mes = 7
        ano = 19
        indice = 20
        num = 18
        meses = {'JAN':'01','FEV':'02','MAR':'03','ABR':'04','MAI':'05','JUN':'06','JUL':'07','AGO':'08','SET':'09','OUT':'10','NOV':'11','DEZ':'12'}
        dias = {'JAN': '31', 'FEV': '28', 'MAR': '31', 'ABR': '30', 'MAI': '31', 'JUN': '30', 'JUL': '31', 'AGO': '31',
                 'SET': '30', 'OUT': '31', 'NOV': '30', 'DEZ': '31'}

        while mes <= num:

            data = str(dois[ano].get_text() + '-' + meses[dois[mes].get_text().strip()] + '-'+dias[dois[mes].get_text().strip()]).strip()
            valor = float(dois[indice].get_text().replace(',','.'))

            print(dois[mes].get_text())
            print(dois[indice].get_text().replace(',','.'))

            if dois[indice].get_text().strip() != '-' :

                    modelspoupanca.cursor = modelspoupanca.connection.execute(modelspoupanca.sql, '1','Índices mensais da poupança', data,valor,data)
                    modelspoupanca.cursor.commit()


            mes += 1
            indice += 1

        modelspoupanca.cursor.close()
        modelspoupanca.connection.close()


    except Exception as e:
        print(e)


schedule.every().day.at("13:52").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

