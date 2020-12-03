from django.shortcuts import render,HttpResponse,redirect
from .forms import Video_form
from .models import Video

import sys
import subprocess
import os

def initiate_pipeline(python_file_path, video_file_path):
	subprocess.Popen([sys.executable, python_file_path, '-a', '-v', video_file_path])

def index(request):
    all_video=Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()        
            # TODO add pipeline code
            # print('video/%y/' + request.FILES['video'].name)
            # video_file_path = 'baseball.mp4'
            video_file_path = request.FILES['video'].name

            print(os.getcwd())
            initiate_pipeline('../GASTNet-pipeline/gen_skes.py', video_file_path)
            output_path = os.path.dirname(os.path.abspath(__file__)) + '../GASTNet-pipeline/output/animation_' + request.FILES['video'].name
            return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
        form=Video_form()
    return render(request,'index.html',{"form":form,"all":all_video})