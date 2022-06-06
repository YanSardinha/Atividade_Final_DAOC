# TRABALHO FINAL DAOC

### Passos a serem reproduzidos
  - Instalar a biblioteca virtualenv
    - pip install virtualenv
  - Criar/entrar na virtualenv
    - python -m virtualenv -p=”Caminho onde está o python.exe” venv
    - venv\Scripts\activate
  - Assim que entrar na virtualenv, instalar o Django
    - pip install django
  - Após instalar o django, atualizar as migrações
    - py manage.py migrate
    - py manage.py migrate --run-syncdb
    - py manage.py makemigrations
