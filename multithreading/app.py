import time
from tqdm import tqdm #barra de prograsso
from speeding_up import TrainModel, LoadData


# replace with train model - suppose it takes 3 seconds to train
def _trainModel():
  time.sleep(3)
  return# replace with load data function - suppose it takes 2 seconds to load


def _loadData():
  time.sleep(2)
  return



# assume we loop 10 times
epochs = 10

# without multithreading
# use with for tqdm to properly shut tqdm down if exception appears
# with tqdm(range(epochs)) as epochLoop:
#   for _ in epochLoop:
# 	# loadData
# 	_loadData()
	
# 	# trainModel
# 	_trainModel()



# with multithreading
# use with for tqdm to properly shut tqdm down if exception appears
with tqdm(range(epochs)) as epochLoop:
	for _ in epochLoop:
		# loadData
		loadThread = LoadData(None)
		loadThread.start()

		# trainModel
		trainThread = TrainModel(None)
		trainThread.start()

		# only continue if both threads are done
		modelLoss = trainThread.join()
		data = loadThread.join()