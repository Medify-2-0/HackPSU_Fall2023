import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image  # Importing PIL from Pillow
import scipy.ndimage
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial import Delaunay

# Some constants
#################
#Change input directory
INPUT_FOLDER = 'testing_tumor/yes'
#################

patients = os.listdir(INPUT_FOLDER)
patients.sort()

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder, filename))
        img = np.asarray(img)


        if img is not None:
            images.append(img)
    return images

# Loading the first patient's scans
first_patient_pixels = np.stack('testing_tumor/yes/Y71.JPG')

# Show histogram
plt.hist(first_patient_pixels.flatten(), bins=80, color='c')
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()

# Show some slice in the middle
plt.imshow(first_patient_pixels[24], cmap=plt.cm.gray)
plt.show()

def resample(image, new_spacing=[1,1,1]):
    spacing = np.array([1, 1, 1])  # Assuming equal spacing in all dimensions for jpg
    resize_factor = spacing / new_spacing
    new_real_shape = image.shape * resize_factor
    new_shape = np.round(new_real_shape)
    real_resize_factor = new_shape / image.shape
    new_spacing = spacing / real_resize_factor
    image = scipy.ndimage.interpolation.zoom(image, real_resize_factor, mode='nearest')
    return image, new_spacing

pix_resampled, spacing = resample(first_patient_pixels, [1,1,1])
print("Shape before resampling\t", first_patient_pixels.shape)
print("Shape after resampling\t", pix_resampled.shape)

def plot_3d(image, threshold=-300):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
   
    verts = np.argwhere(image > threshold)
    tri = Delaunay(verts)
    ax.plot_trisurf(verts[:,0], verts[:,1], verts[:,2], triangles=tri.simplices, cmap='gray')
   
    ax.set_xlim(0, image.shape[0])
    ax.set_ylim(0, image.shape[1])
    ax.set_zlim