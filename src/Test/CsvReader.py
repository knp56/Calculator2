import csv
from Fileutilities.absolutepath import absolute_path
#from pprint import pprint

def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)

class CsvReader:
    data = []

    def __init__(self,filepath):
        self.opdata = []

        # self.data = []
        # with open(absolute_path(filepath)) as text_data:
        #     csv_data = csv.DictReader(text_data)
        #     for row in csv_data:
        #         self.data.append(row)
        # pass

        try:
            with open(absolute_path(filepath)) as text_data:
                csv_data = csv.DictReader(text_data)
                for row in csv_data:
                    self.opdata.append(row)
                    self.data.append(row)
        except OSError:
            print('Cannot open', filepath)
        text_data.close()
        pass

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name,row))
        return objects