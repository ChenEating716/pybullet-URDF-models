'''
Author: Yiting CHEN
Date: 2021-10-22 01:15:14
LastEditTime: 2021-10-22 09:54:18
contact me through chenyiting716@gmail.com
'''

import os
import random


class model_list(object):
    def __init__(self):
        self._model_path_list = []
        self._model_name_list = []
        self._model = {}
        self.dir = 'models'

        self.detect_models()
        self.load_data()

    def detect_models(self):
        filelist = os.listdir(self.dir)
        for i in range(0, len(filelist)):
            file_name = filelist[i]
            self._model_name_list.append(file_name)
            path = os.path.join(self.dir, file_name, 'model.urdf')
            if os.path.isfile(path):
                self._model_path_list.append(os.path.realpath(path))

    def load_data(self):
        if self._model_name_list and self._model_path_list:
            for model_name, model_path in zip(self._model_name_list, self._model_path_list):
                self._model[model_name]=model_path

    @property
    def random(self):
        """
        return: return the absolute path of random model
        """
        num = len(self._model_name_list)
        random_name = self._model_name_list[random.randint(0, num)]
        print("model {} is selected".format(random_name))
        
        return self._model[random_name]

    @property
    def model_path_list(self):
        return self._model_path_list

    @property
    def model_name_list(self):
        return self._model_name_list

    @property
    def available_models(self):
        return self._model

    def __getitem__(self, item):
        return self._model[item]


# test
if __name__ == "__main__":
    model = model_list()
    print(model.model_name_list[10])
    print(model.random)
    print(model['pen_container_1'])
