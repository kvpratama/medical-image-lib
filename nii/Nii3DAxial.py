from .Nii3D import Nii3D

import nibabel as nib
import numpy as np


class Nii3DAxial(Nii3D):
    def __init__(self, path):
        Nii3D.__init__(self, path)

        self.plane = 'axial'

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