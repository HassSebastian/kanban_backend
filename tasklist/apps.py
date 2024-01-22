from django.apps import AppConfig


class TasklistConfig(AppConfig):
    """
    AppConfig class for the Tasklist app.

    Attributes:
    - `default_auto_field` (str): The default auto field for model definitions.
    - `name` (str): The name of the app ('tasklist').

    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "tasklist"
