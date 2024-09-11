import random

from locust import HttpUser, task, between, constant


class UserBehavior(HttpUser):
    host = "http://haproxy:8000"
    # время ожидания между задачами для каждого пользователя
    # wait_time = between(0.1, 0.2)
    wait_time = constant(1)

    def random_cyrillic_string(self, length):
        # генерируем случайную строку из кириллических символов
        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        return ''.join(random.choice(letters) for i in range(length))

    # @task(1)  # вес задачи, можно изменять для имитации различных сценариев
    # def search_users(self):
    #     last_name = self.random_cyrillic_string(random.randint(1, 2)).capitalize()
    #     first_name = self.random_cyrillic_string(random.randint(1, 2)).capitalize()
    #     self.client.get(f'/user/search/?last_name={last_name}&first_name={first_name}')

    @task(1)
    def health_check(self):
        self.client.get('/health/?just=checking')
