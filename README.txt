Run Model.py to run the Classification model. 

While the Python script is running, press q to kill it and close the model.

If the python script does not work install the libraries mentioned in requirements.txt

You can do so by opening a command promt with the location of this folder and entering the command ' pip install -r requirements.txt ' 

The Model.ipynb file is a Jupyter notebook that was used to construct the model.

The Model.h5 file is the AI model which was constructed by the Model.ipynb file and saved.

The 'Face-Mask-Detection' folder contains the databse which was used to train the Model.

The files need to be in the same directory to work.

You need to follow the circuit diagram attached in the form of a .pdf file to make connections to the arduino.

If you run it and the led doesn't light-up or there is a error say the port "COM3" does not exist then you need to edit the file with the name of the usb port used by the arduino.

Otherwise, you can run the non-arduino file.

The model was built with the help of the follwing libraries:

1. Tensorflow
2. Keras
3. Imutils
4. Numpy
5. Opencv
6. Matplotlib
7. Scipy
8. Pyfirmata
