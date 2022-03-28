from rest_framework import generics
from blog.models import Post, Categories, Comment
from users.models import CustomUser
from .serializers import PostSerializer, CategoriesSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
import json
from listed.settings import *


class PostList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        p = Post.objects.all()
        response_data = list()
        for i in p:
            response_data.append(
                {
                    "id": i.id,
                    "title": str(i.title),
                    "author": str(i.author),
                    "post_cat": str(i.post_cat),
                    "post_img": GLOBAL_MEDIA_URL+str(i.post_img),
                    "content": str(i.content),
                    "created_at": str(i.created_at),
                    "updated_at": str(i.updated_at)
                }
            )
        return JsonResponse(response_data, safe=False)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        p = Post.objects.filter(pk=pk)
        response_data = list()
        print(p)
        for i in p:
            response_data.append(
                {
                    "id": i.id,
                    "title": str(i.title),
                    "author": str(i.author),
                    "post_cat": str(i.post_cat),
                    "post_img": GLOBAL_MEDIA_URL+str(i.post_img),
                    "content": str(i.content),
                    "created_at": str(i.created_at),
                    "updated_at": str(i.updated_at)
                }
            )
        return JsonResponse(response_data, safe=False)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoriesList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoryPostList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        p = Post.objects.filter(post_cat=pk)
        response_data = list()
        for i in p:
            # print(GLOBAL_MEDIA_URL+str(i.post_img))
            response_data.append(
                {
                    "id": i.id,
                    "title": str(i.title),
                    "post_cat": pk,
                    "post_img": GLOBAL_MEDIA_URL+str(i.post_img),
                    "content": str(i.content),
                    "created_at": str(i.created_at),
                    "updated_at": str(i.updated_at)
                }
            )
        # print(response_data)
        return JsonResponse(response_data, safe=False)

class CategoriesDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CommentListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    # queryset = Comment.objects.all()
    # serializer_class = CommentSerializer

    def get(self, *args, **kwargs):
        pk = self.kwargs['pk']
        c = Comment.objects.all()
        response_data = list()
        for i in c:
            if i.post_id == pk:
                # print(i)
                response_data.append({"author": str(i.author), "text": str(i.text)})
        # print(response_data)
        return JsonResponse(response_data, safe=False)

    # def post(self, request, **kwargs):
    #     print(request.POST)
    #     print(request.POST['text'])
    #     print(request.POST.get('text'))
    #     print(request.POST.get('user'))
    #     if request.method == "POST":
    #         # pk1 -> post, pk2->user
    #         pk = self.kwargs['pk']
    #         # p = Post.objects.get(pk=pk)
    #         # u = request.POST.get('user')
    #         # print(u)
    #         # u = CustomUser.objects.get(email=u)
    #         # text = request.POST.get('text')
    #         # print(text)
    #         # c = Comment()
    #         # c.post = p
    #         # # print(u)
    #         # c.author = u
    #         # c.text = text
    #         # c.save()
    #         return JsonResponse({"status": "Comment posted"})
    #     else:
    #         return JsonResponse({"status": "Could not post comment."})

class CommentPost(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, **kwargs):
        print(request.body)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
    
        if request.method == "POST":
            # pk1 -> post, pk2->user
            pk = self.kwargs['pk']
            p = Post.objects.get(pk=pk)
            u = body['user']
            print(u)
            u = CustomUser.objects.get(email=u)
            text = body['text']
            print(text)
            c = Comment()
            c.post = p
            # print(u)
            c.author = u
            c.text = text
            c.save()
            return JsonResponse({"status": "Comment posted"})
        else:
            return JsonResponse({"status": "Could not post comment."})

class CommentDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateView(generics.ListAPIView):
    pass
    '''
        def get(self, *args, **kwargs):
            pk = self.kwargs['pk']
            
    '''


