# assemble images grid
Code for assembling a grid of images in dzi format (deep zoom image support)

https://openseadragon.github.io/examples/tilesource-dzi/

## requirements 

the following libraries are required 

PIL
wget 
matplotlib
numpy


## usage 

On the site raremaps (or a site with dzi images), find the dzi repo for the image and update the url variable following the format : 
url = f"https://storage.googleapis.com/raremaps/img/dzi/img_61987_files/{zoom}/{x}_{y}.jpg"

Find realistic values for xmax and ymax (by looking in the dzi folder)

run the script 
