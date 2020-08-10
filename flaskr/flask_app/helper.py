import os
from flaskr.flask_app.config import PATH, PIC_ENDUNG, VID_ENDUNG

#creates dictionary with three connected keys filename, date, time
def get_file_meta(filename):
    meta = {}
    meta['filename'] = filename
    meta['date'] = 'u'
    meta['time'] = 't'

    return meta


#zuordnung von date,time zu element im ordner (bild oder video)
def data_to_html_file(end):
    filenames = data_to_cut(end)
    files = []
    #schrittweise zuordnen und speichern von filename
    for filename in filenames:
            meta = get_file_meta(filename)
            files.append(meta)
    return files

#teilt filename in event, date/time, endung
def filenames_split(video):
    cut = video.split('.')
    cut = cut[0]
    cut = cut.split('-')
    cut = cut[1]
    return cut

def data_to_cut(end):
    ext = end
    direc = PATH
    #liste aller Elemente im Path-Ordner (filenames not sorted)
    elements_list = []
    for i in os.listdir(direc):
        if os.path.splitext(i)[1] == ext:
            elements_list.append(i)
    #Dictionary to store evantual date/time together with filename
    cut_elements = {}
    for element in elements_list:
        #filename shortened to date/time
        cut_element = filenames_split(element)
        #Dictionary-eintrag cut_element(date/time): element(filename)
        cut_elements[cut_element] = element
    #keys of cut_elements to list
    list_cut_element = list(cut_elements.keys())
    #sorted list new to old
    list_cut_element.sort(reverse = True)
    #filenames will be sorted list of cut_elements' values
    filenames = []
    for i in list_cut_element:
        #element_value list filled with responding values to list_cut_element
        element_value = cut_elements[i]
        filenames.append(element_value)
    print(filenames)
    return filenames

data_to_html_file(PIC_ENDUNG)
