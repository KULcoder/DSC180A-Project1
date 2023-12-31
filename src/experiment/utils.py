import torch

"""
Function:
    one_hot_encode
"""

def one_hot_encode(labels, num_classes):
    """
    One hot encode labels
    :param labels: labels to encode
    :param num_classes: number of classes
    :return: one hot encoded labels
    """
    batch_size = labels.size(0)
    one_hot = torch.zeros(batch_size, num_classes)
    one_hot[torch.arange(batch_size), labels] = 1
    return one_hot