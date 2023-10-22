import os
import pydicom
import vtk
from vtk.util import numpy_support
import numpy as np

def load_scan(path):
    slices = [pydicom.dcmread(os.path.join(path, s)) for s in os.listdir(path)]
    slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))
    return slices

def slices_to_volume(slices):
    volume = np.stack([s.pixel_array for s in slices])
    return volume

def numpy_to_vtk(volume):
    vtk_data = numpy_support.numpy_to_vtk(volume.ravel(), deep=True, array_type=vtk.VTK_INT)
    img_data = vtk.vtkImageData()
    img_data.SetDimensions(volume.shape[2], volume.shape[1], volume.shape[0])
    img_data.GetPointData().SetScalars(vtk_data)
    return img_data

def generate_3d_model(slices):
    volume = slices_to_volume(slices)
    image_data = numpy_to_vtk(volume)
    
    # Use marching cubes algorithm
    dmc = vtk.vtkDiscreteMarchingCubes()
    dmc.SetInputData(image_data)
    dmc.GenerateValues(500, 10, 500)  # Adjusted values based on the visualization
    
    # Smoothing
    smoother = vtk.vtkSmoothPolyDataFilter()
    smoother.SetInputConnection(dmc.GetOutputPort())
    smoother.SetNumberOfIterations(10)  # Increased iterations for smoother output 3
    smoother.Update()
    
    # Create a mapper using the smoothed output
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(smoother.GetOutputPort())
    
    # Create an actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetOpacity(1)  # Adjusted opacity 0.7

    ren = vtk.vtkRenderer()
    ren.SetBackground(1, 1, 1)  # Set to white

    ren_win = vtk.vtkRenderWindow()
    ren_win.AddRenderer(ren)

    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    # Lighting
    light = vtk.vtkLight()
    light.SetFocalPoint(0, 0, 0)
    light.SetPosition(5, 5, 5)#10,10,10
    ren.AddLight(light)
    
    ren.AddActor(actor)
    ren_win.SetSize(800, 800)

    ren_win.Render()
    iren.Start()

if __name__ == "__main__":
    path = r"C:\Users\ekans\Desktop\datavis" #C:\Users\ekans\Desktop\files\cancer C:\Users\ekans\Desktop\Dataset\files\files\broken_ribs # C:\Users\ekans\Desktop\files\cancer
    slices = load_scan(path)
    generate_3d_model(slices)