from rest_framework import serializers
from .models import Article, Advertisement, Category, Comment, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'is_journalist']

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = fields = ['id', 'title', 'image', 'url', 'start_date', 'end_date', 'is_active']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = CustomUserSerializer()
    image = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ['id','category','title', 'author', 'content', 'image', 'created_at']
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None


class CommentSerializer(serializers.ModelSerializer):
    user = CategorySerializer()
    class Meta:
        model = Comment
        fields = ['id', 'article', 'user', 'content', 'created_at']