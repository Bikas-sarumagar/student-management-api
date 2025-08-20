from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from .permissions import IsStaffOrReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['student_class']
    search_fields = ['name', 'student_class']
    Ordering_fields = ['roll', 'name', 'student_class', "dob"]
    ordering = ['roll']
    permission_classes = [IsStaffOrReadOnly]
    
    def create(self, request, *args, **kwargs):
        # Handle both single object & list of objects
        is_many = isinstance(request.data, list)

        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)