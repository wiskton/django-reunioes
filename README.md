django-reunioes
===============

aplicação para gerenciar reuniões. Cadastra os emails e as pessoas, depois colocam as pessoas que vão participar da reunião.uniao.


entre na pasta dos seus projetos:

    cd ~/projetos


baixando django-reunioes:

    git clone git@github.com:willemallan/django-reunioes.git


entrando no diretório do projeto::

    cd django-reunioes


criando env:

    virtualenv ~/envs/djangoreunioes --no-site-packages


ativando env:

    source ~/envs/djangoreunioes/bin/activate


instalando requirements:

    pip install -r requirements.txt


alterar o settings.py:

    # -------------------------------------------------------------
    # EMAIL 
    # -------------------------------------------------------------

    EMAIL_HOST="smtp.gmail.com"
    EMAIL_PORT="587"
    EMAIL_HOST_USER="teste@teste.com.br"
    EMAIL_HOST_PASSWORD="123456"
    EMAIL_USE_TLS=True


criando banco de dados:

    python manage.py syncdb
    python manage.py migrate


rodando aplicação:

    python manage.py runserver
