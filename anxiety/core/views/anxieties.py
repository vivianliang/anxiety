from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Anxiety

class AnxietiesView(APIView):

    def get(self, request, *args, **kwargs):
        '''Get Anxieties for the request user.'''
        anxieties = Anxiety.objects.filter(user_id=request.user.id)
        serialized_anxieties = AnxietySerializer(anxieties, many=True).data
        return Response(serialized_anxieties)

    def post(self, request, *args, **kwargs):
        '''Create an anxiety.'''
        print 'post', request
        anxiety = Anxiety.objects.create(
            user=request.user,
            fear=request.GET.get('fear'),
            action=request.GET.get('action'),
        )
        return Response({'anxiety_id': anxiety.id})
