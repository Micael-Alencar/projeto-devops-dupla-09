from app import app, MENSAGEM, NOME_DUPLA 
 
 
def test_saude_responde_ok(): 
    resposta = app.test_client().get("/saude") 
    assert resposta.status_code == 200 
    assert resposta.get_json()["status"] == "ok" 
 
 
def test_aluno():
    resposta = app.test_client().get("/aluno")
    assert resposta.status_code == 200 
    dados = resposta.get_json() 
    assert dados["dupla"] == NOME_DUPLA 
    assert dados["mensagem"] == MENSAGEM 