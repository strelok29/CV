from django.shortcuts import render

def index(request):
	return render(request,'personal/home.html')

def contact(request):
	return render(request,'personal/basic.html', {'content' :['if you would contact me, please email me','strelok.rifqi@gmail.com']})