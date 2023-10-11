# amcom_challenge_backend

### :memo: Sobre a aplicação

Esta é uma aplicação FullStack para um desafio de admissão de vaga. Consiste num sistema de papelaria com cálculo de comissões e vendas, segue abaixo os critérios:</br>
O nosso cliente é uma papelaria hipotética que gostaria de registrar suas vendas e calcular a comissão de seus vendedores com base nas vendas feitas em dado período e nos percentuais de comissão cadastrados nos produtos vendidos.</br>
Um produto deve ter as seguintes informações: código, descrição, valor unitário e percentual de comissão, que pode variar entre 0 e 10%.</br>
Uma venda tem número da nota fiscal, data/hora, cliente, vendedor e uma lista de um ou mais produtos e suas quantidades vendidas.</br>
Clientes e vendedores têm nome, e-mail e telefone.</br>
O cálculo da comissão é feito aplicando-se o percentual cadastrado no produto ao valor total da venda do produto (qtd * valor unitário).</br>
Em alguns dias da semana, o percentual de comissão tem limites mínimos e máximos. Isso pode mudar com alguma frequência, por isso esses parâmetros devem ser configuráveis.</br>
Exemplo: Segundas-Feiras Min: 3% Max: 5%. Nesse caso uma venda nesse dia, de um produto de comissão 10% pagaria uma comissão de 5%. Já a venda de um produto de comissão 2% pagaria 3%.</br>
O total de comissão da venda é o total das somas das comissões dos itens da venda.</br>

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
