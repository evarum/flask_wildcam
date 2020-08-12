import os
from flaskr.flask_app.config import PATH, PIC_ENDUNG, VID_ENDUNG, DATE_FORMAT, TIME_FORMAT


# creates dictionary with two connected keys date, time
def get_file_meta(filename):
    # cut includes time information
    cut = filenames_split(filename)
    # cut out needed parts
    year = cut[0:4]
    month = cut[4:6]
    day = cut[6:8]
    hour = cut[8:10]
    minute = cut[10:12]
    second = cut[12:14]
    # format it
    date = DATE_FORMAT.format(day, month, year)
    time = TIME_FORMAT.format(hour, minute, second)
    meta = {}
    meta['date'] = date
    meta['time'] = time
    return meta

# assignment of date,time to element in folder (picture or video)
def data_to_html_file():
    filenames = pic_vid_connection()
    files = []
    # gradually assigning and saving of filename
    for file_pair in filenames:
        vid_file = file_pair[0]
        pic_file = file_pair[1]
        meta = get_file_meta(vid_file)
        meta['picture'] = pic_file
        meta['video'] = vid_file
        files.append(meta)
    return files

# split filename in event, date/time, ending
def filenames_split(video):
    cut = video.split('.')
    cut = cut[0]
    cut = cut.split('-')
    cut = cut[1]
    return cut

def cut_data_fixed_to_filename(end):
    list_cut_element, cut_elements = data_to_cut(end)
    # filenames will be sorted list of cut_elements' values
    filenames = []
    for i in list_cut_element:
        # element_value list filled with responding values to list_cut_element
        element_value = cut_elements[i]
        filenames.append(element_value)
    return filenames

def data_to_cut(end):
    ext = end
    direc = PATH
    # list of all elements in Path-folder (filenames not sorted)
    elements_list = []
    for i in os.listdir(direc):
        if os.path.splitext(i)[1] == ext:
            elements_list.append(i)
    # Dictionary to store eventual date/time together with filename
    cut_elements = {}
    for element in elements_list:
        # filename shortened to date/time
        cut_element = filenames_split(element)
       # Dictionary-entry cut_element(date/time): element(filename)
        cut_elements[cut_element] = element
    # keys of cut_elements to list
    list_cut_element = list(cut_elements.keys())
    # sorted list new to old
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
            upper_limit = None
        else:
            upper_limit = int(limits_list[upper_limit_index])
        for element_between in liste_between:
            element_between_int = int(element_between)
            # is element_between bigger/equal than the lower_limit?
            if element_between_int >= lower_limit_int:
                # special case last element
                if upper_limit is None:
                    paar.append([lower_limit, element_between])
                    break
                # is element_between bigger than the upper_limit?
                if element_between_int > upper_limit:
                    # exit loop and go to next element_between
                    continue
                else:
                    # appending lower_limit and element_between to list paar
                    paar.append([lower_limit,element_between])
                    break
        liste_between.remove(element_between)
    # giving back the finished sets
    return paar

def pic_vid_connection():

    limit_list, limit_dict = data_to_cut(VID_ENDUNG)
    # print(limit_list)
    # print(limit_dict)
    pic_list, pic_dict = data_to_cut(PIC_ENDUNG)
    # sorted lists are being connected to one
    paar_list = paar_sort(limit_list, pic_list)
    results = []
    # for loop takes cut videos and pictures, puts it into the list limit_dict and pic_dict, then appends it to list results
    for paar in paar_list:
        cut_vid = paar[0]
        cut_pic = paar[1]
        video_value = limit_dict[cut_vid]
        picture_value = pic_dict[cut_pic]
        results.append([video_value, picture_value])
    return results