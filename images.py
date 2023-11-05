# %%
import matplotlib.pyplot as plt
import wget
import numpy as np
from PIL import Image

# %%
# download images from raremaps.com
zoom = 14  # map zoom level
xmax = 38  # number of tiles in x (estimate)
ymax = 25  # number of tiles in y (estimate)

#  image download
for x in range(xmax):
    for y in range(ymax):
        try:
            url = f"https://storage.googleapis.com/raremaps/img/dzi/img_61987_files/{zoom}/{x}_{y}.jpg"
            file_name = wget.download(url)
        except:
            pass

# update actual xmax and ymax
xmax = x - 1
ymax = y - 1

# %%
# open all tiles in a list
images = [plt.imread(f"{x}_{y}.jpg") for x in range(xmax) for y in range(ymax)]

# concatenation of tiles into a single image
# first tile by tile (inner loop)
# then line by line (external loop)
grid = []
for x in range(xmax):
    tmp = []
    for y in range(ymax):
        tmp.append(plt.imread(f"{x}_{y}.jpg"))
    grid.append(np.concatenate(tmp))
imfinale = Image.fromarray(np.concatenate(grid, axis=1))

# image display in an interactive console
imfinale
# %%
# Save the image
imfinale.save("grid_image.jpg")

# %%
