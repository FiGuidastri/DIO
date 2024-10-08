# %%
from datetime import timedelta, datetime

# %%
tipo_carro = {'P': 30, 'M': 45, 'G': 60}
carro = input('Selecione o tamanho do carro: P, M ou G: ').upper()
data_atual = datetime.now()

if carro in tipo_carro:
    data_estimada = data_atual + timedelta(minutes=tipo_carro[carro])
    data_estimada_formatada = data_estimada.strftime('%H:%M')
    print(f'O carro chegou às {data_atual.strftime("%H:%M")} e ficará pronto às {data_estimada_formatada}')
else:
    print("Tipo inválido")

# %%
