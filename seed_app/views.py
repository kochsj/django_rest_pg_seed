# from rest_framework import generics
# from .models import YourModel
# from .serializers import YourSerializer
# from .permissions import IsAuthorOrReadOnly

# # Create your views here.
# class YourList(generics.ListCreateAPIView):
#     queryset = YourModel.objects.all()
#     serializer_class = YourSerializer

# class YourDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = YourModel.objects.all()
#     serializer_class = YourSerializer
#     permission_classes = (IsAuthorOrReadOnly,)