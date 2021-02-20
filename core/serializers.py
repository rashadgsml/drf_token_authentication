from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source="owner.username")
    class Meta:
        model = Post
        fields = (
            'id','owner','title','description'
        )
        