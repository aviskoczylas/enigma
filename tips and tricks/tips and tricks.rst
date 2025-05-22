===================================
tchgraphs code documentation
===================================

Authors: 
    Avi Skoczylas and Maddy Deming

This document will explain how the code works and what it is doing, step by step.

Until line 44 we are simply converting h5 data to numpy arrays like in the other files. For details, see juno_data_processing code documentation.

We are only interested in datawithin certain longitudes, so next we define those longitudes. 

We then name and mask the boundary ellipse data as detailed in boresight_images code documentation. 

We calculate the boresight latitude and longitude by once again taking the average value of each ellipse boundary point's latitude and longitude. We store these in a list
for later use, but we convert to numpy so we are able to use numpy operations for distance calculation later. Optionally, we may plot the boresights here to better 
understand our data set. 

 We'll be using images from channel 6 to demonstrate.

.. figure:: placeholder.png
    :align: center
