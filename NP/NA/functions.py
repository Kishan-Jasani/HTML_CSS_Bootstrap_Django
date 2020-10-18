def Handle_upload_file(f):
    with open('NP/resumes/2020-10-11/'+f.file,'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
