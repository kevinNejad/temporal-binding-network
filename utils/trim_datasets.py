class Trim:
    """Trim dataset by removing unwanted participants, trials, labels etc. """
    def __init__(self, dataset):
        self.dataset = dataset

    def del_participant(self, del_indices):
        if self.dataset == 'epix-kitchens-55':
            with open('../train_val/EPIC_train_action_labels.pkl', 'rb') as f:
                tr_labels = pickle.load(f)

            with open('../train_val/EPIC_val_action_labels.pkl', 'rb') as f:
                val_labels = pickle.load(f)


