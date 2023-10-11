# amcom_challenge_backend

### :memo: Sobre a aplicação

Esta é uma aplicação FullStack para um desafio de admissão de vaga. Consiste num sistema de consulta das cotações das moedas BRL, EUR e JPY dos últimos 5 dias úteis em base de dólar (USD)

### :bookmark_tabs: **Rotas**
A api pode ser acessada em http://localhost:8000 após subir e rodar o projeto</br>
'/docs' lista todas as rotas documentadas. [**GET**]</br>


### :hammer: **Configurando o Projeto**

Clone o projeto</br>
Com o projeto aberto, vamos executar os seguintes comandos de configuração</br>


### :space_invader: BACKEND</br>
py -m venv venv</br>
.\venv\Scripts\Activate</br>
deverá aparecer um (venv) no início do seu console* </br>
pip install -r requirements.txt</br>
py src/manage.py migrate</br>
py src/manage.py runserver</br>


### :wrench: Testando</br>
Para testar a aplicação é necessário abrir o terminal, ir para tests e executar o comando de teste.</br>
*cd backend</br>
py src/manage.py test app</br>*
