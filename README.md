# dosrok.ru
This is going to be another great website hosted by PythonAnywhere.

# Деплой на pythonanywhere.com
//Предполагается, что вы зашли в свой аккаунт на pythonanywhere и ваш юзернэйм dosrok

##list
Перейдите на вкладку "Web" и добавьте новое приложение "Add a new web app".

Укажите нужное доменное имя. Нажмите "Next".

Выберите "Manual configuration" из списка опций. Нажмите "Next" и дождитесь завершения процесса создания приложения.
Теперь вы при заходе на dosrok.pythonanywhere.com вы должны видеть сайт-заглушку.

Произведите нужные настройки у вашего доменного регистратора -- создайте CNAME record, указывающий на адрес, указанный во вкладке "Web" для вашего приложения (webapp-XXXX.pythonanywhere.com).
Подробнее на https://www.pythonanywhere.com/wiki/OwnDomains

##list
Перейдите на вкладку "Databases" и задайте пароль (секция MySQL password). 

По умолчанию должна быть создана база dosrok$default. Если же её нет, создайте базу в секции Create a database

##list
Перейдите на вкладку "Consoles" и создайте Bash-консоль

Введите следующую команду, чтобы загрузить исходники
git clone https://github.com/alexsyrom/dosrok.ru.git

Перейдите в созданную папку с кодом
cd dosrok.ru

Создайте виртуальное окружение
mkvirtualenv --python=/usr/bin/python3.4 dosrok
Если произошла ошибка "mkvirtualenv: command not found", введите следующие команды:
echo '' >> ~/.bashrc && echo 'source virtualenvwrapper.sh' >> .bashrc
source virtualenvwrapper.sh

Приглашение консоли должно теперь начинаться с (dosrok). Если нет, то активируйте окружение вручную:
workon dosrok

Установите зависимости:
pip install -r requirements.txt

В папке dosrok создайте файл local_settings.py со следующим содержанием:
файл
SECRET_KEY = 'kzqoq0=z1_&8lc8#nj=v@!a6-(7a0rvycm*s1+rhe5)s(k%2mr' #следует сгенерировать свой secret_key, например, с помощью этого сайта http://www.miniwebtool.com/django-secret-key-generator/

DEBUG = False
 
ALLOWED_HOSTS = ['dosrok.ru', 'www.dosrok.ru', 'dosrok.pythonanywhere.com']
 
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'dosrok$default',
         'USER': 'dosrok',
         'PASSWORD': 'password', #введите здесь пароль, который вы задали на вкладке "Databases"
         'HOST': 'dosrok.mysql.pythonanywhere-services.com',
         'PORT': '3306',
    }
}
файл

Вернитесь в папку проекта
cd ~/dosrok.ru

Подготовьте базу данных к работе
python manage.py migrate

Создайте суперпользователя.
python manage.py createsuperuser

Соберите static файлы в нужную папку
python manage.py collectstatic

##list
Вновь перейдите на вкладку "Web". Отредактируйте файл WSGI (расположен в секции Code), заменив содержимое на следующий код:
файл
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/dosrok/dosrok.ru/dosrok/settings.py'
# and your manage.py is is at '/home/dosrok/dosrok.ru/manage.py'
path = '/home/dosrok/dosrok.ru'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'dosrok.settings'

# then, for django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
файл

Вернитесь на вкладку "Web". В секции "Virtualenv" настройте путь к окружению. Можно указать или полный путь "/home/dosrok/.virtualenvs/dosrok" или просто ввести dosrok, система сама дополнит до полного пути.

В секции "Static files" добавьте следующие записи:
URL  Directory
/static /home/dosrok/dosrok.ru/static
/media /home/dosrok/dosrok.ru/media

Теперь нажмите на кнопку "Reload" и дождитесь перезагрузки приложения.

##list
Перейдите на dosrok.pythonanywhere.com/admin и войдите как суперпользователь, которого вы создали. 

Теперь добавьте "Предмет". Пока не создано ни одного предмета, при заходе на главную страницу будет выдана страница с ошибкой. Если будет несколько предметов, то на главной будет информация о предмете, добавленном раньше остальных.

На этом процесс развёртывания сайта окончен. 
