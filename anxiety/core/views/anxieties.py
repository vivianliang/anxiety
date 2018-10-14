from rest_framework.response import Response

from core.models import Anxiety

class AnxietiesView(APIView):

    def get(self, request, *args, **kwargs):
        '''Get Anxieties.'''
        # TODO
        return Response({})

    def post(self, request, *args, **kwargs):
        '''Create an anxiety.'''
        anxiety = Anxiety.objects.create(
            user=request.user,
            fear=request.GET.get('fear'),
            action=request.GET.get('action'),
        )
        return Response({'anxiety_id': anxiety.id})
