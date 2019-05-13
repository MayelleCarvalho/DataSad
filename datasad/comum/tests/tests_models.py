# coding=utf-8
import unittest
from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from datasad.comum.models import Perfil


# class TestUser(TestCase):
#
#     def setUp(self):
#         self.user = mommy.make(User, password = 'abcd1234', is_superuser = 'False', username = 'teste', first_name = 'Teste',last_name =  'User', email = 'teste@gmail.com', is_staff = 'True', is_active= 'True',date_joined = datetime.now())
#
#     def test_user_creation(self):
#         self.assertTrue(isinstance(self.user, User))
#         # self.assertEquals(self.user.__str__(), self.user.username)
#
#
class TestPerfil(TestCase):

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.perfil = mommy.make(Perfil, sexo='F', contato ='99 9999-9999', usuario=self.user, cpf='123.456.789-09')

    def test_perfil_creation(self):
        self.assertTrue(isinstance(self.perfil, Perfil))
        # self.assertEquals(self.perfil.__str__(), self.perfil.nome())
