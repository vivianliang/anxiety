from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Anxiety
from core.serializers import AnxietySerializer

class AnxietiesView(APIView):

    def get(self, request, *args, **kwargs):
        '''Get the request user's anxieties.'''
        anxieties = Anxiety.objects.filter(user_id=request.user.id)
        serialized_anxieties = AnxietySerializer(anxieties, many=True).data
        return Response(serialized_anxieties)

    def post(self, request, *args, **kwargs):
        '''Create an anxiety.'''
        anxiety = Anxiety.objects.create(
            user_id=request.user.id,
            fear=request.data.get('fear'),
            action=request.data.get('action'),
        )
        return Response({'anxiety_id': anxiety.id})
