# GET: get an anxiety
# PUT: update/replace
# DELETE: delete a anxity

from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Anxiety
from core.serializers import AnxietySerializer

class AnxietyView(APIView):

    def get(self, request, anxiety_id, *args, **kwargs):
        '''Get anxieties.'''
        try:
            anxiety = Anxiety.objects.get(id=anxiety_id)
        except Anxiety.DoesNotExist:
            raise Exception('invalid anxiety id')
        return Response(AnxietySerializer(anxiety).data)

    def put(self, request, anxiety_id, *args, **kwargs):
        '''Edit an existing anxiety.'''
        try:
            anxiety = Anxiety.objects.get(id=anxiety_id)
        except Anxiety.DoesNotExist:
            raise Exception('invalid anxiety id')

        anxiety.fear = request.data.get('fear')
        anxiety.action = request.data.get('action')
        anxiety.save()

        return Response(AnxietySerializer(anxiety).data)
