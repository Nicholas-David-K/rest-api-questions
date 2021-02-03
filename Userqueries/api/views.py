from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .serializers import AnswerSerializer, QuestionSerializer
from Userqueries.models import Answer, Question
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import filters



"""
    Lists all questions for all users

    Include endpoint to search (api/questions/?search=)
"""
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']
    # lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)




"""
    This view creates a answer given the pk or slug of a question
    endpont: questions/<int:pk>/answer/

    REALLY IMPORANT TO KNOW THIS!
"""
class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all() 
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        request_user = self.request.user
        question = get_object_or_404(Question, pk=self.kwargs.get('pk'))

        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have already answered this question")

        serializer.save(author=request_user, question=question)








"""
    This view lists all answers for a single question
    endpont: questions/<int:pk>/answers/
"""
class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Answer.objects.filter(question__pk=pk).order_by('-created_at')
 





"""
    retrive, update or delete an answer instance
"""
class AnswerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)





"""
    Handles liking an answer instance
"""
class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user

        answer.voters.remove(user)
        answer.save()

        serializer_context = {'request': request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user

        answer.voters.add(user)
        answer.save()

        serializer_context = {'request': request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
