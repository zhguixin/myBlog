# -*- coding: UTF-8 -*-
from rest_framework import viewsets, status
from rest_framework.response import Response
from blog.models import Blog
from blogapi.serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    # 重写该方法，默认返回 status.HTTP_204_NO_CONTENT，
    # 避免返回空信息
    def destroy(self, request, *args, **kwargs):
        blog = self.get_object()
        if blog is not None:
            blog.delete()
            return Response({"message": "delete succeed", "code": "200"},
                            status=status.HTTP_200_OK)
        return super(BlogViewSet, self).destroy(self, request, *args, **kwargs)
