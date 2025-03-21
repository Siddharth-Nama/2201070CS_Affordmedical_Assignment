from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer

@api_view(['GET'])
def top_users(request):
    users = User.objects.order_by('-post_count')[:5]
    serializer = UserSerializer(users, many=True)
    return Response({"top_users": serializer.data})

@api_view(['GET'])
def top_or_latest_posts(request):
    post_type = request.GET.get('type', 'latest')
    posts = Post.objects.filter(type=post_type)
    serializer = PostSerializer(posts, many=True)
    return Response({"posts": serializer.data})

@api_view(['GET'])
def get_comments(request, postid):
    post = get_object_or_404(Post, id=postid)
    comments = Comment.objects.filter(post=post)
    serializer = CommentSerializer(comments, many=True)
    return Response({"comments": serializer.data})
