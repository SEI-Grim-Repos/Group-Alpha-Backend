from rest_framework import serializers
    
from .models import Post, User_Account, Comment

class User_AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Account
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.BaseSerializer):
  def to_representation(self,instance):
    return {
      "id": instance.id,
      "body": instance.body,
      "user": instance.user.username,
      "location": instance.location,
      "date": instance.date,
      "title": instance.title,
      "image": instance.image,
      "likes": instance.likes,
    }
    
class CommentSerializer(serializers.BaseSerializer):
    def to_representation(self,instance):
      return {
      "id":instance.id,
      "body": instance.body,
      "user": instance.user.username,
    }