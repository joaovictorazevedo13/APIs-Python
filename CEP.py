import fun
import requests

def main():
    fun.linha()
    print("Consulta CEP".center(30))
    fun.linha()

    cep_input = input("Digite o CEP: ")

    if len(cep_input) != 8:
        print("Quantidade de digitos inválida")
        exit()

    request = requests.get(f"https://viacep.com.br/ws/{cep_input}/json/")

    adress_data = request.json()

    if "erro" not in adress_data:
        if adress_data['logradouro'] == '':
            adress_data['logradouro'] = 'CEP da Cidade toda'
            print(f"Rua: {adress_data['logradouro']}")
        else:
            print(f"Rua: {adress_data['logradouro']}")
        print(f"Bairro: {adress_data['bairro']}")
        print(f"Cidade: {adress_data['localidade']}")
        print(f"UF: {adress_data['uf']}")
    else:
        print("CEP inválido")

if __name__ == '__main__':
    main()