from django.core.management.base import CommandError, BaseCommand
from News.models import Post, Category

class Command(BaseCommand, CommandError):
    help = 'Команда удаляет все статьи указанной категори'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    missing_args_message = 'Не указана категория!'
    requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        parser.add_argument('cat', help='имя категории')

    def handle(self, *args, **kwargs):
        cat = kwargs['cat']
        try:
            category = Category.objects.get(name_category=cat)
            self.stdout.write(f'Do you really want to delete all posts in category "{cat}"? yes/no')
            answer = input()
            if answer == 'yes':
                posts_cat = category.post_set.all()
                posts_cat.delete()
                self.stdout.write(self.style.SUCCESS('Succesfully wiped posts!'))
                return
            else:
                self.stdout.write(self.style.ERROR('Access denied'))
        except Category.DoesNotExist:
            self.stdout.write(f'Category "{cat}" does not exist')


