import threading
import time

class TrainModel (threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data
        self._return = None


    def _trainModel(self):
        time.sleep(3)
        return
    

    def run(self):
        # return model loss
        self._return = self._trainModel()    
    

    def join(self):
        threading.Thread.join(self)
        return self._return




class LoadData (threading.Thread):
    def __init__(self, filenames):
        threading.Thread.__init__(self)
        self.filenames = filenames
        self._return = None


    def _loadData(self):
      time.sleep(2)
      return


    def run(self):        
        # return data
        self._return = self._loadData()


    def join(self):
        threading.Thread.join(self)
        return self._return