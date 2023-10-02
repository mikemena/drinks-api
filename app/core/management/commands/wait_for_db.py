"""
Django command to wait for the database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write(self.style.WARNING("Waiting for database..."))
        start_time = time.time()
        timeout = 60  # so it doesn't try indefinitely if there's a persistent issue with the database connection
        wait_time = 1
        db_up = False
        while db_up is False and time.time() - start_time < timeout:
            try:
                self.check()
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write(
                    self.style.ERROR("db unavailable, waiting 1 second...")
                )

                time.sleep(wait_time)
                wait_time = min(
                    wait_time * 2, 30
                )  # Double the wait time, but cap at 30 seconds

        self.stdout.write(self.style.SUCCESS("db available!"))
