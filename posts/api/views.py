from ..models import Post
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        super(PostCreateView, self).perform_create(serializer)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": self.request.data}
        return Response(response)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def retrieve(self, request, *args, **kwargs):
        super(PostDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': "Successfully retrieved",
                    'result': data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(PostDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': "Successfully updated",
                    'result': data}
        return Response(response)
    
    def delete(self, request, *args, **kwargs):
        super(PostDetailView, self).patch(request, args, kwargs)
        response = {'status_code': status.HTTP_200_OK,
                    'message': "Successfully updated"}
        return Response(response)