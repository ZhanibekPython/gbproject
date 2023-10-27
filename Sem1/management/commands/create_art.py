from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates new article'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('body', type=str)
        parser.add_argument('author_name', type=str)
        parser.add_argument('author_surname', type=str)

    def handle(self, *args, **options):
        model1 = apps.get_model('Sem1', 'Article')
        model2 = apps.get_model('Sem1', 'Author')
        name = options.get('name')
        body = options.get('body')
        author_name = options.get('author_name')
        author_surname = options.get('author_surname')
        author = model2(name=author_name, surname=author_surname)
        author.save()
        article = model1(name=name, body=body, author=author)
        article.save()
        self.stdout.write(f'{article}')

    # def add_arguments(self, parser):
    #     parser.add_argument('--create', action='store_true', help='Создать новый объект')
    #     parser.add_argument('--read', action='store_true', help='Прочитать все объекты')
    #     parser.add_argument('--update', type=int, help='Обновить объект по идентификатору')
    #     parser.add_argument('--delete', type=int, help='Удалить объект по идентификатору')
    #
    # def handle(self, *args, **options):
    #     if options['create']:
    #         new_object = Article.objects.create(name='Новый объект', description='Описание нового объекта')
    #         self.stdout.write(self.style.SUCCESS(f'Создан новый объект: {new_object}'))
    #
    #     if options['read']:
    #         all_objects = Article.objects.all()
    #         for obj in all_objects:
    #             self.stdout.write(self.style.SUCCESS(f'{obj}'))
    #
    #     if options['update']:
    #         obj_id = options['update']
    #         try:
    #             obj = Article.objects.get(id=obj_id)
    #             obj.name = 'Обновленный объект'
    #             obj.save()
    #             self.stdout.write(self.style.SUCCESS(f'Обновлен объект: {obj}'))
    #         except Article.DoesNotExist:
    #             self.stdout.write(self.style.ERROR(f'Объект с идентификатором {obj_id} не найден'))
    #
    #     if options['delete']:
    #         obj_id = options['delete']
    #         try:
    #             obj = Article.objects.get(id=obj_id)
    #             obj.delete()
    #             self.stdout.write(self.style.SUCCESS(f'Удален объект с идентификатором {obj_id}'))
    #         except Article.DoesNotExist:
    #             self.stdout.write(self.style.ERROR(f'Объект с идентификатором {obj_id} не найден'))
