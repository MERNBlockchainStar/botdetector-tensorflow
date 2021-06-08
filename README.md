# Botnet-Detection

<b> Dataset Used </b>

This project uses the CTU-13 dataset which involves 13 scenarios of lablled network traffic data with normal and botnet traffic. 


<b> Dependencies </b>

This project requires set of the following python modules:

1. scipy
2. numpy
3. theano
4. scikit-learn
5. keras
6. tensorflow

<b> training and testing, saving model </b>

To train the model, in the botdetector/src using the following commands

<b>     cd src<br>
        python gui_train.py</b>

in interface, select .binetfile. after that, click train button.
then,pickle file  been made in the pickle directory and saved model been made in the model directory.
!!!!!!!  binetfile must be in dataset/, i.e 1.binetflow for scenario_1, 2.binetflow for scenario_2 , ...

attack type | saved model numbers
 IRC        |  1,2,3,4,9,10,11
 spam       |  1,2,5,9,13
 cf         |  1,2,9
 ps         |  3,6,8,13
 us         |  3,4,10
 http       |  5,7,13
 ddos       |  4,10,11
 p2pbotnet  |  12

accuracy of models

acc_model = [95.74, 96.85, 97.79, 94, 95.69, 87.4, 99.69, 93.29, 94.99, 98.21, 99.9, 90.29, 94.5]

to test 