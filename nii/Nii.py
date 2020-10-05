import nibabel as nib
import numpy as np


class Nii:

    def __init__(self, path):
        self.path = path
        self.nii = nib.load(self.path)
        self.nii_np = np.array(self.nii.dataobj)

    def plot(self, index=0):
        pass

    def save(self, save_path):
        nii = nib.Nifti1Image(self.nii_np, affine=None)
        nib.save(nii, save_path)
