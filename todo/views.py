from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
import logging

logger = logging.getLogger(__name__)


def list_todo_by_user(request, username):
    user = request.user
    if user:
        todo_list = Todo.objects.filter(user=user).order_by('-created_at')
        logger.debug("get %d todos from %s", len(todo_list), user)
        return JsonResponse(todo_list)