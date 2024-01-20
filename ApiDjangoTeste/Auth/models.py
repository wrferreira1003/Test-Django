from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # AbstractUser já tem campos como username, email, password, etc.
    type = models.CharField(max_length=100, help_text="Tipo de usuário")

    # Configura email como identificador principal e único
    email = models.EmailField(unique=True)
    # Configurar email como identificador principal
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # 'email' é obrigatório por padrão e não deve ser listado aqui

    # Sobrescrever o método save para garantir que o email é único
    def save(self, *args, **kwargs):
        self.email = self.email.lower()  # Converter email para lowercase para evitar duplicatas
        return super(User, self).save(*args, **kwargs)


