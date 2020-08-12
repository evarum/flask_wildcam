import os
from flaskr.flask_app.config import PATH, PIC_ENDUNG, VID_ENDUNG

# Noah
# creates dictionary with three connected keys filename, date, time
def get_file_meta(filename):
    meta = {}
    meta['date'] = 'u'
    meta['time'] = 't'
    return meta

# Eva
# zuordnung von date,time zu element im ordner (bild oder video)
def data_to_html_file():
    filenames = pic_vid_connection()
    files = []
    # schrittweise zuordnen und speichern von filename
    for file_pair in filenames:
        vid_file = file_pair[0]
        pic_file = file_pair[1]
        meta = get_file_meta(vid_file)
        meta['picture'] = pic_file
        meta['video'] = vid_file
        files.append(meta)
    return files

# Eva
# teilt filename in event, date/time, endung
def filenames_split(video):
    cut = video.split('.')
    cut = cut[0]
    cut = cut.split('-')
    cut = cut[1]
    return cut

# Eva
def cut_data_fixed_to_filename(end):
    list_cut_element, cut_elements = data_to_cut(end)
    # filenames will be sorted list of cut_elements' values
    filenames = []
    for i in list_cut_element:
        # element_value list filled with responding values to list_cut_element
        element_value = cut_elements[i]
        filenames.append(element_value)
    return filenames

# Eva
def data_to_cut(end):
    ext = end
    direc = PATH
    #liste aller Elemente im Path-Ordner (filenames not sorted)
    elements_list = []
    for i in os.listdir(direc):
        if os.path.splitext(i)[1] == ext:
            elements_list.append(i)
    #Dictionary to store eventual date/time together with filename
    cut_elements = {}
    for element in elements_list:
        #filename shortened to date/time
        cut_element = filenames_split(element)
       #Dictionary-eintrag cut_element(date/time): element(filename)
        cut_elements[cut_element] = element
    #keys of cut_elements to list
    list_cut_element = list(cut_elements.keys())
    #sorted list new to old
    list_cut_element.sort()
    return list_cut_element, cut_elements

# Elfi
# two sorted lists are compared and written down if they fullfill the following condition: lower_limit <= element_between < upper_limit
def paar_sort(list1, list2):
    # limits_list sets the borders of possible placement for elements of liste_between
    limits_list = list1
    liste_between = list2
    paar = []
    # iteration through limits_list
    for lower_limit in limits_list:
        lower_limit_int = int(lower_limit)
       # print(lower_limit)
        # defining upper_limit
        lower_limit_index = limits_list.index(lower_limit)
        upper_limit_index = lower_limit_index + 1

        if upper_limit_index >= len(limits_list):
            # last element has no upper_limit in list
            break
        upper_limit = int(limits_list[upper_limit_index])
        for element_between in liste_between:
            element_between_int = int(element_between)
            # is element_between bigger/equal than the lower_limit?
            if element_between_int >= lower_limit_int:

                # is element_between bigger than the upper_limit?
                if element_between_int > upper_limit:
                    # exit loop and go to next element_between
                    continue
                else:
                    # appending lower_limit and element_between to list paar
                    paar.append([lower_limit,element_between])
                    break
        liste_between.remove(element_between)
    # we have to deal with the last lower limit seperatly
    lower_limit = limits_list[-1]
    lower_limit_int = int(lower_limit)
    for element_between in liste_between:
        element_between_int = int(element_between)
        # is element_between bigger/equal than the lower_limit?
        if element_between_int >= lower_limit_int:
            # appending lower_limit and element_between to list paar
            paar.append([lower_limit, element_between])
            break
    # giving back the finished sets
    return paar

# Noah
def pic_vid_connection():
    limit_list, limit_dict = data_to_cut(VID_ENDUNG)
   # print(limit_list)
    # print(limit_dict)
    pic_list, pic_dict = data_to_cut(PIC_ENDUNG)
    paar_list = paar_sort(limit_list, pic_list)
    results = []
    for paar in paar_list:
        cut_vid = paar[0]
        cut_pic = paar[1]
        video_value = limit_dict[cut_vid]
        picture_value = pic_dict[cut_pic]
        results.append([video_value, picture_value])
    return results


