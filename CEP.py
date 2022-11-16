import fun
import requests

fun.linha()
print("Consulta CEP".center(30))
fun.linha()

cep_input = input("Digite o CEP: ")

if len(cep_input) != 8:
    print("Quantidade de digitos inválida")
    exit()

request = requests.get(f"viacep.com.br/ws/{cep_input}/json/")

adress_data = request.json()

print(adress_data)