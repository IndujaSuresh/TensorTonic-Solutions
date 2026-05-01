import math
def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here
    total = 0
    length = len(predictions)
    for i in range(len(predictions)):
            if targets[i] == 1:
                pt = predictions[i]
            else:
                pt =1 - predictions[i]
            
            modulating = pow((1-pt),gamma)
            loss= alpha*-1 *(modulating)*(math.log(pt))
            total = total+loss
    loss_total = total/length
    return loss_total    

