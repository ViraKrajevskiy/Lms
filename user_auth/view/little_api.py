from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_auth.models.Hw_model.model_lesson import Room

@api_view(['GET'])
def total_room_count(request):
    count = Room.objects.count()
    return Response({"total_rooms": count})
