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
    - https://django-crispy-forms.readthedocs.io/en/latest/install.html
    - ## Installation
      Install this plugin using `pip`:

          $ pip install django-crispy-forms

      ## Usage

      You will need to update your project's settings file to add ``crispy_forms``
      to your projects ``INSTALLED_APPS``. Also set
      ``bootstrap4`` as and allowed as the default template pack
      for your project::

          INSTALLED_APPS = (
              ...
              "crispy_forms",
              ...
          )

          CRISPY_TEMPLATE_PACK = "bootstrap4"

#### Desenvolvido por: *Jodson Alves, Marianne Dutra e Yan Sardinha*
