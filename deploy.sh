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
PROJECT_DIR="/opt/List_Employ"    #    /home/List_Employ
DB_NAME="ListEmpDB"
# DB_USER="postgres"
# DB_PASS="Cen78Ter19"
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
            PYTHON_PKG="python3.5 python3.5-pip python3.5-venv"   #  python3-pip python3-venv
            DJANGO_VERSION="1.10"
            ;;
        "1.7")
            DB_PKG="postgresql-11 postgresql-contrib-11"
            PYTHON_PKG="python3.7 python3-pip python3.7-venv  "    #  python3-pip python3-venv
            DJANGO_VERSION="1.11"
            ;;
    esac

    # Обновление списка пакетов
    sudo apt-get update

    # Установка Git
    sudo apt install -y git

    # Установка PostgreSQL
    log "Установка PostgreSQL..."
    sudo apt-get install -y $DB_PKG

    # Установка Python и инструментов
    log "Установка Python и pip..."
    sudo apt-get install -y $PYTHON_PKG
   #  sudo apt-get install -y python3-pip
   



    # Зависимости для сборки Python‑пакетов и работы с PostgreSQL
    sudo apt-get install -y build-essential libpq-dev python3-dev

    

    log "Системные зависимости установлены"
}

# Настройка PostgreSQL
setup_postgresql() {
    log "Настройка PostgreSQL..."

    # Запуск и включение автозапуска службы
    sudo systemctl start postgresql     #  Запускаем службу PostgreSQL
    sudo systemctl enable postgresql    # Автозапуск службы PostgreSQL после каждой перезагрузки 

    # Создание пользователя БД (Если в postgresql не существует пользователь )
    # sudo -u postgres psql -c "DO \$$  
      #   BEGIN
          #   IF NOT EXISTS (SELECT * FROM pg_catalog.pg_user WHERE usename = '$DB_USER') THEN  
            #     CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';
          #   END IF;
       #  END
   #  \$$;"


    # Создание базы данных
    #  sudo -u postgres psql -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;" || true

   #  log "PostgreSQL настроен. Пользователь: $DB_USER, БД: $DB_NAME"
}

# Клонирование репозитория
clone_repository() {
    log "Клонирование репозитория из $REPO_URL..."

    if [ -d "$PROJECT_DIR" ]; then  #   Проверяем существует ли папка проекта
        warn "Директория проекта $PROJECT_DIR уже существует. Выполняется git pull..."
        cd "$PROJECT_DIR"   # Переходим в директорию проекта
        git pull   #   извлекаем изменения из удалённого репозитория и объединяем их с текущей локальной веткой
    else #  Если папка проекта не найдена
        mkdir -p "$PROJECT_DIR" #  Создаём папку проекта
        cd "$PROJECT_DIR"      #  Переходим в созданную папку проекта
        git clone "$REPO_URL" .   #  Клонируем целевой репозиторий
    fi

    log "Репозиторий успешно клонирован в $PROJECT_DIR"
}

# Создание виртуального окружения и установка Python‑зависимостей
setup_python_env() {
    log "Создание виртуального окружения Python..."
    python3 -m venv venv       # Создаём виртуальное окружение 
    source venv/bin/activate   # Активируем виртуальное окружение





    # Обновляем pip-менеджер
    log "Обновление pip..."
    pip install --upgrade pip

    # Установка Django нужной версии
    log "Установка Django $DJANGO_VERSION..."
    pip install "Django==$DJANGO_VERSION"

    # Установка драйвера PostgreSQL
    log "Установка psycopg2..."
    pip install psycopg2-binary

    # Если есть файл с зависимостями, устанавливаем их
    if [ -f "$REQUIREMENTS_FILE" ]; then  # Если файл с зависимостями  () найден, то .....
        log "Установка дополнительных зависимостей из $REQUIREMENTS_FILE..."
        pip install -r "$REQUIREMENTS_FILE" # устанавливаем зависимости проекта 
    else
        warn "Файл $REQUIREMENTS_FILE не найден. Пропускаем установку дополнительных зависимостей."
    fi

    log "Виртуальное окружение настроено"
}

# Применение SQL‑скрипта для инициализации БД
apply_sql_script() {
    log "Поиск SQL‑скрипта '$SQL_SCRIPT_NAME'..."

    if [ -f "$SQL_SCRIPT_NAME" ]; then  # Проверяем доступен ли файл с sql-скриптом
        log "Применение SQL‑скрипта к базе данных $DB_NAME..."
        sudo -u postgres psql -d "$DB_NAME" -f "$SQL_SCRIPT_NAME"
        log "SQL‑скрипт успешно применён"
    else
        warn "SQL‑скрипт '$SQL_SCRIPT_NAME' не найден. Пропускаем инициализацию БД."
    fi
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
    clone_repository  # clone_repository
    setup_python_env   # setup_python_env   # Создание виртуального окружения и установка Python‑зависимостей
    apply_sql_script   # apply_sql_script      # Применение SQL‑скрипта для инициализации БД
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