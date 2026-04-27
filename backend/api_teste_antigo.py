import requests

# URL base da API
BASE_URL = 'http://127.0.0.1:5000'

# Teste de GET para listar animais
def test_listar_animais():
    response = requests.get(f'{BASE_URL}/animais')
    assert response.status_code == 200, f"Esperado 200, mas obteve {response.status_code}"
    print("✅ Teste de listar animais passou!")

# Teste de POST para adicionar um novo animal
def test_adicionar_animal():
    novo_animal = {
        "nome": "Girafa",
        "descricao": "Animal de pescoço longo",
        "data_nascimento": "2015-07-23",
        "especie": "Mamífero",
        "habitat": "Savanas",
        "pais_origem": "África"
    }
    response = requests.post(f'{BASE_URL}/animais', json=novo_animal)
    assert response.status_code == 201, f"Esperado 201, mas obteve {response.status_code}"
    assert response.json()['nome'] == novo_animal['nome'], "O nome do animal não foi retornado corretamente!"
    print("✅ Teste de adicionar animal passou!")

# Teste de PUT para atualizar um animal
def test_atualizar_animal():
    animal_id = 1  # Supondo que o ID do animal que você quer atualizar seja 1
    animal_atualizado = {
        "nome": "Leão Atualizado",
        "descricao": "Animal grande e feroz",
        "data_nascimento": "2010-05-10",
        "especie": "Mamífero",
        "habitat": "Florestas",
        "pais_origem": "África"
    }
    response = requests.put(f'{BASE_URL}/animais/{animal_id}', json=animal_atualizado)
    assert response.status_code == 200, f"Esperado 200, mas obteve {response.status_code}"
    assert response.json()['nome'] == animal_atualizado['nome'], "O nome do animal não foi atualizado corretamente!"
    print("✅ Teste de atualizar animal passou!")

# Teste de DELETE para remover um animal
def test_remover_animal():
    animal_id = 1  # Supondo que o ID do animal que você quer remover seja 1
    response = requests.delete(f'{BASE_URL}/animais/{animal_id}')
    
    # Debug: Imprime a resposta completa
    print("Resposta completa da API:", response.json())
    
    # Recupera a mensagem da resposta
    mensagem = response.json().get('message', '')
    print("Mensagem de resposta:", mensagem)

    # Verifica se a mensagem contém a frase esperada
    assert "Animal removido com sucesso!" in mensagem, f"A mensagem de remoção não foi retornada corretamente! Mensagem: {mensagem}"
    print("✅ Teste de remover animal passou!")

# Executando os testes
if __name__ == '__main__':
    test_listar_animais()
    test_adicionar_animal()
    test_atualizar_animal()
    test_remover_animal()
