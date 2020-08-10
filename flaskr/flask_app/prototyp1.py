import os
from flaskr.flask_app.config import PATH, VID_ENDUNG
from flaskr.flask_app.helper import filenames_split


def data_to_cut(end):
    ext = end
    direc = PATH
    #liste aller videos im Ordner
    video_list = []
    for i in os.listdir(direc):
        if os.path.splitext(i)[1] == ext:
            video_list.append(i)
    cut_videos = {}
    for video in video_list:
        #Dateinnamen in video_list zu Datum, Uhrzeit gekürzt
        cut = filenames_split(video)
        #Dictionary-eintrag cut: video
        cut_videos[cut] = video
    list_cuts = list(cut_videos.keys())
    list_cuts.sort(reverse = True)
    filenames = []
    for i in list_cuts:
        value = cut_videos[i]
        filenames.append(value)
    return cut_videos

data_to_cut(VID_ENDUNG)

#list_cuts = list(cut_videos.keys())
#list_cuts.sort(reverse=True)
#print('cuts', list_cuts)

#filenames = []
#for i in list_cuts:
 #   value = cut_videos[i]
  #  filenames.append(value)