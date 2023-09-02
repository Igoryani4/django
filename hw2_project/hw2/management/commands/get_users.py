from django.core.management.base import BaseCommand
from hw2.models import User


class Command(BaseCommand):
    help = "Get user by id."
    
    
    def add_arguments(self, parser):
        # parser.add_argument('id', type=int, help='User ID')
        parser.add_argument('pk', type=int, help='User ID')
    
    
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
        # id = kwargs['id']
        # user = User.objects.get(id=id)
        # self.stdout.write(f'{user}')


# if __name__ == '__main__':
#     Command.run_from_argv()