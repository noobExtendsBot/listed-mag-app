from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class MagazineDetailView(DetailView):
	permission_classes = (IsAuthenticated,)
	template_name = "magazines/reader.html"
	def get(self, request, *args, **kwargs):
		context = {
			"data": "some random stuff",
			"date": "some date",
		}
		return render(request, "magazines/reader.html", context)

