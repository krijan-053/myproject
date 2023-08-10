from rest_framework import serializers
from myapp.models import ClassRoom, Student, StudentProfile


class ClassRoomSerializer(serializers.Serializer):
    name = serializers.CharField()


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "name"]


class StudentModelSerializer(serializers.ModelSerializer):
    # classroom = ClassRoomModelSerializer()
    description = serializers.SerializerMethodField()
    address = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    phone_no = serializers.CharField(required=False)

    class Meta:
        model = Student
        fields = ["id", "name", "age", "department", "classroom", "description", "profile_picture", "address", "email",
                  "phone_no"]

    def get_description(self, obj):
        return f"Hello I am {obj.name} and I'm {obj.age} years old."

    # def validate(self, attrs):
    #     if attrs["name"] == "Jon" or attrs["age"] > 20:
    #         raise serializers.ValidationError("Invalid request data")
    #     return attrs
    #
    # def validate_department(self, department):
    #     if department not in ["IT", "CS", "Electrical"]:
    #         raise serializers.ValidationError("Department must be IT,CS or Electrical")
    #     return department

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method.lower() == "get":
            fields["classroom"] = ClassRoomModelSerializer()
        return fields

    def create(self, validated_data):
        address = validated_data.pop("address", None)
        email = validated_data.pop("email", None)
        phone_no = validated_data.pop("phone_no", None)
        student = super().create(validated_data)
        if all([address, email, phone_no]):
            StudentProfile.objects.create(address=address, phone_no=phone_no, email=email, student=student)
        return student


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ["id", "student", "address", "phone_no", "email"]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method.lower() == "get":
            fields["student"] = StudentModelSerializer()
        return fields
