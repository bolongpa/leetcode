# leetcode
problems without an official solution

Tasks remaining:
1.	Publication standard plots Final PR and ROC curves
2.	Publication standard plots Pr, Re and F1 scores vs epochs
3.	Publication standard plots Train and validate loss vs epochs
4.	Bolong: filter maps for DS3, CrackSegNet and Xincong 1 image data.
5.	Liu and Bolong: We need computational time or wall time or inference time or run time.
6.	*** Liu: All the details of architecture, methodology, hyperparameters used and any details for experimentation.
7.	*** Liu and Bolong: Write some paragraph for the other methods what we used.

FCN
We applied Fully Convolutional Network (FCN) on our datasets to examine to demonstrate our proposed model is dominating. When we doing experiments with FCN, we set 150 epochs for training process based on pretrained VGG19 parameters, and we altered the resizing method to nearest for consistency. 

FPHB
We also implemented the experiments with Feature Pyramid and Hierarchical Boosting Network (FPHB). We tried to train the models with 20k, 32k and 40k iterations, which are 90, 145 and 180 epochs equivalently. And as the performance illustrated in the original paper, it maintains the same when the iteration number is over 20 thousand. Finally we choose the model trained with 40k iterations for comparisons to other algorithms.
