# EVENTEX

Sistema de Eventos encomendado pela Morena.

## Como desenvolver ?

1. Clone o repositório.
2. Crie um virtualenv com python 3.5
3. Ative o virtualenv.
4. Instale as  depedencias.
5.Configure a instancia com o .env
6. Execute os testes.

````console
git clone git@github.com:VictorOliveiraPy/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirementes-dev.txt
cp contrib/env-sample .env
python manage.py test

````

## Como fazer o deploy ?
1. Crie um instancia  no heroku.
2. Envie as configuracoes para o heroku.
3. Define uma SECRET_KEY segura para instância.
4. Define DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o heroku

````console
heroku create minhainstancia
heroko config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configro o emil
git push heroku master --force

````
