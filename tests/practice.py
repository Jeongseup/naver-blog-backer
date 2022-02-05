from tqdm import tqdm
from time import sleep


pbar = tqdm(["a", "b", "c", "d"])

for char in pbar:
	sleep(0.25)

	pbar.set_description(" Processing")




