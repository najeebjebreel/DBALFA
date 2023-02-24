import torch
from torch.utils.data.dataloader import DataLoader 
import numpy as np

def get_features(model, dataset, device = 'cuda', layers = None):
    data_loader = DataLoader(dataset, batch_size = 128, shuffle = False)
    model.to(device)
    model.eval()
    ftrs_dict = None
    labels = None
    preds = None
    for batch_idx, (data, target) in enumerate(data_loader):
        data, target = data.to(device), target.to(device).long()

        output, ftrs = model(data.clone(), get_features = True)

        if labels is None:
            labels = target.cpu().view(-1).numpy()
        else:
            labels = np.concatenate((labels, target.cpu().view(-1).numpy()))

        L = layers
        if layers is None:
            L = np.arange(len(ftrs))
            
        if ftrs_dict is None:
            ftrs_dict = {l:None for l in L}
        for l in L:
                if ftrs_dict[l] is None:
                    ftrs_dict[l] = ftrs[l].cpu().numpy()
                else:
                    ftrs_dict[l]= np.vstack((ftrs_dict[l], ftrs[l].cpu().numpy()))

        pred = output.argmax(dim=1, keepdim=True) # get the index of the max log-probability
        if preds is None:
            preds = pred.cpu().view(-1).numpy()
        else:
            preds = np.concatenate((preds, pred.cpu().view(-1).numpy()))

    return  ftrs_dict, labels, preds
