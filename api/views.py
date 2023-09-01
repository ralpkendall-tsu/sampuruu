from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Course
from .CourseSerializer import CourseSerializer

# Create your views here.

@api_view(['GET'])
def getCourses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getCourse(request, id):
    course = Course.objects.get(pk=id)
    serializer = CourseSerializer(course, many=False)

    return Response(serializer.data)