import csv
import random
from datetime import datetime, timedelta

'''
Estação	        Início (aprox.)	    Término (aprox.)	Temperatura Média (°C) em SP	Características
Verão ☀️	    21/22 de dezembro	20/21 de março	    22°C a 28°C	                    Quente e úmido, chuvas de verão frequentes no fim da tarde.
Outono 🍂	    20/21 de março	    20/21 de junho	    17°C a 24°C	                    Clima ameno, menos chuvas, queda gradual da temperatura.
Inverno ❄️	    20/21 de junho	    22/23 de setembro	12°C a 22°C	                    Seco e frio, com possíveis quedas abaixo de 10°C em madrugadas.
Primavera 🌱	22/23 de setembro	21 de dezembro	    18°C a 26°C	                    Temperaturas sobem, chuvas retornam, umidade começa a aumentar.
'''

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
delta = end_date - start_date

with open('historico.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Data", "Vendas", "Temperatura"])
    
    for i in range(delta.days + 1):
        current_date = start_date + timedelta(days=i)

        if current_date.month == 12 and current_date.day >= 21 or current_date.month <= 3 and current_date.day <= 20:
            # Verão
            temperatura = random.randint(22, 28)
            vendas = random.randint(120, 190) if temperatura < 25 else random.randint(160, 230)

        elif current_date.month == 3 and current_date.day >= 21 or current_date.month <= 6 and current_date.day <= 20:
            # Outono
            temperatura = random.randint(17, 24)
            vendas = random.randint(120, 180) if temperatura < 20 else random.randint(130, 200)

        elif current_date.month == 6 and current_date.day >= 21 or current_date.month <= 9 and current_date.day <= 22:
            # Inverno
            temperatura = random.randint(12, 22)
            vendas = random.randint(100, 130) if temperatura < 17 else random.randint(110, 140)
        else:
            # Primavera
            temperatura = random.randint(18, 26)
            vendas = random.randint(120, 180) if temperatura < 20 else random.randint(130, 200)

        writer.writerow([current_date.strftime('%d/%m/%y'), vendas, temperatura])

print("Arquivo 'dados_vendas_temperatura.csv' criado com sucesso!")