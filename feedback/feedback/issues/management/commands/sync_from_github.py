from django.core.management.base import BaseCommand

from feedback.issues.utils.gh import sync_from_github


class Command(BaseCommand):
    help = 'Close issues which have been closed on Github'

    def handle(self, *args, **options):
        sync_from_github()
