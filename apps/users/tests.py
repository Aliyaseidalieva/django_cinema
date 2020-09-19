# from rest_framework.test import APITestCase
# from django.urls import reverse


# class userProfileTestCase(APITestCase):
#     profile_list_url=reverse('all-profiles')
#     def setUp(self):
#         # создаем нового пользователя, отправляющего запрос на конечную точку djoser
#         self.user=self.client.post('/auth/users/',data={'username':'aliya','password':'326022aa'})
#         # получаем токен json для вновь созданного пользователя
#         response=self.client.post('api/auth/jwt/create/',data={'username':'aliya','password':'326022aa'})
#         self.token=response.data['access']
#         self.api_authentication()

#     def api_authentication(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)

#     # получить список всех профилей пользователей, пока пользователь запроса аутентифицирован
#     def test_userprofile_list_authenticated(self):
#         response=self.client.get(self.profile_list_url)
#         self.assertEqual(response.status_code,status.HTTP_200_OK)

#     # получить список всех профилей пользователей, пока пользователь запроса не прошел аутентификацию
#     def test_userprofile_list_unauthenticated(self):
#         self.client.force_authenticate(user=None)
#         response=self.client.get(self.profile_list_url)
#         self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

#     # проверка, чтобы получить данные профиля аутентифицированного пользователя
#     def test_userprofile_detail_retrieve(self):
#         response=self.client.get(reverse('profile',kwargs={'pk':1}))
#         print(response.data)
#         self.assertEqual(response.status_code,status.HTTP_200_OK)


#     # заполняем профиль пользователя, который был автоматически создан с помощью сигналов
#     def test_userprofile_profile(self):
#         profile_data={'description':'Very cool people','is_staff':'true',}
#         response=self.client.put(reverse('profile',kwargs={'pk':1}),data=profile_data)
#         print(response.data)
#         self.assertEqual(response.status_code,status.HTTP_200_OK)