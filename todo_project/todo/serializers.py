from rest_framework import serializers
from .models import TodoItem, Tag

class TagSerializer(serializers.ModelSerializer):
    """
    Serializer to represent the Tag model in JSON format
    """
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TodoItemSerializer(serializers.ModelSerializer):
    """
    Serializer to represent the TodoItem model in JSON format
    """
    tags = TagSerializer(many=True, read_only=False, required=False)
    class Meta:
        model = TodoItem
        fields = ['id', 'created_at','title', 'description', 'due_date', 'tags', 'status']
        read_only_fields = ['created_at']

    def create(self, instance, validated_data):
        """
        Override create method to handle tags
        """
        tags_data = validated_data.pop('tags', None)
        todo_entry = TodoItem.objects.create(**validated_data)

        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            todo_entry.tags.add(tag)
        
        return todo_entry
    
    def update(self, instance, validated_data):
        """
        Override update method to handle tags
        """
        tags_data = validated_data.pop('tags', None)
        instance = super().update(instance, validated_data)

        if tags_data:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(name=tag_data['name'])
                instance.tags.add(tag)
        
        return instance
    
