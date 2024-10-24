# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostViewSet(APIView):
    def get(self, request):
        
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({'count': posts.count(), 'results': serializer.data})

    def post(self, request):
    
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'count': Post.objects.count(), 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
