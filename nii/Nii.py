import nibabel as nib


class Nii:

    def __init__(self, path):
        self.path = path
        self.nii = nib.load(self.path)

    def plot(self, index=0):
        pass

    def save(self, save_path):
        nib.save(self.nii, save_path)
