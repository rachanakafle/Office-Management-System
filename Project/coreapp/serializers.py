from coreapp.models import MyUser, Partner, Project, ProjectManager, Developer
from rest_framework import serializers

'''serializer determines the attributes to manipulate'''

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'password','email', 'first_name', 'last_name','photo','address','contact','position',"groups")
        extra_kwargs = {'password': {'write_only': True}}


#for group
    # @transaction.atomic
    # def create(self, validated_data):
    #     user = MyUser(
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #     )
    #     user.set_password(validated_data['password'])
    #
    #     user.save()
    #
    #     group_filtered = Group.objects.get(pk=self.context['group_id'])
    #     user.groups.add(group_filtered)
    #
    #     return user

#
# class UserDetailReadSerializer(serializers.ModelSerializer):
#     user = MyUserSerializer(read_only=True)
#     class Meta:
#         model = UserDetail
#         fields = '__all__'
#
#
# class UserDetailWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserDetail
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         response['user'] = UserDetailWriteSerializer(instance.user).data
#         return response



class PartnerReadSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)
    class Meta:
        model = Partner
        fields = "__all__"

class PartnerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = MyUserSerializer(instance.user).data
        return response



#
# class ProjectDetailReadSerializer(serializers.ModelSerializer):
#     project = ProjectReadSerializer(read_only=True)
#     class Meta:
#         model = ProjectDetail
#         fields = "__all__"
#
# class ProjectDetailWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProjectDetail
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         response['project'] = ProjectDetailWriteSerializer(instance.project).data
#         return response



class ProjectManagerReadSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)

    class Meta:
        model = ProjectManager
        fields = "__all__"

class ProjectManagerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManager
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = MyUserSerializer(instance.user).data
        return response


class DeveloperReadSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)

    class Meta:
        model = Developer
        fields = "__all__"

class DeveloperWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = MyUserSerializer(instance.user).data
        return response


class ProjectReadSerializer(serializers.ModelSerializer):
    partner = PartnerWriteSerializer(read_only=True)
    project_manager = ProjectManagerWriteSerializer(read_only=True)
    developer = DeveloperWriteSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = (
            'id', 'project_name', 'partner', 'project_manager', 'developer',  'theme', 'status', 'start_date',
            'end_date')


class ProjectWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'project_name', 'partner', 'project_manager', 'developer', 'theme', 'status', 'start_date',
            'end_date')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['partner'] = PartnerWriteSerializer(instance.partner).data
        response['project_manager'] = ProjectManagerWriteSerializer(instance.project_manager).data
        return response


class CounterSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    developer = serializers.IntegerField()
    pm = serializers.IntegerField()
    partner = serializers.IntegerField()
    queued = serializers.IntegerField()
    ongoing = serializers.IntegerField()
    completed = serializers.IntegerField()
    suspended = serializers.IntegerField()
    project = serializers.IntegerField()
