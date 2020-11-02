from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),
    (2, 'Not to disclose')
) # 상수로 올려서 따로 뻄

class UserManager(BaseUserManager): #이메일로 로그인하기 위한 작업

    """
    _create_user : 클래스 내에서만 사용하겠다 명시
    create_user : 외부에서도 호출하면서 사용하겠다 명시
    """
    def _create_user(self, email, username, password, gender=0, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, username='', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must jave is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must jave is_superuser=True.')

        return self._create_user(email, '' ,password, **extra_fields)

class User(AbstractUser):
    # 이메일로 로그인, 중복성을 없애기 위해 unique=True 사용
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)

    username = models.CharField(max_length=30)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES) # SmallIntegerField : 성별 선택창

    objects = UserManager()
    USERNAME_FIELD = 'email' # 이메일로 로그인을 해야하니 email로 치안을 함
    REQUIRED_FIELDS = [] # 필수로 받고 싶은 필드를 넣기 원래 소스 코드엔 email필드가 들어가지만 우리는 로그인을 이메일로 하니깐

    def __str__(self):
        return "<%d %s>" % (self.pk, self.email)