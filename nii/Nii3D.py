from .Nii import Nii

import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt


class Nii3D(Nii):
    def __init__(self, path):
        Nii.__init__(self, path)
        self.nii_np = np.transpose(np.array(self.nii.dataobj), axes=[2, 1, 0])
        self.shape = self.nii_np.shape

    def plot(self, index=0):
        plt.imshow(self.nii_np[index])
        plt.show()

    def save(self, save_path):
        nii = nib.Nifti1Image(np.transpose(self.nii_np, axes=[2, 1, 0]), affine=None)
        nib.save(nii, save_path)

