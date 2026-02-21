
# ЗАПРОСЫ ДЛЯ СОТРУДНИКОВ

# Запрос для вывода списка сотрудников
sql_employ_list ='\
          SELECT\
            e.id,\
            e."FIO",\
            e.id_gender,\
            g.name_gender,\
            e.age,\
            e.id_positions,\
            p.name_position,\
            e.id_category,\
            c.name_category\
              FROM employ e\
                  INNER JOIN positions  p ON p.id = e.id_positions \
                  INNER JOIN category  c ON c.id = e.id_category \
                  INNER JOIN gender  g ON g.id = e.id_gender ORDER BY e.id'
       


# SQL-запрос "Карточка сотрудника" 
sql_employ_detail = 'SELECT * FROM employ WHERE id = %s'


# Запрос для добавления нового сотрудника
sql_employ_insert ='\
           INSERT INTO employ \
           ("FIO",age,id_positions,id_category,id_gender) \
            VALUES (%s,%s,%s,%s,%s)'


# Запрос на изменение карточки сотрудника
sql_employ_update ='\
            UPDATE employ \
              SET "FIO" = %s, \
                   age = %s, \
                   id_gender = %s \
                     WHERE id = %s'
  
# Запрос на удаление сотрудника
sql_employ_delete ='DELETE FROM employ WHERE id= %s'
 


#   ЗАПРОСЫ ДЛЯ ДОЛЖНОСТЕЙ


# Выводим все должности без ограничений  id, name_position
sql_positions = 'SELECT * FROM positions '

# Выводим все должности относящиеся к той или иной категории id, name_position
# sql_position_list = 'SELECT * FROM positions where id_category = %s ORDER BY id ASC'


sql_position_list ='\
                     SELECT \
                         p.id, \
                         p.name_position,\
                         p.id_category, \
                         c.name_category  \
                              FROM positions p  \
                                    INNER JOIN category c ON c.id = p.id_category  \
                                          where id_category = %s ORDER BY id ASC'



# Детализация должностей
sql_position_detail = 'SELECT * FROM positions WHERE id = %s'

# Добавление должности
sql_position_insert = 'INSERT INTO positions (name_position,id_category) VALUES (%s,%s)'


# Изменение должности   
sql_position_update = ' \
                UPDATE positions  \
                  SET name_position = %s,  \
                      id_category = %s  \
                         WHERE id = %s'


# Удаление должности
sql_position_delete = 'DELETE FROM positions WHERE id=%s'

# Список категорий
sql_category_list ='SELECT id,name_category FROM category ORDER BY id ASC'


# Считаем количество Сотрудников принятых на определённую должность (проверка перед удалением)
sql_count_employ_by_position ='SELECT count(*) result FROM employ WHERE id_positions=%s'