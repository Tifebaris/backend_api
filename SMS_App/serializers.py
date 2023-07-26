from rest_framework import serializers
from .models import Student, Course, Instructor
from django.contrib.auth.models import User


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=100)
    about_course = serializers.CharField()
    duration = serializers.CharField(max_length=500)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    start_date = serializers.DateField()
    end_date = serializers.DateField()

#object level validation
    def validate(self, attrs):
        if attrs['duration'] != '3 months':
            raise serializers.ValidationError('Please duration must be 3 months')
        return super().validate(attrs)
    
    # def validate_title(self, value):
    #     if not isinstance(value, [float]):
    #         raise serializers.ValidationError('Only decimals are allowed')
        
    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self,instance,  validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.about_course=validated_data.get('about_course',instance.about_course)
        instance.duration=validated_data.get('duration',instance.duration)
        instance.price=validated_data.get('price',instance.price)
        instance.start_date=validated_data.get('start_date',instance.start_date)
        instance.end_date=validated_data.get('end_date',instance.end_date)
        instance.save()
        return instance
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'age', 'gender', 'email', 'contact', 'address']

class IntsructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['name', 'course_assigned',  'gender', 'email']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password' ]

