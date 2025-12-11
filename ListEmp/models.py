
#Это автоматически сгенерированный модуль модели Django.

# Вам придется вручную сделать следующее, чтобы это очистить:

# * Измените порядок моделей

# * Убедитесь, что в каждой модели есть одно поле с primary_key=True

# * Убедитесь, что для каждого ForeignKey и OneToOneField `on_delete` задано желаемое поведение

# * Удалите строки `managed = False`, если вы хотите разрешить Django создавать, 
# изменять и удалять таблицу

# Можете свободно переименовывать модели, но не переименовывайте значения db_table 
# или имена полей.


from django.db import models


# ВСТАВИТЬ КОММЕНТЫ


class Employ(models.Model):
    id = models.BigAutoField(primary_key=True)
    fio = models.CharField(db_column='FIO', max_length=35, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(blank=True, null=True)
    positions = models.ForeignKey('Positions', models.DO_NOTHING, db_column='id_positions', blank=True, null=True)
    category: str = models.ForeignKey('Category', models.DO_NOTHING, db_column='id_category', blank=True, null=True)
    gender: str = models.ForeignKey('Gender', models.DO_NOTHING, db_column='id_gender', blank=True, null=True)
    
    '''
    id_positions = models.ForeignKey('Positions', models.DO_NOTHING, db_column='id_positions', blank=True, null=True)
    id_category = models.ForeignKey('Category', models.DO_NOTHING, db_column='id_category', blank=True, null=True)
    id_gender = models.ForeignKey('Gender', models.DO_NOTHING, db_column='id_gender', blank=True, null=True)
    '''
    
    
    
    class Meta:
        managed = False
        db_table = 'employ'
       
    '''
    def __str__(self) -> str:
        return self.positions
    '''     


class Positions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_position = models.CharField(max_length=40, blank=True, null=True)
    category = models.ForeignKey('Category', models.DO_NOTHING, db_column='id_category', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'positions'

    def __str__(self) -> str:
        return self.name_position

class Gender(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_gender = models.CharField(max_length=40, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'gender'
        
    def __str__(self) -> str:
        return self.name_gender
 
        
class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_category = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category' 
        
    def __str__(self) -> str:
        return self.name_category       











class ListempCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_category = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ListEmp_category'

'''
class ListempEmployees(models.Model):
    id = models.BigAutoField(primary_key=True)
    fio = models.CharField(db_column='FIO', max_length=35)  # Field name made lowercase.
    gender = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'ListEmp_employees'
'''       
        


class ListempPositions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_positions = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'ListEmp_positions'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)





class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

