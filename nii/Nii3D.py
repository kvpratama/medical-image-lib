from .Nii import Nii

import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt


class Nii3D(Nii):
    def __init__(self, path, plane='axial'):
        Nii.__init__(self, path)
        self.nii_np = np.transpose(np.array(self.nii.dataobj), axes=[2, 1, 0])
        self.shape = self.nii_np.shape
        self.plane = plane

    def plot(self, index=0):
        plt.imshow(self.nii_np[index])
        plt.show()

    def to_axial(self):
        if self.plane == 'axial':
            print("current plane")
            pass
        elif self.plane == 'coronal':
            self.nii_np = np.transpose(self.nii_np, axes=[1, 0, 2])
        elif self.plane == 'sagittal':
            self.nii_np = np.transpose(self.nii_np, axes=[1, 2, 0])
        else:
            print('Unknown plane!')
            return

        self.plane = 'axial'
        self.shape = self.nii_np.shape

    def to_coronal(self):
        if self.plane == 'axial':
            self.nii_np = np.transpose(self.nii_np, axes=[1, 0, 2])
        elif self.plane == 'coronal':
            print("current plane")
            pass
        elif self.plane == 'sagittal':
            self.nii_np = np.transpose(self.nii_np, axes=[2, 1, 0])
        else:
            print('Unknown plane!')
            return

        self.plane = 'coronal'
        self.shape = self.nii_np.shape

    def to_sagittal(self):
        if self.plane == 'axial':
            self.nii_np = np.transpose(self.nii_np, axes=[2, 0, 1])
        elif self.plane == 'coronal':
            self.nii_np = np.transpose(self.nii_np, axes=[2, 1, 0])
        elif self.plane == 'sagittal':
            print("current plane")
            pass
        else:
            print('Unknown plane!')
            return

        self.plane = 'sagittal'
        self.shape = self.nii_np.shape

    def save(self, save_path):
        nii = nib.Nifti1Image(np.transpose(self.nii_np, axes=[2, 1, 0]), affine=None)
        nib.save(nii, save_path)

