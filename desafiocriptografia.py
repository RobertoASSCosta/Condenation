# Codenation Criptografia
import requests
import hashlib
import json

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
tk = "fd3b5ee7f6e6a73db25662c25b5ad6fbadb9d357"

urlgit = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={0}'.format(tk)
response = requests.get(urlgit)
response_json = response.json()
numero_casas = response_json['numero_casas']
cifrado = response_json['cifrado']
token = response_json['token']

def decifrar():
    msg = ''
    for x in cifrado:
        if x in alfabeto:
            pos = alfabeto.index(x)
            msg += alfabeto[pos - numero_casas]
        else:
            msg += x
    return msg.lower()

orig = decifrar()
resumo = hashlib.sha1(str(orig).encode('utf-8')).hexdigest()

resultado = {
    "numero_casas": numero_casas,
    "token": token,
    "cifrado": cifrado,
    "decifrado": orig,
    "resumo_criptografico": resumo
}


def criar_arquivo():
    arquivo = open('answer.json', 'w')
    json.dump(resultado, arquivo, indent=4, sort_keys=False)
    arquivo.close()


def postar():
    urlpost = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={0}'.format(tk)
    file = {"answer": open("answer.json", "rb")}
    requests.post(urlpost, files=file)
    print(response.status_code)
    print(response.content)

if __name__ == '__main__':
    print(resultado)
    criar_arquivo()
    postar()