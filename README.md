# Instruções Gerador de Boletos Fake

#### Criar e ativar um ambiente virtual:
* pip install virtualenv
* virtualenv venv
* source venv/bin/activate

#### Instalar dependências:
* pip install -r requirements.txt

Chamar a função billet_generator.print_custom_data com os parâmetros 'Nome do beneficiário', 'Nome do pagador' e 'Valor a ser pago'. Como teste local, enviei os parâmetros 'Igreja de Teste', 'Fulano Testando' e 350,50.

#### Resultado:
![alt text](https://i.ibb.co/CsYTtZB/billet.jpg)