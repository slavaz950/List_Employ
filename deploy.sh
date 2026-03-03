#!/bin/bash

# Скрипт для развёртывания Django‑проекта на Astra Linux (1.6 / 1.7)
# Требует запуска с правами sudo

# set -euo pipefail  # Строгий режим: прерывать при ошибках, неинициализированных переменных, ошибках в пайпах


# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Логирование
log() { echo -e "${GREEN}[INFO]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

# Конфигурация 
REPO_URL="https://github.com/slavaz950/List_Employ.git"
PROJECT_DIR="/opt/List_Employ"    #   
DB_NAME="ListEmpDB"
DB_USER="postgres"
DB_PASS="Cen78Ter19"
SQL_SCRIPT_NAME="sql_data.sql"  # Имя SQL‑скрипта в репозитории
# SETTINGS_FILE="List_Employ\settings.py"  # Путь к settings.py в проекте  # \List_Employ\List_Employ\settings.py           myproject/settings.py  
REQUIREMENTS_FILE="requirements.txt"  # Файл с зависимостями Python



# Проверка прав sudo
# check_sudo() {
   #  if [[ $EUID -ne 0 ]]; then
     #    error "Этот скрипт должен запускаться с правами sudo"
   #  fi
# }

# Определение версии Astra Linux
detect_astra_version() {
    if [[ ! -f /etc/astra_version ]]; then  #   Проверка наличия файла /etc/astra_version
        error "Не удалось найти /etc/astra_version. Это Astra Linux?"
    fi

    if grep -q "1.6" /etc/astra_version; then  # Ищем версию 1.6
        ASTRA_VERSION="1.6"
        log "Обнаружена Astra Linux 1.6"
    elif grep -q "1.7" /etc/astra_version; then  # Ищем версию 1.7
        ASTRA_VERSION="1.7"
        log "Обнаружена Astra Linux 1.7"
    else
        cat /etc/astra_version  # выводит содержимое файла на экран (чтобы пользователь увидел, какая версия обнаружена)
        error "Неподдерживаемая версия Astra Linux. Требуется 1.6 или 1.7"
    fi
}












# Установка зависимостей в зависимости от версии
install_dependencies() {
    log "Установка системных зависимостей для Astra Linux $ASTRA_VERSION..."

    case "$ASTRA_VERSION" in
        "1.6")
            DB_PKG="postgresql-9.6 postgresql-contrib-9.6"
            PYTHON="python3.5"   #  python3-pip python3-venv
            PYTHON_PIP="python3.5-pip"
            PYTHON_VENV="python3.5-venv"
            DJANGO_VERSION="1.10"
            ;;
        "1.7")
            DB_PKG="postgresql-11 postgresql-contrib-11"
            PYTHON="python3.7"    #  python3-pip python3-venv
            PYTHON_PIP="python3-pip"
            PYTHON_VENV="python3.7-venv"
            DJANGO_VERSION="1.11"
            ;;
    esac

    log "Текущий пользователь:    $USER    "

    #  log "Создание папки для загрузки недостающих пакетов"
   #   sudo mkdir -p /opt/downloads/
   #   log "Папка для загрузки пакетов создана"



   #   log "Переходим в папку в которую будем загружать пакеты"
   #   sudo cd /opt/downloads/
    #  log "Переход осуществлён"

#  $

   #   log "Качаем пакет $PYTHON_VENV"
   #   sudo apt download $PYTHON_VENV
   #   log "Пакет $PYTHON_VENV загружен"


  #    log "Качаем пакет $PYTHON_PIP"
  #    sudo apt download $PYTHON_PIP
   #   log "Пакет $PYTHON_PIP загружен"

    #  log "Качаем пакет python3-pip"
    #  sudo apt download python-pip-whl
     # log "Обновление списка пакетов"

  #    log "Переходим к установке недостающих пакетов"
   #   sudo dpkg --force-depends -i /opt/downloads/*.deb  # Устанавливаем все пакеты с разрешением .deb находящиеся в папке
  #    log "Установка недостающих пакетов завершена"

    # URL репозитория (измените на нужный)
    REPO_URL="deb https://download.astralinux.ru/astra/stable/orel/repository/pool/main/"

    # Добавляем репозиторий в sources.list
    echo "$REPO_URL" | sudo tee -a /etc/apt/sources.list > /dev/null

    # Обновляем кэш пакетов
    # sudo apt update


    # Обновление списка пакетов
    log "Обновление списка пакетов"
    sudo apt-get update
    log "Список пакетов обновлён"

    # Установка Git
    log "Установка Git"
    sudo apt install -y git
    log "Git установлен"

    # Установка PostgreSQL
    log "Установка PostgreSQL..."
    sudo apt-get install -y $DB_PKG
    log "PostgreSQL установлен"

    # Установка Python 
    log "Установка Python"
    sudo apt-get install -y $PYTHON
    log "Python установлен"
   
    # Установка PIP
    log "Установка PIP-менеджера"
    sudo apt-get install -y $PYTHON_PIP
    log "PIP-менеджер установлен"

    # Установка VENV
    log "Установка VENV"
    sudo apt-get install -y $PYTHON_VENV
    log "VENV установлен"


    # Зависимости для сборки Python‑пакетов и работы с PostgreSQL
    log "Зависимости для сборки Python‑пакетов и работы с PostgreSQL"

    log "Установка build-essential"
    sudo apt-get install -y build-essential
    log "build-essential установлен"

    log "Установка libpq-dev" 
    sudo apt-get install -y libpq-dev
    log "libpq-dev установлен"


    log "Установка python3-dev" 
    sudo apt-get install -y python3-dev
    log "python3-dev установлен"


    log "Системные зависимости установлены"
}

# Настройка PostgreSQL
setup_postgresql() {
    log "Настройка PostgreSQL..."

    # Запуск и включение автозапуска службы
    log "Запускаем службу PostgreSQL"
    sudo systemctl start postgresql     #  Запускаем службу PostgreSQL
    log "Служба PostgreSQL запущена"

    log "Включаем автозагрузку службу PostgreSQL"
    sudo systemctl enable postgresql    # Автозапуск службы PostgreSQL после каждой перезагрузки 
    log "Автозагрузка службы PostgreSQL запущена"

    # Создание пользователя БД (Если нужен какой-то другой пользователь, не postgres )
    # sudo -u postgres psql -c "DO \$$  
      #   BEGIN
          #   IF NOT EXISTS (SELECT * FROM pg_catalog.pg_user WHERE usename = '$DB_USER') THEN  
            #     CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';
          #   END IF;
       #  END
   #  \$$;"


    # Создание базы данных
    log "Задаём пароль для пользователя postgres"
    psql -U postgres -c "ALTER USER postgres WITH PASSWORD '$DB_PASS';"  #  Задаём пароль для пользователя postgres
    log "Пароль для пользователя postgres успешно задан"
    log "Создаём базу данных $DB_NAME с укзанием владельца: $DB_USER "
    sudo -u postgres psql -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;" || true # true гарантирует, что скрипт продолжит выполнение даже при ошибке создания БД. 
    log "База данных $DB_NAME успешно создана" 
    log "PostgreSQL настроен. Пользователь: $DB_USER, БД: $DB_NAME"


    log "Поиск SQL‑скрипта '$SQL_SCRIPT_NAME'..."

    if [ -f "$SQL_SCRIPT_NAME" ]; then  # Проверяем доступен ли файл с sql-скриптом
        log "SQL‑скрипта '$SQL_SCRIPT_NAME' найден"
        log "Применение SQL‑скрипта к базе данных $DB_NAME..."
        sudo -u postgres psql -d "$DB_NAME" -f "$SQL_SCRIPT_NAME"
        log "SQL‑скрипт успешно применён"
    else
        warn "SQL‑скрипт '$SQL_SCRIPT_NAME' не найден. Пропускаем инициализацию БД."
    fi




}




# СОДЕРЖИМОЕ ОБЪЕДИНИЛ С ФУНКЦИЕЙ НАХОДЯЩЕЙСЯ ВЫШЕ этот кусок пока оставил. Если будет не нужен - УДАЛИТЬ
# Применение SQL‑скрипта для инициализации БД
# apply_sql_script() {
   #  log "Поиск SQL‑скрипта '$SQL_SCRIPT_NAME'..."

   #  if [ -f "$SQL_SCRIPT_NAME" ]; then  # Проверяем доступен ли файл с sql-скриптом
      #   log "Применение SQL‑скрипта к базе данных $DB_NAME..."
       #  sudo -u postgres psql -d "$DB_NAME" -f "$SQL_SCRIPT_NAME"
      #   log "SQL‑скрипт успешно применён"
   #  else
     #    warn "SQL‑скрипт '$SQL_SCRIPT_NAME' не найден. Пропускаем инициализацию БД."
   #  fi
# }







# Клонирование репозитория
clone_repository() {
    log "Клонирование репозитория из $REPO_URL..."

    if [ -d "$PROJECT_DIR" ]; then  #   Проверяем существует ли папка проекта
        warn "Директория проекта $PROJECT_DIR уже существует. Выполняется git pull..."
        cd "$PROJECT_DIR"   # Переходим в директорию проекта  PROJECT_DIR="/opt/List_Employ"
        git pull   #   извлекаем изменения из удалённого репозитория и объединяем их с текущей локальной веткой
    else #  Если папка проекта не найдена
      sudo mkdir -p "$PROJECT_DIR" #  Создаём папку проекта
      sudo chown $USER:$USER "$PROJECT_DIR"  # Назначаем текущего пользователя владельцем каталога
        cd "$PROJECT_DIR"      #  Переходим в созданную папку проекта
        git clone "$REPO_URL" .   #  Клонируем целевой репозиторий
    fi

    log "Репозиторий успешно клонирован в $PROJECT_DIR"
}

# Создание виртуального окружения и установка Python‑зависимостей
setup_python_env() {
    log "Создание виртуального окружения Python..."
    log "Переход в целевой каталог"
    cd /opt/   # Переход в каталог в котором будет создаваться виртуальное окружение
    log "Переход в каталог осуществлён"
    log "Создаём виртуальное окружение"
    python3 -m venv venv       # Создаём виртуальное окружение 
    log "Виртуальное окружение создано"
    log "Активируем виртуальное окружение"
    source venv/bin/activate   # Активируем виртуальное окружение
    # source /opt/venv/bin/activate   # Активируем виртуальное окружение
    log "Виртуальное окружение активировано"


 # Обновляем pip-менеджер
    log "Обновление pip..."
    pip install --upgrade pip
    log "pip-менеджер обновлён"








    # Установка Django нужной версии
    log "Установка Django $DJANGO_VERSION..."
    pip install "Django==$DJANGO_VERSION"
    log "Django $DJANGO_VERSION установлен"

    # Установка драйвера PostgreSQL
    log "Установка psycopg2..."
    pip install psycopg2-binary
    log " psycopg2 установлен"



    # Если есть файл с зависимостями, устанавливаем их
    if [ -f "$REQUIREMENTS_FILE" ]; then  # Если файл с зависимостями  () найден, то .....
        log "Установка дополнительных зависимостей из $REQUIREMENTS_FILE..."
        pip install -r "$REQUIREMENTS_FILE" # устанавливаем зависимости проекта 
    else
        warn "Файл $REQUIREMENTS_FILE не найден. Пропускаем установку дополнительных зависимостей."
    fi

    log "Виртуальное окружение настроено"
}






# Настройка Django settings.py
# configure_django() {
    # log "Настройка Django settings.py..."

   #  if [ ! -f "$SETTINGS_FILE" ]; then
       #  error "Файл настроек Django '$SETTINGS_FILE' не найден. Проверьте путь."
    # fi

    # Резервное копирование оригинального файла
    # cp "$SETTINGS_FILE" "$SETTINGS_FILE.backup"

    # Заменяем настройки DATABASES в settings.py
    # sed -i "s/DATABASES = {.*/DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql', 'NAME': '$DB_NAME', 'USER': '$DB_USER', 'PASSWORD': '$DB_PASS', 'HOST': 'localhost', 'PORT': '5432'}}/" "$SETTINGS_FILE"

    # Разрешаем доступ с localhost для разработки
    # sed -i "s/ALLOWED_HOSTS = \[.*/ALLOWED_HOSTS = ['localhost', '127.0.0.1']/" "$SETTINGS_FILE"

    # log "Настройки БД и ALLOWED_HOSTS в settings.py обновлены"
# }





# Запуск миграций Django и сбор статических файлов
run_django_setup() {
    log "Запуск миграций Django..."
    python manage.py migrate --noinput

    log "Сбор статических файлов..."
    python manage.py collectstatic --noinput

    log "Django‑проект настроен и готов к запуску"
}


# Основной процесс развёртывания проекта
main() {
    log "Начало развёртывания Django‑проекта"

    # check_sudo   # check_sudo   # Проверка прав sudo
    detect_astra_version  # detect_astra_version    # Определение версии Astra Linux
    install_dependencies   # install_dependencies   # Установка зависимостей в зависимости от версии
    setup_postgresql  #  setup_postgresql     # Настройка PostgreSQL
    clone_repository  # clone_repository    # Клонирование репозитория
    setup_python_env   # setup_python_env   # Создание виртуального окружения и установка Python‑зависимостей
   #  apply_sql_script   # apply_sql_script      # Применение SQL‑скрипта для инициализации БД # В КОДЕ ЗАКОМЕНЧЕНА ВОЗМОЖНО - УДАЛЯТЬ
  #   configure_django  # НЕ ИСПОЛЬЗУЮ
    run_django_setup  # run_django_setup       # Запуск миграций Django и сбор статических файлов

    log "Развёртывание завершено успешно!"
    log "Проект расположен в: $PROJECT_DIR"
    log "Для запуска сервера выполните:"
    log "  cd $PROJECT_DIR && source venv/bin/activate && python manage.py runserver 0.0.0.0:8000"
    log "Доступ к проекту: http://localhost:8000"
    log "Для остановки сервера нажмите Ctrl+C"
}

# ОБРАБОТКА СИГНАЛОВ ДЛЯ КОРРЕКТНОГО ЗАВЕРШЕНИЯ
# (Команда trap в Bash позволяет перехватывать системные сигналы и выполнять заданные действия при их получении)
# В данном случае реагируем на сигналы INT и TERM
# INT - обычно генерируется при нажатии Ctrl + C в терминале.По умолчанию приводит к немедленному завершению скрипта.
# TERM - стандартный сигнал для запроса завершения процесса.Отправляется командами kill <PID> (без дополнительных флагов) или системными службами 
# при штатном завершении работы. По умолчанию также завершает скрипт, но даёт возможность выполнить очистку перед выходом.
trap 'error "Скрипт прерван пользователем"' INT TERM

# Запуск процесса развёртывания
main "$@"







# Запуск Django development server  НАВЕРНО НУЖНО ЭТОТ ОШМЁТОК УДАЛИТЬ
# start_django_server() {
   #  log "Запуск Django development server на http://localhost:8000..."

    # Активируем виртуальное окружение
   #  source venv/bin/activate

    # Запускаем сервер в фоне
   #  nohup python manage.py runserver 0.0.0.0:8000 > django_server.log 2>&1 &

    # Сохраняем PID процесса
   #  echo $! > django_server.pid

    # log "Django server запущен. PID: $(cat django_server.pid)"
   #  log "Логи сервера записываются в django_server.log"
   #  log "Доступ к проекту: http://localhost:8000