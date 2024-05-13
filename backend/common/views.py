from rest_framework.generics import ListCreateAPIView

from common.models import Task
from common.serializers import TaskSerializer


class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
