from rest_framework import serializers
from .models  import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['name','url','language','price']