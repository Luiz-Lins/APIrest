import argparse
import csv

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Importa os autores a partir de um csv'

    def add_arguments(self, parser):
        parser.add_arguments('csv', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        with options['csv'] as f:
            reader = csv.reader(f)
