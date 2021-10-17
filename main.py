import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001

    passcards = Passcard.objects.all()
    print(passcards)

    person42: Passcard = passcards[41]
    person_info = '''owner_name: {0}
passcode: {1}
created_at: {2}
is_active: {3}'''
    print(person_info.format(person42.owner_name, person42.passcode, person42.created_at, person42.is_active))

    active_passcards = Passcard.objects.filter(is_active=True)
    print(f'Всего пропусков {len(passcards)}')
    print(f'Активных пропусков {len(active_passcards)}')
