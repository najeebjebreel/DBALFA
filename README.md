# DBALFA: Defending Against Backdoor Attacks by Layer-wise Feature Analysis

[![Paper](https://img.shields.io/badge/Paper-PAKDD%202023-blue)](https://arxiv.org/abs/2302.12758)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.anaconda.com/download)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.8%2B-orange)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> Official PyTorch implementation of the paper **"Defending Against Backdoor Attacks by Layer-wise Feature Analysis"**, accepted at the Pacific-Asia Conference on Knowledge Discovery and Data Mining [(PAKDD 2023)](https://pakdd2023.org/).

---

## Overview

**DBALFA** is a backdoor defense method that detects and mitigates backdoor attacks against deep neural networks by analyzing the layer-wise feature representations of benign and poisoned inputs. The method identifies anomalous activation patterns introduced by backdoor triggers across intermediate network layers, enabling robust detection without requiring access to the original clean training data.

This repository provides a reproducible implementation of the experiments reported in the paper for the CIFAR-10 benchmark under the **Input-aware Dynamic (IAD)** backdoor attack.

---

## Paper

**Defending Against Backdoor Attacks by Layer-wise Feature Analysis**
Najeeb M. Jebreel, Josep Domingo-Ferrer, Yuxuan Li
*Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD)*, pp. 428–440, Springer Nature Switzerland, 2023
🔗 [Read on arXiv](https://arxiv.org/abs/2302.12758)

---

## Repository Structure

```
DBALFA/
├── notebooks/                          # Jupyter notebooks for experiments
│   └── Ours_CIFAR10-ResNet18.ipynb     # Main experiment: CIFAR-10 / ResNet-18 / IAD attack
├── core/                               # Core framework (attacks, defenses, models, utils)
│   ├── attacks/                        # Backdoor attack implementations
│   │   ├── BadNets.py
│   │   ├── Blended.py
│   │   ├── IAD.py
│   │   ├── WaNet.py
│   │   └── ...                         # (additional attack implementations)
│   ├── defenses/                       # Baseline defense implementations
│   │   ├── ABL.py
│   │   ├── NAD.py
│   │   ├── Pruning.py
│   │   └── ...                         # (additional defense implementations)
│   ├── models/                         # Standard model architectures
│   │   ├── resnet.py
│   │   ├── vgg.py
│   │   ├── mobilenetv2.py
│   │   └── ...
│   └── utils/                          # Shared utilities (logging, metrics, adversarial tools)
├── my_models/                          # Feature-extracting model variants
│   ├── resnet.py                       # ResNet modified to return intermediate features
│   ├── vgg.py
│   ├── mobilenetv2.py
│   └── ...
├── data/                               # Dataset storage (see setup instructions below)
│   └── poisoned_testsets/              # Place downloaded poisoned test sets here
├── checkpoints/                        # Place downloaded pretrained attacked DNNs here
├── utils.py                            # Shared helper functions
├── requirements.txt
└── README.md
```

---

## Installation

### Prerequisites

| Dependency | Version |
|---|---|
| [Python](https://www.anaconda.com/download) | ≥ 3.8 |
| [PyTorch](https://pytorch.org/) | ≥ 1.8 |
| CUDA | ≥ 11.1 (recommended) |

### Setup

```bash
git clone https://github.com/najeebjebreel/DBALFA.git
cd DBALFA
pip install -r requirements.txt
```

---

## Datasets

| Dataset | Access | Notes |
|---|---|---|
| [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) | Automatic | Downloaded automatically via torchvision |
| [GTSRB](https://ieeexplore.ieee.org/document/6033395/) | Manual | See instructions below |

### GTSRB Manual Setup

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign/).
2. Extract and save it under `data/` with the following structure:

```
data/
├── train/
└── test/
```

---

## Poisoned Datasets & Pretrained Attacked DNNs

Pre-generated poisoned test sets and pretrained attacked DNNs are provided to allow direct reproduction of the paper's results without retraining from scratch.

1. Download **poisoned test sets** from [Dropbox](https://www.dropbox.com/sh/02g7ys181u7yhlx/AABZSgKSYxgDF8DtystO31Sla?dl=0) and save them to:

```
data/poisoned_testsets/
```

2. Download **pretrained attacked DNNs** from [Dropbox](https://www.dropbox.com/sh/ilwdvone2fl5c2d/AADpmdjgKKq175Nj6Oj-bK8ma?dl=0) and save them to:

```
checkpoints/
```

---

## Reproducing Experiments

Open the main notebook and follow the inline instructions:

```bash
jupyter notebook notebooks/Ours_CIFAR10-ResNet18.ipynb
```

The notebook walks through loading a pretrained attacked model, extracting layer-wise features from benign and poisoned inputs, applying the DBALFA defense, and evaluating detection performance.

---

## Citation

If you use this code or build upon this work, please cite:

```bibtex
@inproceedings{jebreel2023dbalfa,
  title     = {Defending Against Backdoor Attacks by Layer-wise Feature Analysis},
  author    = {Jebreel, Najeeb Moharram and Domingo-Ferrer, Josep and Li, Yuxuan},
  booktitle = {Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD)},
  pages     = {428--440},
  year      = {2023},
  publisher = {Springer Nature Switzerland}
}
```

---

## Acknowledgment

This research was funded by the European Commission (projects H2020-871042 "SoBigData++" and H2020-101006879 "MobiDataLab"), the Government of Catalonia (ICREA Acadèmia Prize to J. Domingo-Ferrer, grant no. 2021 SGR 00115, and FI_B00760 grant to N. Jebreel), and MCIN/AEI/10.13039/501100011033 and "ERDF A way of making Europe" under grant PID2021-123637NB-I00 "CURLING". The authors are with the UNESCO Chair in Data Privacy, but the views in this paper are their own and are not necessarily shared by UNESCO.

---

## Affiliation

Developed at the **[CRISES Research Group](https://crises-deim.urv.cat/)**, [Universitat Rovira i Virgili (URV)](https://www.urv.cat/en/), Tarragona, Catalonia.
