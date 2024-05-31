from coreapp.models import MyUser, Partner, Project, ProjectManager, Developer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.core.mail import send_mail

from coreapp.serializers import MyUserSerializer, ProjectReadSerializer, \
     ProjectManagerReadSerializer, DeveloperReadSerializer, PartnerReadSerializer, PartnerWriteSerializer, ProjectWriteSerializer,  \
    ProjectManagerWriteSerializer, DeveloperWriteSerializer, CounterSerializer

"""
    API endpoint that allows users to be viewed or edited.
    """


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

#for group
    # def create(self, request, *args, **kwargs):
    #     group_id = request.data['groups']
    #     serializer = MyUserSerializer(data=request.data, context={'group_id': group_id})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

# class UserDetailViewSet(viewsets.ModelViewSet):
#     queryset = UserDetail.objects.all()
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
#             return UserDetailWriteSerializer
#         else:
#             return UserDetailReadSerializer
#
#     def retrieve(self, request, *args, **kwargs):
#         instance = UserDetail.objects.get(user_id=kwargs['pk'])
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
#
#
#     serializer_class = UserDetailReadSerializer



class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.filter(user__groups='3')

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return PartnerWriteSerializer
        else:
            return PartnerReadSerializer

    serializer_class = PartnerReadSerializer


    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)
        id = data.data['id']
        id = Partner.objects.get(id=id).user_id
        u = MyUser.objects.get(id=id)
        send_mail('Login Credentials',
                  'Hello ' + u.first_name + ' Your account credential have been  created or modified:'
                                            ' username:' + u.email + ' password :' + u.password, 'iwcore_admin@gmail.com',  [u.email, ])
        return Response(request.data)


#
# class ProjectDetailViewSet(viewsets.ModelViewSet):
#     queryset = ProjectDetail.objects.all()
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST'or self.request.method == 'PUT' or self.request.method == 'PATCH':
#             return ProjectDetailWriteSerializer
#         else:
#             return ProjectDetailReadSerializer
#
#     serializer_class = ProjectDetailReadSerializer



class ProjectManagerViewSet(viewsets.ModelViewSet):
    queryset = ProjectManager.objects.filter(user__groups='2')

    def get_serializer_class(self):
        if self.request.method == 'POST'or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return ProjectManagerWriteSerializer
        else:
            return ProjectManagerReadSerializer

    serializer_class = ProjectManagerReadSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)
        id = data.data['id']
        id = ProjectManager.objects.get(id=id).user_id
        u = MyUser.objects.get(id=id)
        send_mail('Login Credentials',
                  'Hello ' + u.first_name + ' Your account credential have been  created or modified:'
                                            ' username:' + u.email + ' password :' + u.password, 'iwcore_admin@gmail.com',   [u.email,])
        return Response(request.data)


class DeveloperViewset(viewsets.ModelViewSet):
    queryset = Developer.objects.filter(user__groups='1')

    def get_serializer_class(self):
        if self.request.method == 'POST'or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return DeveloperWriteSerializer
        else:
            return DeveloperReadSerializer

    serializer_class = DeveloperReadSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)
        id = data.data['id']
        id = Developer.objects.get(id=id).user_id
        u = MyUser.objects.get(id=id)
        send_mail('Login Credentials',
                  'Hello ' + u.first_name + ' Your account credential have been  created or modified:'
                                             'username:' + u.email + ' password :' + u.password,  'iwcore_admin@gmail.com',[u.email,])
        return Response(request.data)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return ProjectWriteSerializer
        else:
            return ProjectReadSerializer

    serializer_class = ProjectReadSerializer


class Counter(generics.RetrieveAPIView):
    serializer_class = CounterSerializer

    def get_queryset(self):
        return

    def get(self, request):
        user = MyUser.objects.all().count()
        developer = Developer.objects.all().count()
        pm = ProjectManager.objects.all().count()
        partner = Partner.objects.all().count()
        queued = Project.objects.filter(status='queued').count()
        ongoing = Project.objects.filter(status='ongoing').count()
        completed = Project.objects.filter(status='completed').count()
        suspended = Project.objects.filter(status='suspended').count()
        project = Project.objects.all().count()
        count_data = [{'user': user, 'developer': developer, 'pm': pm,
                       'partner': partner, 'queued': queued,
                       'ongoing': ongoing, 'completed': completed
                       ,'suspended': suspended, 'project': project}]
        data = CounterSerializer(count_data, many=True).data

        return Response(data)
