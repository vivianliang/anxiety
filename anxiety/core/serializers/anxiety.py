from rest_framework import serializers

class AnxietySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField(source='anxiety.user.id')
    fear = serializers.CharField()
    action = serializers.CharField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
