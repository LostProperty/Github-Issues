from django.core.management.base import BaseCommand

from feedback.issues.utils.gh import sync_to_github


class Command(BaseCommand):
    help = 'Add new accepted issues to Github'

    def handle(self, *args, **options):
        sync_to_github()
