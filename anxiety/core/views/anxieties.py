from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Anxiety

class AnxietiesView(APIView):

    def get(self, request, *args, **kwargs):
        '''Get Anxieties.'''
        # TODO
        # print 'get', request
        # anxiety = Anxiety.objects.get(id=request.GET.get('anxiety_id'))
        return Response({})

    def post(self, request, *args, **kwargs):
        '''Create an anxiety.'''
        print 'post', request
        anxiety = Anxiety.objects.create(
            user=request.user,
            fear=request.GET.get('fear'),
            action=request.GET.get('action'),
        )
        return Response({'anxiety_id': anxiety.id})
