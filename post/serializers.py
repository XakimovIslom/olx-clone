from rest_framework import serializers

from option.models import PostOption
from option.serializers import OptionSerializer, PostOptionValueSerializer
from post.models import Category, Post, District, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('title',)


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('title', 'image', 'order', 'subcategory')


class DistrictSerializer(serializers.ModelSerializer):
    region = serializers.StringRelatedField(source='region.title')

    class Meta:
        model = District
        fields = ('title', 'region')


class MainPostsSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()

    class Meta:
        model = Post
        fields = ('title', 'main_photo', 'price', 'district', 'created_at')


class PostDetailSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(source="district.title")
    options = serializers.StringRelatedField(source="json.options", read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'price', 'district', 'options', 'main_photo', 'content', 'views_count')


