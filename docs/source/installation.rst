Деплой на pythonanywhere.com
====================================
Везде ниже предполагается, что вы зашли в свой аккаунт на pythonanywhere и ваш username *dosrok_name* **(далее логин выделяется курсивом)**

Пошаговая инструкция
--------------------

Шаг 1
~~~~~

Перейдите на вкладку "Web" и добавьте новое приложение: "Add a new web app".

Укажите нужное доменное имя. Нажмите "Next".

Выберите "Manual configuration" из списка опций. Нажмите "Next" и дождитесь завершения процесса создания приложения.

Теперь по адресу *dosrok_name*.pythonanywhere.com вы должны видеть страницу-заглушку.

Произведите нужные настройки у вашего доменного регистратора -- создайте CNAME record, указывающий на адрес, указанный во вкладке "Web" для вашего приложения (webapp-XXXX.pythonanywhere.com).
Подробнее на https://www.pythonanywhere.com/wiki/OwnDomains

Шаг 2
~~~~~
Перейдите на вкладку "Databases" и задайте пароль (секция MySQL password). 

По умолчанию должна быть создана база *dosrok_name*\ $default. Если же её нет, создайте базу с таким именем в секции Create a database.

Шаг 3
~~~~~

Перейдите на вкладку "Consoles" и создайте Bash-консоль

Введите следующую команду, чтобы загрузить исходники

.. code-block:: shell

    git clone https://github.com/alexsyrom/dosrok.ru.git

Перейдите в созданную папку с кодом

.. code-block:: shell

    cd dosrok.ru

Создайте виртуальное окружение

.. code-block:: shell

    mkvirtualenv --python=/usr/bin/python3.4 dosrok

Если произошла ошибка *"mkvirtualenv: command not found"*, введите следующие команды:

.. code-block:: shell

    echo '' >> ~/.bashrc && echo 'source virtualenvwrapper.sh' >> .bashrc
    source virtualenvwrapper.sh

Приглашение консоли должно теперь начинаться с (dosrok). Если этого не произошло, активируйте окружение вручную:

.. code-block:: shell

    workon dosrok

Установите зависимости:
    
.. code-block:: shell

    pip install -r requirements.txt

В папке **dosrok** создайте файл **local_settings.py** со следующим содержанием (обратите внимание на комментарии):

.. code-block:: python
    
    SECRET_KEY = 'kzqoq0=z1_&8lc8#nj=v@!a6-(7a0rvycm*s1+rhe5)s(k%2mr' 
    '''
    следует сгенерировать свой secret_key, 
    например, с помощью этого сайта 
    http://www.miniwebtool.com/django-secret-key-generator/
    '''

    DEBUG = False

    # измените набор допустимых адресов при необходимости
    ALLOWED_HOSTS = ['dosrok.ru', 'www.dosrok.ru', '*dosrok_name*.pythonanywhere.com']
 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'dosrok$default',
            'USER': 'dosrok',
            'PASSWORD': 'password', # пароль, который вы задали на вкладке "Databases"
            'HOST': 'dosrok.mysql.pythonanywhere-services.com',
            'PORT': '3306',
        }
    }

Вернитесь в папку проекта

.. code-block:: shell

    cd ~/dosrok.ru

Подготовьте базу данных к работе

.. code-block:: shell

    python manage.py migrate


Создайте суперпользователя.

.. code-block:: shell

    python manage.py createsuperuser

Соберите static файлы в нужную папку

.. code-block:: shell

    python manage.py collectstatic

Шаг 4
~~~~~

Вновь перейдите на вкладку "Web". Отредактируйте файл WSGI (расположен в секции Code), заменив содержимое на следующий код:

.. code-block:: python

    # To use your own django app use code like this:
    import os
    import sys

    # assuming your django settings file is at '/home/*dosrok_name*/dosrok.ru/dosrok/settings.py'
    # and your manage.py is is at '/home/*dosrok_name*/dosrok.ru/manage.py'
    path = '/home/*dosrok_name*/dosrok.ru'
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'dosrok.settings'

    # then, for django >=1.5:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()


Вернитесь на вкладку "Web". В секции "Virtualenv" настройте путь к окружению. Можно указать или полный путь "/home/*dosrok_name*/.virtualenvs/dosrok" или просто ввести dosrok, система сама дополнит путь.

В секции "Static files" добавьте следующие записи:

.. code-block:: shell

    URL  Directory
    /static /home/*dosrok_name*/dosrok.ru/static
    /media /home/*dosrok_name*/dosrok.ru/media

Теперь нажмите на кнопку "Reload" и дождитесь перезагрузки приложения.

Шаг 5
~~~~~

Перейдите на *dosrok_name*.pythonanywhere.com/admin и войдите как суперпользователь, которого вы создали в конце шага 3. 

В административном интерфейсе добавьте первый "Предмет". Пока не создано ни одного предмета, при заходе на главную страницу будет выдана страница с ошибкой. Если в базе существует несколько предметов, то на главной будет информация о предмете, добавленном раньше остальных.

На этом процесс развёртывания сайта окончен. 
