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

# two sorted lists are compared and written down if they fullfill the following condition: lower_limit <= element_between < upper_limit
def paar_sort(list1, list2):
    # limits_list sets the borders of possible placement for elements of liste_between
    limits_list = list1
    liste_between = list2
    paar = []
    # iteration through limits_list
    for lower_limit in limits_list:
       # print(lower_limit)
        for element_between in liste_between:
            # is element_between bigger/equal than the lower_limit?
            if element_between >= lower_limit:
                # defining upper_limit
                upper_limit = lower_limit+1
                # is element_between bigger than the upper_limit?
                if element_between > upper_limit:
                    # exit loop and go to next element_between
                    break
                # appending lower_limit and element_between to list paar
                paar.append([lower_limit,element_between])
    print(paar)
    # giving back the finished sets
    return paar