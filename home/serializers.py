from rest_framework import serializers
from .models import Question, Answer
from .custom_related_fields import UserEmailRelatedField


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    # user = serializers.StringRelatedField(read_only=True)
    user = UserEmailRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = "__all__"

    def get_answers(self, obj):
        result = obj.qanswer.all()
        return AnswerSerializer(instance=result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="email")

    class Meta:
        model = Answer
        fields = "__all__"
