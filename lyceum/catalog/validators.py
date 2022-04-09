from django.forms import ValidationError


def validate_brilliant(value):
    must_words = ("Превосходно", "Роскошно")
    if (
        not any([word.lower() in value.lower() for word in must_words])
        or len(value.strip().split()) < 2
    ):
        raise ValidationError(
            f"Обязательно используйте слова {' или '.join(must_words)}"
        )
