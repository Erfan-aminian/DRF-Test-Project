from rest_framework import serializers
from datetime import datetime, timedelta

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

class Comment(object):
    def __init__(self, email, content = None, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='amir.@gmail.com', content='too far')