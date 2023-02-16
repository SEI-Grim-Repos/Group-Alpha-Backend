from rest_framework import viewsets
from .models import User_Account, Comment, Post
from rest_framework.views import APIView
from .serializers import User_AccountSerializer, CommentSerializer, PostSerializer
from rest_framework import permissions
from rest_framework.response import Response

# Create your views here.

class User_AccountViewSet(viewsets.ModelViewSet):
  queryset = User_Account.objects.all()
  serializer_class = User_AccountSerializer;
  
class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer;

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer;
  
class AllPost_ViewSet(APIView):
  permission_classes = [
    permissions.AllowAny
  ]
  def post(self,request):
    try:
      user = self.request.user
      isAuthenticated = user.is_authenticated
      if isAuthenticated:
          body = request.data['body']
          location = request.data['location']
          date = request.data['date']
          title = request.data['title']
          image = request.data['image']
          likes = request.data['likes']
          # This is to get the profile of the user who is making this post
          userProfile = User_Account.objects.get(user=user)
          Post.objects.create(user=userProfile, body=body, location=location, title=title, date=date, image=image, likes=likes)
          return Response({'message': " ◕‿↼ Post Successfully Created ! "})
      else:
          return Response({'error': "ヽ(ﾟДﾟ)ﾉ  not authenticated make sure you include a token"})
    except Exception as e:
          print("Error", e)
          return Response({'error': "( ﾟДﾟ)b error; you are most likely messed up by passing an invaild body"})
  def get(self, request): 
    try:
      results = Post.objects.all()
      all_post = PostSerializer(results, many=True)
      return Response(all_post.data)
    except:
      return Response({"error": "( ﾟДﾟ)b  somthing went wrong "})
  
class OnePost_ViewSet(APIView):
  permission_classes = [
    permissions.AllowAny
  ]
  def get(self, request,id):
    try:
      post_results = Post.objects.get(id=id)
      post = PostSerializer(post_results)
      comments_results = Comment.objects.filter(post=id)
      comments = CommentSerializer(comments_results, many=True)
      
      return Response({"post": post.data, "comments": comments.data})
    except Exception as e:
      print("Error getting One Post:", e)
      return Response({"error": "( ﾟДﾟ)b  somthing went wrong "})
  
class Comment_ViewSet(APIView):
  permission_classes = [
    permissions.AllowAny
  ]
  def post(self,request,id):
    try:
      user = self.request.user
      isAuthenticated = user.is_authenticated
      print("I'm in user comment creation")
      if isAuthenticated:
          body = request.data['body']
          # This is to get the profile of the user who is making this post
          userProfile = User_Account.objects.get(user=user)
          post = Post.objects.get(id=id)
          print("Userprofile:", userProfile)
          print("Post:", post)
          Comment.objects.create(user=userProfile, body=body, post=post)
          return Response({'message': " ◕‿↼ Comment Successfully Created ! "})
      else:
          return Response({'error': "ヽ(ﾟДﾟ)ﾉ  not authenticated make sure you include a token"})
    except:
          return Response({'error': "( ﾟДﾟ)b error; you are most likely messed up by passing an invaild body"})
