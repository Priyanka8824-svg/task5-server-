from django.shortcuts import render
from .serializers import TaskSerialzier, TaskUpdateSerialzier
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .models import Task
from .permissions import IsManager, IsAssingee, IsManagerOrTL
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

import logging
logger = logging.getLogger(__name__)

# create/list task
class TaskListCreateAPI(generics.ListCreateAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated, IsManagerOrTL]
    serializer_class = TaskSerialzier
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(task_assigned_by = self.request.user)

# list assigned task
class AssignedTaskListAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        tasks = Task.objects.filter(task_assigned_to = request.user)
        serializer = TaskSerialzier(tasks, many=True)
        return Response(data=serializer.data)
    
# update(complete) task
class TaskUpdateAPI(generics.UpdateAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated, IsAssingee]
    serializer_class=TaskUpdateSerialzier
    queryset=Task.objects.all()

# delete task
class TaskDeleteAPI(generics.DestroyAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated, IsManager]
    serializer_class=TaskSerialzier
    queryset=Task.objects.all()

