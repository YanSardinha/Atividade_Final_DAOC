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
  - Importante também instalar o crispy forms
    - https://github.com/django-crispy-forms/crispy-bootstrap5
    - ## Installation
      Install this plugin using `pip`:

          $ pip install crispy-bootstrap5

      ## Usage

      You will need to update your project's settings file to add ``crispy_forms``
      and ``crispy_bootstrap5`` to your projects ``INSTALLED_APPS``. Also set
      ``bootstrap5`` as and allowed template pack and as the default template pack
      for your project::

          INSTALLED_APPS = (
              ...
              "crispy_forms",
              "crispy_bootstrap5",
              ...
          )

          CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

          CRISPY_TEMPLATE_PACK = "bootstrap5"

#### Desenvolvido por: *Jodson Alves, Marianne Dutra e Yan Sardinha*
