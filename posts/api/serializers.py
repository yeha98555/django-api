from ..models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Post
        fields = ('title', 'content', 'is_featured', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')