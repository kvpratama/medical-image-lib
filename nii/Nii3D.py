from .Nii import Nii

import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt


class Nii3D(Nii):
    def __init__(self, path, orientation='axial'):
        Nii.__init__(self, path)

        self.orientation = orientation

        if self.orientation == 'axial':
            self.nii_np = np.transpose(self.nii_np, axes=[2, 1, 0])
        elif self.orientation == 'coronal':
            self.nii_np = np.transpose(self.nii_np, axes=[1, 2, 0])
        elif self.orientation == 'sagittal':
            self.nii_np = np.transpose(self.nii_np, axes=[0, 2, 1])
        else:
            print('Orientation {} is not supported. Using axial orientation.'.format(orientation))
            self.nii_np = np.transpose(self.nii_np, axes=[2, 1, 0])
            self.orientation == 'axial'

        self.shape = self.nii_np.shape

    def plot(self, index=0):
        plt.imshow(self.nii_np[index])
        plt.show()

    def save(self, save_path):
        if self.orientation == 'axial':
            nii = nib.Nifti1Image(np.transpose(self.nii_np, axes=[2, 1, 0]), affine=None)
        elif self.orientation == 'coronal':
            nii = nib.Nifti1Image(np.transpose(self.nii_np, axes=[2, 1, 0]), affine=None)
        elif self.orientation == 'sagittal':
            nii = nib.Nifti1Image(np.transpose(self.nii_np, axes=[2, 1, 0]), affine=None)

        nib.save(nii, save_path)

