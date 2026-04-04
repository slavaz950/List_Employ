#!/bin/bash

# Скрипт для развёртывания Django‑проекта на Astra Linux (1.6 / 1.7)
# Требует запуска с правами sudo

set -euo pipefail  # Строгий режим: прерывать при ошибках, неинициализированных переменных, ошибках в пайпах


# Задаём цвета для вывода информационных сообщений
RED='\033[0;31m'     # Красный
GREEN='\033[0;32m'   # Зелёный
YELLOW='\033[1;33m'  # Жёлтый
NC='\033[0m'         # Без цвета

# Разложим одну из строк на примере первой строки  RED='\033[0;31m'   на части:

#     \033 — escape‑символ (ESC) в восьмеричной записи. Он сигнализирует терминалу, что далее идёт управляющая последовательность, а не обычный текст

#      [ — начало управляющей последовательности (Control Sequence Introducer, CSI). Указывает, что дальше следуют параметры форматирования.

#      0;31 — параметры цвета и стиля:
#             0 — сброс всех атрибутов (нормальный стиль, без жирного, подчёркивания и т. д.); 
#             31 — код цвета текста: красный.

#      m — завершение управляющей последовательности. Говорит терминалу: «применить указанные стили».



# Логирование (для префиксов сообщений используем цвета заданные выше)
log() { echo -e "${GREEN}[INFO]${NC} $1"; }  # Определение функции log для унифицированного вывода информационных сообщений с префиксом [INFO]
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; } # Определение функции warn - вывод предупреждений (warnings) в терминале с префиксом [WARN] цвет -жёлтый
error() { echo -e "${RED}[ERROR]${NC} $1"; exit 1; } # Определение функции error - вывод сообщения об ошибке с префиксом [ERROR] (красный). Немедленное завершение с кодом ошибки 1

# Определение общих параметров (для обоих ОС) для развёртывания проекта 
REPO_URL="https://github.com/slavaz950/List_Employ.git"   # Определение git-ресурса для загрузки файлов проекта
PROJECT_DIR="/opt/List_Employ"                            # Определение папки проекта  
DB_NAME="ListEmpDB"                                       # Определение имени базы данных
DB_USER="postgres"                                        # Определение пользователя-владельца базы данных (наделённого админскими правами)
DB_PASS="Cen78Ter19"                                      # Пароль пользователя postgres
SQL_SCRIPT_NAME="/opt/List_Employ/sql_data.sql"           # Имя SQL‑скрипта выполняющего заполнение базы данных данными
PYTHON="python3"                                          # Имя пакета
PYTHON_PIP="python3-pip"                                  # Имя пакета
PYTHON_VENV="python3-venv"                                # Имя пакета
GIT="git"                                                 # Имя пакета
REQUIREMENTS_FILE="/opt/List_Employ/requirements.txt"     # Файл с зависимостями Python

# Определение версии Astra Linux
 detect_astra_version() {
     if [[ ! -f /etc/astra_version ]]; then  #   Проверка наличия файла /etc/astra_version (файл содержит информацию о версии установленной ОС)
        error "Не удалось найти /etc/astra_version. Вы уверены что это Astra Linux?"
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

# Функция для проверки установки пакета и его последующей установки в случае его отсутствия (единственный параметр: Имя пакета)
check_package_installed() {
    local package_name="$1"  # запоминаем значение входящего параметра
  
    # Проверяем входные данные
    if [[ -z "$package_name" ]]; then
        echo "Ошибка: не указано имя пакета для проверки."
        return 2  # ошибка (не указано имя пакета)
    fi

    # Проверяем статус пакета
    if dpkg -s "$package_name" &> /dev/null; then
       echo "Пакет '$package_name' уже установлен в системе."
       local version=$(dpkg -s "$package_name" 2>/dev/null | grep '^Version:' | cut -d' ' -f2)
       echo "Версия: $version"  # Дополнительно выводим версию пакета
        return 0  # пакет установлен
    else
        echo "Пакет '$package_name' не установлен в системе."
        echo "Начинаем установку"
        sudo apt install -y $package_name  # Подставляем имя пакета в установщик
        echo "Пакет '$package_name' установлен"
            #   return 1  # пакет не установлен

    fi
}

# Определение параметров в зависимости от версии Astra Linux. Подготовка к развёртыванию проекта
install_dependencies() {
    log "Установка системных зависимостей для Astra Linux $ASTRA_VERSION..."

    case "$ASTRA_VERSION" in
        "1.6")
            DB_PKG="postgresql-9.6 postgresql-contrib-9.6"   # Параметры для установки postgresql
            DJANGO_VERSION="1.10"                            # Версия стабильно работает с Python 3.5
             ;;
        "1.7")
            DB_PKG="postgresql-11 postgresql-contrib-11"  # Параметры для установки postgresql
            DJANGO_VERSION="1.11.17"                      #  Минимальная версия с которой может работать стабильно python 3.7
           ;;
    esac

    log "Подготовка Astra Linux $ASTRA_VERSION к развёртыванию Django-проекта"
    
    # Обновление списка пакетов
    sudo apt update
    log "Список пакетов обновлён"

    check_package_installed $GIT # Установка Git (Проверяем установлен или нет. Если нет устанавливаем)
    check_package_installed $DB_PKG # Проверяем установлен ли PostgreSQL нужной версии. Если нет устанавливаем
    check_package_installed $PYTHON_VENV  # Установка Python3-venv

}

# Клонирование репозитория (переносим проек на компьютер)
clone_repository() {
    log "Клонирование репозитория из $REPO_URL..."

    if [ -d "$PROJECT_DIR" ]; then            #   Проверяем существует ли папка проекта
        warn "Директория проекта $PROJECT_DIR уже существует. Выполняется git pull..."
        cd "$PROJECT_DIR"                     # Переходим в директорию проекта  PROJECT_DIR="/opt/List_Employ"
        git pull                              # извлекаем изменения из удалённого репозитория и объединяем их с текущей локальной веткой
    else                                      # Если папка проекта не найдена
      sudo mkdir -p "$PROJECT_DIR"            # Создаём папку проекта
      sudo chown $USER:$USER "$PROJECT_DIR"   # Назначаем текущего пользователя владельцем каталога
        cd "$PROJECT_DIR"                     # Переходим в созданную папку проекта
        git clone "$REPO_URL" .               # Клонируем целевой репозиторий 
    fi
    log "Репозиторий успешно клонирован в $PROJECT_DIR"

    # Настройка PostgreSQL
    log "Настройка базы данных и наполнение её данными "
    # Задаём пароль пользователю postgres
    log "Задаём пароль для пользователя postgres"
    # Сама по себе команда echo не меняет пароль в PostgreSQL. Для выполнения в БД эта комманда передаёт вывод echo в клиент psql через конвейер (|)
    echo "ALTER USER postgres WITH PASSWORD '$DB_PASS'" | sudo -u postgres psql -d postgres
       if [[ $? -eq 0 ]]; then # Проверяем была ли предыдущая команда успешно завершена (код 0)
          echo "Пароль успешно задан"
      else
          echo "Ошибка при создании пароля"
          exit 1    # Ошибка. Код возврата 1
      fi
    log "Пароль для пользователя postgres успешно задан"
    log "Создаём базу данных $DB_NAME"
    sudo -u "$DB_USER" psql -tAc "SELECT 1 FROM pg_database WHERE datname='$DB_NAME'" | grep -q 1 || sudo -u "$DB_USER" createdb -O "$DB_USER" "$DB_NAME"
    log "База данных $DB_NAME успешно создана"
    log "Начинаем заполнение базы данных данными"
    log "Поиск SQL‑скрипта '$SQL_SCRIPT_NAME'..."

    if [ -f "$SQL_SCRIPT_NAME" ]; then  # Проверяем доступен ли файл с sql-скриптом
        log "SQL‑скрипта '$SQL_SCRIPT_NAME' найден"
        log "Применение SQL‑скрипта к базе данных $DB_NAME..."
        sudo -u postgres psql -d "$DB_NAME" -f "$SQL_SCRIPT_NAME"
        log "SQL‑скрипт успешно применён. Данные успешно добавлены в базу данных "$DB_NAME""
    else
        warn "SQL‑скрипт '$SQL_SCRIPT_NAME' не найден. Пропускаем инициализацию БД."
    fi

   log "Предварительная подготовка системы завершена"
}

# Создание виртуального окружения и установка Python‑зависимостей
setup_python_env() {
    # Переходим к созданию виртуального окружения
    # Для того чтобы в будущем избежать проблем с правами будем создавать виртуальное окружение
    # внутри папки проекта
    cd "$PROJECT_DIR"  #
    log "Создаём виртуальное окружение"
    python3 -m venv venv       # Создаём виртуальное окружение 
    log "Виртуальное окружение создано"
    log "Активируем виртуальное окружение"
    source venv/bin/activate   # Активируем виртуальное окружение
    log "Виртуальное окружение активировано"
    log "Начинаем настройку виртуального окружения"

    # Установка Python
    log "Установка Python"
    sudo apt install -y $PYTHON  
    log "Python установлен"

    # Установка PIP
    log "Установка PIP-менеджера"
    sudo apt install -y $PYTHON_PIP 
    log "PIP-менеджер установлен"

   # Обновляем pip-менеджер 
    log "Обновление pip..."
    pip install --upgrade pip
    log "pip-менеджер обновлён"

    log "Установка дополнительных пакетов для установки psycopg2..."
    sudo apt install python3-dev libpq-dev build-essential
    log "Установка дополнительных пакетов завершена завершена."



    # Установка Django нужной версии (Та версия что находится в Requirement.txt нам не интересна. Игнорируем её)
    # Версия Django в Requirement.txt закоменчена. Ставим ту версию которую требует ТЗ в зависимости от версии Astra Linux
    log "Установка Django $DJANGO_VERSION..."
    pip install "Django==$DJANGO_VERSION"  # РАСКОМЕНТИТЬ
    log "Django $DJANGO_VERSION установлен"

    # Установка драйвера PostgreSQL (Содержится в Requirement.txt (закоменчен), установим 
    # другой вариант, чтобы избежать проблем совместимости в будущем)
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

    detect_astra_version    # Определение версии Astra Linux
    install_dependencies    # Определение параметров в зависимости от версии Astra Linux. Подготовка к развёртыванию проекта
    clone_repository        # Клонирование репозитория и наполнение базы данных данными
    setup_python_env        # Создание виртуального окружения и установка Python‑зависимостей
    run_django_setup        # Запуск миграций Django и сбор статических файлов

    log "Развёртывание завершено успешно!"
    log "Проект расположен в: $PROJECT_DIR"
    log "Для запуска сервера выполните:"
   
    log cd $PROJECT_DIR
    log source venv/bin/activate
    log python manage.py runserver

    cd $PROJECT_DIR
    source venv/bin/activate
    python manage.py runserver 

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
