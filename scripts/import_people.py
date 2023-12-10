import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
django.setup()

from users.models import User


def run_script():
    prepared_users = []
    with open('people.csv', encoding='UTF-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            try:
                full_name, wtf, city = line.split(',')
                first_name, last_name = full_name.split(' ')
                prepared_users.append(User(**{
                    'first_name': first_name,
                    'last_name': last_name,
                    'city': city,
                    'username': User.generate_username()
                }))
                if len(prepared_users) % 100 == 0:
                    print(f'{len(prepared_users)} prepared for creation...')
            except Exception as e:
                print(f'Error parsing user by line "{line}": {e}')

    for i in range(0, len(prepared_users), 1000):
        stop = i + 1000
        print(f'Creating {i} to {stop} users...')
        created = User.objects.bulk_create(prepared_users[i:stop])
        print(f'Created: {created}')

    print(f'Created {len(prepared_users)} users totally')


if __name__ == '__main__':
    run_script()
