
#!/bin/bash



# Функция для вывода сообщений об ошибках и завершения скрипта
error_exit() {
    echo "Ошибка: $1" >&2
    exit 1
}

# --- Конфигурация ---
# Укажите URL вашего GitHub репозитория
GIT_REPO_URL="https://github.com/slavaz950/List_Employ.git"
GIT_REPO="https://github.com/slavaz950/List_Employ.git"

# Имя директории для проекта
PROJECT_DIR="my_django_project"
PROJECT_NAME="my-django-app"

# Имя файла с зависимостями Python (если есть)
REQUIREMENTS_FILE="requirements.txt"


# Имя SQL скрипта для БД
DB_SETUP_SCRIPT="db_setup.sql"


DB_NAME="django_db"
DB_USER="django_user"
DB_PASSWORD="password"
SQL_SCRIPT="db_init.sql"
VENV_DIR="/opt/$PROJECT_NAME/venv"
SOURCE_DIR="/opt/$PROJECT_NAME/src"




# --- Определение версии Astra Linux и соответствующих зависимостей ---
# ASTRA_VERSION=""
# PYTHON_VERSION=""
# POSTGRES_VERSION=""
# DJANGO_VERSION=""


# Проверяем версию Astra Linux
ASTRALINUX_VERSION=$(lsb_release -sr)


# echo "Пожалуйста, укажите версию Astra Linux (1.6 или 1.7):"
# read ASTRA_VERSION

case "$$ASTRALINUX_VERSION" in
    "1.6")
        PYTHON_VERSION="python3.5"
        POSTGRESQL_VERSION="9.6"
        DJANGO_VERSION="1.10"
        ;;
    "1.7")
        PYTHON_VERSION="python3.7"
        POSTGRESQL_VERSION="11.1"
        DJANGO_VERSION="1.11"
        ;;
    *)
        # error_exit "Неподдерживаемая версия Astra Linux. Используйте 1.6 или 1.7."
        # ;;
		echo "Неверная версия Astra Linux ($ASTRALINUX_VERSION)"
        exit 1
		
esac


# Установим необходимые зависимости
sudo apt-get update || error_exit "Не удалось обновить списки пакетов."
sudo apt-get install -y $PYTHON_VERSION $POSTGRESQL_VERSION libpq-dev git python3-pip #  ГИГАЧАТ  
sudo apt-get install -y $PYTHON_VERSION $PYTHON_VERSION-dev $PYTHON_VERSION-venv postgresql-$POSTGRES_VERSION postgresql-contrib-$POSTGRES_VERSION git || error_exit "Не удалось установить системные зависимости."




# --- Установка зависимостей (пример, может потребоваться адаптация под specific Astra Linux) ---
echo "Установка необходимых пакетов..."

sudo apt-get update || error_exit "Не удалось обновить списки пакетов."
sudo apt-get install -y $PYTHON_VERSION $PYTHON_VERSION-dev $PYTHON_VERSION-venv postgresql-$POSTGRES_VERSION postgresql-contrib-$POSTGRES_VERSION git || error_exit "Не удалось установить системные зависимости."




# --- Создание виртуального окружения     ГИК---
# echo "Создание виртуального окружения..."
# mkdir -p "$PROJECT_DIR" || error_exit "Не удалось создать директорию проекта."
# cd "$PROJECT_DIR" || error_exit "Не удалось перейти в директорию проекта."
# $PYTHON_VERSION -m venv venv || error_exit "Не удалось создать виртуальное окружение."
# source venv/bin/activate || error_exit "Не удалось активировать виртуальное окружение."

# Создание виртуального окружения   ГИГАЧАТ
$PYTHON_VERSION -m venv $VENV_DIR
source $VENV_DIR/bin/activate



# Установим дополнительные зависимости  ГИГАЧАТ
pip install $DJANGO_VERSION
pip install psycopg2-binary






# Проверьте наличие файла с дополнительными зависимостями и установите их
if [ -f "$SOURCE_DIR/requirement.txt" ]; then
    pip install -r $SOURCE_DIR/requirement.txt
fi





# Скачать проект из GitHub
rm -rf $SOURCE_DIR || true
git clone $GIT_REPO $SOURCE_DIR


# Переместимся в папку проекта
cd $SOURCE_DIR


# Подготовим базу данных
sudo -u postgres createuser -d $DB_USER
sudo -u postgres createdb -O $DB_USER $DB_NAME
sudo -u postgres psql -d $DB_NAME -a -f $SQL_SCRIPT

# Настроим конфигурационные файлы проекта (settings.py):
sed -i "s/DATABASE_NAME/'$DB_NAME'/g" settings.py
sed -i "s/DATABASE_USER/'$DB_USER'/g" settings.py
sed -i "s/DATABASE_PASSWORD/'$DB_PASSWORD'/g" settings.py

# Выполнение миграций модели базы данных
python manage.py migrate

# Сборка статичных файлов
python manage.py collectstatic --noinput

# Запустим внутренний сервер Django
python manage.py runserver 0.0.0.0:8000






# --- Клонирование репозитория ---   ГИК
# echo "Клонирование GitHub репозитория..."
# git clone "$GIT_REPO_URL" . || error_exit "Не удалось клонировать репозиторий."

# --- Установка зависимостей Python ---
# echo "Установка зависимостей Python..."
# pip install --upgrade pip || error_exit "Не удалось обновить pip."
# pip install django==$DJANGO_VERSION || error_exit "Не удалось установить Django."
# Установка остальных зависимостей из requirements.txt (предполагается, что он есть)
# if [ -f "requirements.txt" ]; then
   #  pip install -r requirements.txt || error_exit "Не удалось установить зависимости из requirements.txt."
# else
    # echo "Файл requirements.txt не найден. Установите зависимости вручную, если необходимо."
# fi

# --- Настройка PostgreSQL ---
# echo "Настройка PostgreSQL..."
# Предполагается, что PostgreSQL запущен и сконфигурирован для работы с пользователем
# Вам может потребоваться создать пользователя и базу данных вручную или добавить соответствующие команды сюда
# Пример:
# sudo -u postgres psql -c "CREATE DATABASE mydatabase;"
# sudo -u postgres psql -c "CREATE USER myuser WITH PASSWORD 'mypassword';"
# sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;"

# АЛЬТЕРНАТИВНЫЙ ПОДХОД К ПРЕДВАРИТЕЛЬНОЙ НАСТРОЙКЕ PostgreSQL
# Предполагается, что PostgreSQL установлен, запущен, и пользователь 'postgres' имеет доступ.
# Вам может потребоваться создать БД и пользователя вручную или добавить команды.
# DB_NAME="mydjangodb" # Ваше имя базы данных
# DB_USER="mydjangouser" # Ваш логин пользователя БД
# DB_PASS="mypassword" # Ваш пароль БД




# --- Применение SQL скрипта ---  ГИК
# echo "Применение SQL скрипта для базы данных..."
# if [ -f "db_setup.sql" ]; then
   #  sudo -u postgres psql -d mydatabase -f db_setup.sql || error_exit "Не удалось применить SQL скрипт."
# else
    # error_exit "SQL скрипт 'db_setup.sql' не найден в репозитории."
# fi

# --- Миграции Django ---
# echo "Применение миграций Django..."
# python manage.py migrate || error_exit "Не удалось применить миграции Django."

# --- Запуск тестового сервера Django (для проверки) ---
# echo "Проверка запуска сервера Django..."
# python manage.py runserver 8000 & # Запуск в фоновом режиме
# TEST_SERVER_PID=$!
# sleep 5 # Даем время серверу запуститься

# if ps -p $TEST_SERVER_PID > /dev/null; then
    # echo "Сервер Django успешно запущен на http://127.0.0.1:8000/"
   #  echo "Для остановки сервера нажмите Ctrl+C в терминале, где он запущен."
   #  echo "Для завершения работы скрипта, введите 'kill $TEST_SERVER_PID' в другом терминале."
# else
   #  echo "Не удалось запустить сервер Django. Проверьте логи ошибок."
# fi

# echo "--- Развертывание Django проекта завершено ---"

# Команда для выхода из виртуального окружения: deactivate
