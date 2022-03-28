from rest_framework import generics
from polls.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer, VoteChoiceSerializer
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


class QuestionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        print(pk)
        q = Question.objects.get(pk=pk)
        c = Choice.objects.filter(question__question_text__startswith=q)
        response_data = list()
        for i in c:
            response_data.append({"id": i.id, "choice": str(i)})
        print(response_data)
        return JsonResponse(response_data, safe=False)

#
# class VoteView(generics.ListCreateAPIView):
#     # queryset = Choice.objects.get(pk=pk2)
#     queryset = ''
#     serializer_class = ChoiceSerializer
#
#     def post(self, request, *args, **kwargs):
#         # pk1 = kwargs.post('pk1', None)
#         pk2 = kwargs.post('pk2', None)
#         c = Choice.objects.get(pk=pk2)
#         c.votes += 1
#         c.save()
#         return JsonResponse({'status': 'voting done'})


class Vote(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self, *args, **kwargs):
        pk1 = self.kwargs['pk1']
        pk2 = self.kwargs['pk2']
        c = Choice.objects.get(pk=pk2)
        c.votes += 1
        c.save()
        q = Question.objects.get(pk=pk1)
        new_c = Choice.objects.filter(question__question_text__startswith=q)
        response_data = list()
        for i in new_c:
            response_data.append({"id": i.id, "choice": str(i), "votes": i.votes})
        return JsonResponse(response_data, safe=False)


