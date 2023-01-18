from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability','secondary_ability', 'catch_phrase', 'super_type', 'type_id']
        depth = 1
        
    type_id = serializers.IntegerField(write_only=True)