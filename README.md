# Data Science Accelerator Project
## Highways project

### Things to do

* ~~Split videos into frames (or do we want a 5D tensor?)~~ 
139.59GB on disk, 391,902 frames.

By week 3 (16 August 2018) - have it so that I've done chapter 5 of the book and trained using ImageNet minimum.

* Read up on YOLO and ImageNet models so that I can use a pretrained convnet.
* The purpose of this is to do object detection ran than image classification (therefore it is worth doing focusing on detecting objects.)
* Look into caffe (pretrained models)
* 10 training images could potentially be enough to do this.
* 'Transfer learning' problem so retrain the last few layers of the model.
* Yolo has the weights straight from them. (Possily yolo3)
* Improve the bounding boxes so that they'll be better at predicting (possibly use the german taste set??)

* Make use of the yolo, command to run
python yolo_video.py --input="A38_NB_YR2_R09_180519132259.avi" --output='output'



* It might be necessary to run 100 objects to begin with and creating these things manually

* ~~Spend 30 minutes on looking for a front-end solution that could potentially help with classifying the training set more quickly.~~ Tool being used labelImg working, not hierarchical though currently.

It makes sense to run just the frames so that I can classify the images.

* Training set is the main set of data that we run the algorithm on.
* Test sets should reflect the data I want to do well on. (So critical road signage)
* Dev set is what you use to tune the parameters of the project, select features and other decisions regarding algorithm. (Hold-out cross validation set)

Tests should not just be 30% of the available data. Pick tests set that should teach want you ultimately want to perform well on.

Test set is dependent on the size of the examples as well. For instance 100 examples could be 30% split, but for 100,000 or millions it's not necessary.

* Establish a single-number evaluation metric (for a classifier that might be it's accuracy)

* Look at the images as where the signs are going to most likely feature in the image. (Are they likely to be on the left, and right more than centrally.

## Questions for Liucija
* ~~Should the dataset contain the rear of signs, so it picks up the right one.~~ -- don't worry about it just yet!
* If we were capturing all signs, should the first layers of the model be capturing shapes and train it for shapes?
    * Triangle
    * Square
    * Circle
    * Rectangle
* Then train a new layer for 
    * Informational?
    * Warning signs etc
* Maybe not for now but for different iteration.



### Other areas of interest for the project.
* White line degradation
* Yellow line
* Bay areas (for instance disabled or parking bay lines)
* Carriage way width
* Street objects? (bollards, lighting)
* potholes
* kerb height? if kerb or path available?
* encroaching bushes or dangerous falling branches