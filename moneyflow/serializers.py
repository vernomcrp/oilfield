from django.forms import widgets
from rest_framework import serializers
from moneyflow.models import MoneyFlowRecord, TASK_TYPE

class MoneyFlowSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=100)
    task_type = serializers.ChoiceField(choices=TASK_TYPE)
    
    def create(self, validated_data):
        return MoneyFlowRecord.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.task_type = validated_data.get('task_type', instance.task_type)
        instance.save()
        return instance