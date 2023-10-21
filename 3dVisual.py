import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, morphology
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import imageio
import scipy.ndimage

# Some constants 

#################
INPUT_FOLDER = '../Desktop/HackPSUFall23/brain_tumor_dataaset/yes'
#################

patients = os.listdir(INPUT_FOLDER)
patients.sort()

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = imageio.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

# Loading the first patient's scans
first_patient_pixels = np.stack(load_images_from_folder(os.path.join(INPUT_FOLDER, patients[0])))

# Show histogram
plt.hist(first_patient_pixels.flatten(), bins=80, color='c')
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()

# Show some slice in the middle
plt.imshow(first_patient_pixels[80], cmap=plt.cm.gray)
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
    p = image.transpose(2,1,0)
    verts, faces = measure.marching_cubes(p, threshold)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    mesh = Poly3DCollection(verts[faces], alpha=0.70)
    face_color = [0.45, 0.45, 0.75]
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)
    ax.set_xlim(0, p.shape[0])
    ax.set_ylim(0, p.shape[1])
    ax.set_zlim(0, p.shape[2])
    plt.show()

plot_3d(pix_resampled, 100)  # Adjusted threshold as HU isn't applicable for JPG
