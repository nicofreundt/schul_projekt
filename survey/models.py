from django.db.models import (
    CharField,
    TextField,
    IntegerField,
    BooleanField,
    ForeignKey,
    UUIDField,
    Model,
    CASCADE,
)
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from uuid import uuid4

# GLOBALS #
user_model = get_user_model()

# MODELS #
class Survey(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    title = CharField(max_length=100)
    description = TextField()
    creator = ForeignKey(user_model, on_delete=CASCADE)
    closed = BooleanField(default=True)

    def __str__(self):
        return (
            self.title
            + " | "
            + self.description
            + " | "
            + self.creator.username
            + " | "
            + str(self.closed)
        )


class Question(Model):
    survey = ForeignKey(Survey, on_delete=CASCADE)
    position = IntegerField(validators=[MinValueValidator(1)])
    text = TextField()


class Answer(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    rating = IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
