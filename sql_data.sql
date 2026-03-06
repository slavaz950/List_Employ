
-- Задаём пароль для пользователя postgres
ALTER USER postgres WITH PASSWORD 'Cen78Ter19';


-- СОЗДАНИЕ БАЗЫ ДАННЫХ И ЕЁ СТРУКТУРЫ

-- Если в кластере PostgreSQL уже существует БД ListEmpDB, то удаляем её
--DROP DATABASE IF EXISTS "ListEmpDB";
--COMMIT;

-- Создаём БД ListEmpDB используя «чистый» шаблон template0, гарантируя отсутствие лишних объектов
--CREATE DATABASE "ListEmpDB" WITH TEMPLATE = template0 ENCODING = 'UTF8';
--COMMIT;



-- Создаём базу данных ListEmpDB, владельцем которой сразу становится postgres
CREATE DATABASE "ListEmpDB";
   -- OWNER = postgres
  --  ENCODING = 'UTF8'
  --  LC_COLLATE = 'en_US.UTF-8'
  --  LC_CTYPE = 'en_US.UTF-8'
  --  TEMPLATE = template0;

-- Предоставляем все привилегии на базу данных ListEmpDB пользователю postgres
GRANT ALL PRIVILEGES ON DATABASE "ListEmpDB" TO postgres;


-- Даём права пользователю postgres (как владеделец)
--ALTER DATABASE "ListEmpDB" OWNER TO postgres;
--COMMIT;


-- Подключаемся к БД ListEmpDB  
--\connect "ListEmpDB"


-- СОЗДАЁМ ВСЕ НЕОБХОДИМЫЕ ТАБЛИЦЫ

/* =========================================================================== */
-- СОЗДАНИЕ ТАБЛИЦЫ category (таблица-справочник)
CREATE TABLE public.category (
    id bigint NOT NULL,  -- Первичный ключ (не NULL. Обязательное поле)
    name_category character varying(20) NOT NULL, -- Наименование категории (не NULL. Не более 20 символов)
    CONSTRAINT category_pkey PRIMARY KEY (id)  -- Ограничение (Первичный ключ)
);

-- Даём права пользователю postgres как владельцу на таблицу category (Категории)
ALTER TABLE public.category OWNER TO postgres;


/* =========================================================================== */
-- СОЗДАНИЕ ТАБЛИЦЫ gender (таблица-справочник)
CREATE TABLE public.gender (
    id bigint NOT NULL,                         --  Первичный ключ (не NULL. Обязательное поле)
    name_gender character varying(8) NOT NULL,   -- Наименование пола (не NULL. Не более 8 символов)
	CONSTRAINT gender_pkey PRIMARY KEY (id)
);

-- Даём права пользователю postgres как владельцу на таблицу gender (Пол)
ALTER TABLE public.gender OWNER TO postgres;


/* =========================================================================== */
-- СОЗДАНИЕ ТАБЛИЦЫ positions (таблица-справочник)
CREATE TABLE public.positions (
    id bigint NOT NULL,                   --  Первичный ключ (не NULL. Обязательное поле)
    name_position character varying(40),  -- Наименование должности (не NULL. Не более 40 символов)
    id_category bigint,                   -- Идентификатор "Категория" (Целое число)
	CONSTRAINT positions_pkey PRIMARY KEY (id),  -- Первичный ключ
	CONSTRAINT name_position UNIQUE (name_position), -- Уникальное значение поля "Наименование должности"
	CONSTRAINT positions_id_category_fkey FOREIGN KEY (id_category) REFERENCES public.category(id) -- Внешний ключ таблица "Категории"
);

-- Даём права пользователю postgres как владельцу на таблицу positions (Должность)
ALTER TABLE public.positions OWNER TO postgres;


/* =========================================================================== */
-- СОЗДАНИЕ ТАБЛИЦЫ employ (таблица использующая данные таблиц справочников)
CREATE TABLE public.employ (
    id bigint NOT NULL,           --  Первичный ключ (не NULL. Обязательное поле)
    "FIO" character varying(35),  -- Наименование категории (не NULL. Не более 35 символов)
    age integer,                  -- Поле "Возраст". Целочисленное значение
    id_positions bigint,         -- Идентификатор "Должность" (Целое число)
    id_category bigint,          -- Идентификатор "Категория" (Целое число)
    id_gender bigint,             -- Идентификатор "Пол"
	CONSTRAINT employ_pkey PRIMARY KEY (id),  -- Первичный ключ
	CONSTRAINT "employ_FIO_age_key" UNIQUE ("FIO", age), -- уникальные значения полей "Ф.И.О" и "Возраст")
	CONSTRAINT fk_employ_category FOREIGN KEY (id_category) REFERENCES public.category(id),  -- Внешний ключ таблица "Категории"
	CONSTRAINT fk_employ_positions FOREIGN KEY (id_positions) REFERENCES public.positions(id) -- Внешний ключ таблица "Должности"
);

-- Даём права пользователю postgres как владельцу на таблицу employ (Сотрудники)
ALTER TABLE public.employ OWNER TO postgres;


/* =========================================================================== */
/* =========================================================================== */
-- СОЗДАНИЕ ПОСЛЕДОВАТЕЛЬНОСТЕЙ
/* Для генерации уникальных числовых значений для идентификаторов таблиц category, positions, employ
создаём последовательности category_id_seq, positions_id_seq, category_id_seq. Будем использовать 
их для заполнения первичных ключей в этих таблицах
 */
 
 ---------------------------------------------------------------------------------------------
-- Создаём последовательность category_id_seq для таблицы category
CREATE SEQUENCE public.category_id_seq
   -- AS bigint      -- Тип данных последовательности
    START WITH 1    -- начальное значение последовательности (первое число = 1)
    INCREMENT BY 1  -- шаг приращения (каждое следующее число будет на 1 больше предыдущего)
    NO MINVALUE     -- Отключение ограничения минимального значения
    NO MAXVALUE     -- Отключение ограничения максимального значения
    CACHE 1;        -- количество предварительно выделенных значений, хранящихся в памяти
	/* значение 1 означает отсутствие кэширования: каждое новое значение 
	генерируется индивидуально*/

-- Даём права пользователю postgres как владельцу на последовательность category_id_seq
ALTER SEQUENCE public.category_id_seq OWNER TO postgres;


---------------------------------------------------------------------------------------------
-- Создаём последовательность positions_id_seq для таблицы positions
CREATE SEQUENCE public.positions_id_seq
   -- AS bigint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

-- Даём права пользователю postgres как владельцу на последовательность positions_id_seq
ALTER SEQUENCE public.positions_id_seq OWNER TO postgres;

-----------------------------------------------------------------------------------------------
-- Создаём последовательность employ_id_seq для таблицы employ
CREATE SEQUENCE public.employ_id_seq
   -- AS bigint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

-- Даём права пользователю postgres как владельцу на последовательность employ_id_seq
ALTER SEQUENCE public.employ_id_seq OWNER TO postgres;


/* =========================================================================== */
-- НАСТРАИВАЕМ СВЯЗИ ПОСЛЕДОВАТЕЛЬНОСТЕЙ СО СТОЛБЦАМИ id СООТВЕТСТВУЮЩИХ ТАБЛИЦ

-- Связываем последовательность category_id_seq со столбцом id таблицы category 
ALTER SEQUENCE public.category_id_seq OWNED BY public.category.id;

-- Связываем последовательность positions_id_seq со столбцом id таблицы positions
ALTER SEQUENCE public.positions_id_seq OWNED BY public.positions.id;


-- Связываем последовательность employ_id_seq со столбцом id таблицы employ
ALTER SEQUENCE public.employ_id_seq OWNED BY public.employ.id;




/* =========================================================================== */
-- УСТАНАВЛИВАЕМ ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ ДЛЯ СТОЛБЦОВ id ЧЕРЕЗ nextval() ДЛЯ СООТВЕТСТВУЮЩИХ ТАБЛИЦ
/* Для того чтобы при вставке новых строк без указания значения id PostgreSQL будет 
автоматически получать следующее значение из последовательности public.category_id_seq 
с помощью функции nextval().*/

-- Устанавливаем значение по умолчанию для столбца id таблицы category.
ALTER TABLE ONLY public.category ALTER COLUMN id SET DEFAULT nextval('public.category_id_seq'::regclass);

-- Устанавливаем значение по умолчанию для столбца id таблицы positions.
ALTER TABLE ONLY public.positions ALTER COLUMN id SET DEFAULT nextval('public.positions_id_seq'::regclass);

-- Устанавливаем значение по умолчанию для столбца id таблицы employ.
ALTER TABLE ONLY public.employ ALTER COLUMN id SET DEFAULT nextval('public.employ_id_seq'::regclass);



/* =========================================================================== */
-- ЗАПОЛНЕНИЕ СПРАВОЧНЫХ ТАБЛИЦЫ

-- Добавление данных в таблицу category
INSERT INTO public.category (id, name_category) 
VALUES 
 (1, 'Руководитель'),
 (2, 'Специалист'),
 (3, 'Служащий'),
 (4, 'Рабочий');

-- Добавление данных в таблицу gender
INSERT INTO public.gender (id, name_gender) 
VALUES 
 (1, 'Мужской'),
 (2, 'Женский');


-- Добавление данных в таблицу positions
INSERT INTO public.positions (id, name_position, id_category) 
VALUES 
 (1, 'Директор', 1),
 (2, 'Главный бухгалтер', 1),
 (3, 'Главный диспетчер', 1),
 (6, 'Инженер по качеству', 2),
 (7, 'Инженер-технолог', 2),
 (8, 'Инженер-электронник', 2),
 (9, 'Инженер-программист', 2),
 (10, 'Секретарь', 3),
 (11, 'Консультант', 3),
 (12, 'Токарь', 4),
 (13, 'Фрезеровщик', 4),
 (14, 'Плотник', 4),
 (15, 'Каменщик', 4),
 (16, 'Грузчик', 4),
 (141, 'Кладовщик', 4),
 (142, 'Главный инженер', 1),
 (143, 'Сварщик', 4),
 (144, 'Штамповщик', 4),
 (145, 'Монтажник', 4),
 (146, 'Сверловщик', 4),
 (147, 'Специалист по ТБ и ОТ', 2),
 (149, 'Специалист ОТИЗ', 2),
 (150, 'Водитель', 4),
 (151, 'Слесарь', 4),
 (155, 'Дежурный', 3),
 (156, 'Архивариус', 3),
 (157, 'Комендант', 3),
 (5, 'Инженер-лаборант', 2),
 (4, 'Инженер-конструктор', 2),
 (134, 'Инженер-эколог', 2),
 (135, 'Шлифовщик', 4);


-- Добавление данных в таблицу employ

INSERT INTO public.employ (id, "FIO", age, id_positions, id_category, id_gender) 
VALUES 
 (233, 'Булгаков А.С.', 47, 7, 2, 1),
 (106, 'Павлов Р.В.', 37, 14, 4, 1),
 (234, 'Круглова С.И.', 34, 5, 2, 2),
 (236, 'Козлова М.Н.', 32, 10, 3, 2),
 (237, 'Рябов К.Р.', 63, 135, 4, 1),
 (3, 'Карпова А.П.', 48, 6, 2, 2),
 (6, 'Дубовик А.Л.', 59, 13, 4, 1),
 (2, 'Смирнов О.Р.', 24, 12, 4, 1),
 (238, 'Шарапов А.Н.', 25, 14, 4, 1),
 (239, 'Лаврова Г.П.', 48, 134, 2, 2),
 (5, 'Меньшова О.Т.', 54, 2, 1, 2),
 (240, 'Харина С.А.', 47, 1, 1, 2),
 (241, 'Должина Р.А.', 52, 3, 1, 2),
 (65, 'Краснов А.А.', 34, 13, 4, 1),
 (7, 'Никольский В.В.', 47, 4, 2, 1),
 (242, 'Корнилов А.С.', 34, 142, 1, 1),
 (243, 'Свиридова И.С.', 34, 9, 2, 2),
 (105, 'Ползунова А.П.', 46, 6, 2, 2),
 (19, 'Рукавишников Н.Р.', 63, 15, 4, 1),
 (1, 'Иванов П.И.', 34, 8, 2, 1),
 (15, 'Стуков А.А.', 24, 12, 4, 1),
 (37, 'Аверин П.Р.', 45, 12, 4, 1),
 (72, 'Сухоруков А.А.', 23, 13, 4, 1),
 (4, 'Анисимова Н.Н.', 29, 10, 3, 2),
 (146, 'Панков М.Р.', 24, 5, 2, 1),
 (88, 'Моргунова Е.П.', 44, 5, 2, 2),
 (57, 'Усачёва О.Е.', 25, 7, 2, 2),
 (58, 'Кузнецова С.П.', 64, 10, 3, 2),
 (59, 'Клещёв С.П.', 34, 16, 4, 1),
 (64, 'Баталов А.А.', 56, 15, 4, 1),
 (97, 'Хомяков А.Р.', 56, 13, 4, 1),
 (99, 'Кутузов А.А.', 44, 12, 4, 1),
 (100, 'Сурков С.С.', 55, 4, 2, 1);



/* =========================================================================== */
-- УСТАНОВКА ТЕКУЩИХ ЗНАЧЕНИЙ ПОСЛЕДОВАТЕЛЬНОСТЕЙ ЧЕРЕЗ setval().


-- Установка текущего значения последовательности category_id_seq
SELECT pg_catalog.setval('public.category_id_seq', 4, true);

-- Установка текущего значения последовательности positions_id_seq
SELECT pg_catalog.setval('public.positions_id_seq', 157, true);

-- Установка текущего значения последовательности employ_id_seq
SELECT pg_catalog.setval('public.employ_id_seq', 243, true);


