from rest_framework import filters
from rest_framework import generics


from post.models import Category, Post
from post.serializers import CategorySerializer, MainPostsSerializer, PostDetailSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MainPostAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(plan__code="TOP").order_by('?')
    serializer_class = MainPostsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'district__title']


class PostDetailRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.views_count += 1
    #     instance.save()
    #     return super().retrieve(request, *args, **kwargs)

    def views_up(request, pk):
        obj = Post.objects.get(id=pk)
        obj.views += 1
        obj.save()
        return super().views_up(request, *args, **kwargs)