# Data Science Accelerator Project
## Highways project

### Things to do

* Split videos into frames (or do we want a 5D tensor?)

It makes sense to run just the frames so that I can classify the images.

* Training set is the main set of data that we run the algorithm on.
* Test sets should reflect the data I want to do well on. (So critical road signage)
* Dev set is what you use to tune the parameters of the project, select features and other decisions regarding algorithm. (Hold-out cross validation set)

Tests should not just be 30% of the available data. Pick tests set that should teach want you ultimately want to perform well on.

Test set is dependent on the size of the examples as well. For instance 100 examples could be 30% split, but for 100,000 or millions it's not necessary.

* Establish a single-number evaluation metric (for a classifier that might be it's accuracy)

* Look at the images as where the signs are going to most likely feature in the image. (Are they likely to be on the left, and right more than centrally.

### Other areas of interest for the project.
* White line degradation
* Yellow line
* Bay areas (for instance disabled or parking bay lines)
* Carriage way width
* Street objects? (bollards, lighting)
* potholes
* kerb height? if kerb or path available?
* encroaching bushes or dangerous falling branches