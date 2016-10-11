from django.db.models import Q

from rest_framework.filters import(
		SearchFilter,
		OrderingFilter,
	)
from rest_framework.generics import(
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	DestroyAPIView,
	RetrieveUpdateAPIView
	)
from rest_framework.pagination import(
	LimitOffsetPagination,
	PageNumberPagination,
	)
from rest_framework.permissions import(
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)
from posts.models import Post

from .pagination import (
	PostLimitOffsetPagination,
	PostPageNumberPagination
	)
from .permissions import IsOwnerOrReadOnly

from .serializers import (
	PostDetailSerializer,
	PostListSerializer,
	PostCreateSerializer
	)


class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class=PostCreateSerializer
	permission_classes=[IsAuthenticated]
	def perform_create(self,serializer):
		serializer.save(user=self.request.user)
	#def get_queryset():

class PostListAPIView(ListAPIView):
	serializer_class=PostListSerializer
	filter_backends=[SearchFilter,OrderingFilter]
	search_fields=['title','content','user__first_name']
	pagination_class=PostLimitOffsetPagination
	def get_queryset(self,*args,**kwargs):
		queryset_list=Post.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
					Q(title__icontains=query)|
					Q(content__icontains=query)|
					Q(user__first_name__icontains=query) |
					Q(user__last_name__icontains=query)
					).distinct()
		return queryset_list

class PostDetailAPIView(RetrieveAPIView):
	queryset=Post.objects.all()
	serializer_class=PostDetailSerializer
	lookup_field='slug'

class PostDeleteAPIView(DestroyAPIView):
	queryset=Post.objects.all()
	serializer_class=PostDetailSerializer
	lookup_field='slug'
	permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset=Post.objects.all()
	serializer_class=PostDetailSerializer
	lookup_field='slug'
	permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

	def perform_updated(self,serializer):
		serializer.save(user=self.request.user)