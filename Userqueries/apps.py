from django.apps import AppConfig


class UserqueriesConfig(AppConfig):
    name = 'Userqueries'
    
    def ready(self):
        import Userqueries.signals