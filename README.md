# Defending Against Backdoor Attacks by Layer-wise Feature Analysis
This repository contains PyTorch implementation of the paper: Defending Against Backdoor Attacks by Layer-wise Feature Analysis that has been accepted to The Pacific-Asia Conference on Knowledge Discovery and Data Mining [(PAKDD 2023)](https://pakdd2023.org/).

## Paper 
[Defending Against Backdoor Attacks by Layer-wise Feature Analysis]()

## Content
The repository contains one jupyter notebook (`Ours_CIFAR10-ResNet18.IPYNB`) that contains code and instructions on how to re-produce the experiments reported in the paper for the benchmark under the Input-aware Dynamic backdoor attack (IAD). 
Also, models modified to extract intermediate features are available in the folder `my_models`.


## Datasets
[CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html) will be automatically downloaded.
However, [GTSRB](https://ieeexplore.ieee.org/document/6033395/) can be manually downloaded using this [link](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign/). 
After downloading [GTSRB](https://ieeexplore.ieee.org/document/6033395/), please save in the folder named 'data' with two subfolders each 'train' and 'test.


## Poisoned Datasets and Pretrained Attacked DNNs
Please download poisoned datasets via this link (https://www.dropbox.com/sh/02g7ys181u7yhlx/AABZSgKSYxgDF8DtystO31Sla?dl=0) and save them in the folder data/poisoned_testsets.
Also, please download pretrained attacked DNNs via this link (https://www.dropbox.com/sh/ilwdvone2fl5c2d/AADpmdjgKKq175Nj6Oj-bK8ma?dl=0) and save them in the folder checkpoints.
## Dependencies

Required packages and libraries are in `requirements.txt`


## Note
We will provide the remaining codes for reproducing our main experiments upon the acceptance of our paper.

