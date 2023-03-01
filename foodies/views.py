from rest_framework import viewsets
from .models import User_Account, Comment, Post
from rest_framework.views import APIView
from .serializers import User_AccountSerializer, CommentSerializer, PostSerializer
from rest_framework import permissions
from rest_framework.response import Response


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
                userProfile = User_Account.objects.get(user=user)
                Post.objects.create(user=userProfile, body=body, location=location, title=title, date=date, image=image, likes=likes)
                return Response({'message': "Post Successfully Created"})
            else:
                return Response({'error': "Not authenticated; Include an authentication token"})
        except Exception as e:
            print("Error", e)
            return Response({'error': "Error: Invaild body"})
    def get(self, request): 
        try:
            results = Post.objects.all()
            all_post = PostSerializer(results, many=True)
            return Response(all_post.data)
        except:
            return Response({"error": "Something went wrong"})
  
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
            return Response({"error": "Something went wrong"})
    def put(self, request, id):
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
                Account = User_Account.objects.get(user=user)
                Posts = Post.objects.get(id=id)
                userAccount = Account.id
                userPost = Posts.id
                if userPost == userAccount:
                    Post.objects.update(body=body, location=location, title=title, date=date, image=image, likes=likes)
                    return Response({'message': 'Post successfully updated'})
                else:
                    return Response({'message': "You are not authorized to perform this action"})
            else:
                return Response({'error': "Not Authenticated make sure you include a token"})
        except:
            return Response({'error': "Error: Invalid Body"})
    def delete(self, request, id):
        try:
            user = self.request.user
            isAuthenticated = user.is_authenticated
            if isAuthenticated:
                userAccount = User_Account.objects.get(user=user)
                Posts = Post.objects.get(id=id)
                Profile = userAccount.id
                userPost = Posts.user_id
                if Profile == userPost:
                    Posts.delete()
                    return Response({'message': "Post Successfully Deleted!!"})
                else:
                    return Response({'message': "You are not authorized to perform this action"})
            else:
                return Response({'error': "Not Authenticated make sure you include a token"})
        except:
            return Response({'error': "Error: Invalid Body"})
  
class Comment_ViewSet(APIView):
    permission_classes = [
        permissions.AllowAny
    ]
    def post(self,request,id):
        try:
            user = self.request.user
            isAuthenticated = user.is_authenticated
            if isAuthenticated:
                body = request.data['body']
                userProfile = User_Account.objects.get(user=user)
                post = Post.objects.get(id=id)
                Comment.objects.create(user=userProfile, body=body, post=post)
                return Response({'message': "Comment Successfully Created"})
            else:
                return Response({'error': "Not authenticated make sure you include a token"})
        except:
            return Response({'error': "( ﾟДﾟ)b error; you are most likely messed up by passing an invaild body"})
