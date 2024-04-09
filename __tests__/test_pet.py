# 1-  Bibliotecas
import json          # leitor e escritor de arquivos json
import pytest        # engine / framework do teste de unidade
import requests      # framework de teste de API


# 2- classe (opcional no Python, em muitos casos)


# 2.1 - atributos ou variáveis
# consulta e resultado esperado
pet_id = 117659801                # código do animal
pet_name = "Snoopy"               # nome do animal
pet_category_id = 1               # código da categoria do animal
pet_category_name = "dog"         # título da categoria
pet_tag_id = 1                    # código do rótulo
pet_tag_name = "vacinado"         # título do rótulo  
       

#informações em comum
url = 'https://petstore.swagger.io/v2/pet'
headers= {'Content-Type': 'application/json'}           #formato dos dados tracejados

# 2.2 - funções / métodos
def test_post_pet():
    #configura
    #dados de entrada estão no arquivo json
    pet = open('./fixtures/json/pet1.json')               # abre o arquivo json da pasta fixtures
    data = json.loads (pet.read())                        # função vai carregar os dados do json  / ler o conteudo e carrega o json em uma variavel chamada data

    # resultado esperado estão nos atributos acima das funções
    
    #executa
    response = requests.post(                                 # executa o metodo  Post com as informações a seguir
        url = url,                                           # url recebe a url declarada nos atibutos url = 'https://petstore.swagger.io/v2/pet'
        headers = headers,                                   #cabeçalho / informações extras
        data = json.dumps(data),                             # a mensagem - json
        timeout = 5                                          # tempo limite
    )

    #valida
    response_body = response.json()                        # cria uma variavel e carrega a resposta em formato json

    assert response.status_code == 200
    assert response_body ['id'] == pet_id
    assert response_body ['name'] == pet_name
    assert response_body ['category']['name'] == pet_category_name
    assert response_body ['tags'][0]['name'] == pet_tag_name


def test_get_pet():
    #configura
    #dados de entrada e saida / resultado esperado estão na seção de atributosw antes das funções


    #executa
    response = requests.get (
        url= f'{url}/{pet_id}',                       # chama o endereço do get/consulta passando o id do animal
        headers=headers
        #não tem corpo da mensagem / body
    )

    #valida
    response_body = response.json()   

    assert response.status_code == 200
    assert response_body ['name'] == pet_name
    assert response_body ['category']['id'] == pet_category_id
    assert response_body ['tags'][0]['id'] == pet_tag_id
    assert response_body ['status'] == 'available'

def test_put_pet():
    #configura
    # dados entrada vem de um arquivo json

    pet = open ('./fixtures/json/pet2.json')
    data = json.loads (pet.read())

    #dados de saida/ resultado esperado vem dos atributos descritos antes das funções

    # executa
    response = requests.put(
        url = url,
        headers=headers,
        data = json.dumps (data),
        timeout= 5
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body ['name'] == pet_name
    assert response_body ['category']['id'] == pet_category_id
    assert response_body ['tags'][0]['id'] == pet_tag_id
    assert response_body ['status'] == 'sold'
    assert response_body ['name'] == pet_name
    assert response_body ['category']['id'] == pet_category_id
    assert response_body ['tags'][0]['id'] == pet_tag_id
    
def test_delete_pet():
    #configura
    #dados de entrada e saida virão dos atributos

    #executa
    response = requests.delete(
        url= f'{url}/{pet_id}',
        headers=headers
    )

    #valida
    response_body = response.json()

    assert response.status_code == 200
    assert response_body ['code'] == 200
    assert response_body ['type'] == 'unknown'
    assert response_body ['message'] == str (pet_id)



