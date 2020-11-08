import pandas as pd
class Trim:
    """Trim dataset by removing unwanted participants, trials, labels etc. """
    def __init__(self, dataset):
        self.dataset = dataset


    def del_participant(self, del_tr_indices, del_val_indices):
        if self.dataset == 'epix-kitchens-55':
            del_tr_indices = ['P'+str(idx).rjust(2,'0') for idx in del_tr_indices]
            del_val_indices = ['P'+str(idx).rjust(2,'0') for idx in del_val_indices]
            
            with open('../train_val/EPIC_train_action_labels.pkl', 'rb') as f:
                tr_labels = pickle.load(f)
                tr_label = tr_label[tr_label.participant_id.isin(del_tr_indices)]
                tr_label.to_pickle('../train_val/EPIC_valt_action_labels.pkl')

            with open('../train_val/EPIC_val_action_labels.pkl', 'rb') as f:
                val_labels = pickle.load(f)
                val_label = val_label[val_label.participant_id.isin(del_val_indices)]
                val_label.to_pickle('../train_val/EPIC_val_action_labels.pkl')

