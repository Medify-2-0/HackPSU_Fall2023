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

def volume_rendering(slices):
    volume = slices_to_volume(slices)
    image_data = numpy_to_vtk(volume)
    
    # Create a color transfer function
    color_func = vtk.vtkColorTransferFunction()
    color_func.AddRGBPoint(10, 1.0, 0.356, 0.047)   # Low intensity
    color_func.AddRGBPoint(500, 0, 0.15, 0.21)  # High intensity

    # Create an opacity transfer function
    opacity_func = vtk.vtkPiecewiseFunction()
    opacity_func.AddPoint(10, 0.0)
    opacity_func.AddPoint(500, 1.0)
    
    # Volume renderer
    volume_renderer = vtk.vtkSmartVolumeMapper()

    volume_renderer.SetInputData(image_data)
    
    # The property describes how the data will look
    volume_property = vtk.vtkVolumeProperty()
    volume_property.SetColor(color_func)
    volume_property.SetScalarOpacity(opacity_func)
    
    # The volume holds the mapper and the property and
    # can be used to position/orient the volume
    volume_vtk = vtk.vtkVolume()
    volume_vtk.SetMapper(volume_renderer)
    volume_vtk.SetProperty(volume_property)

    ren = vtk.vtkRenderer()
    ren_win = vtk.vtkRenderWindow()
    ren_win.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)
    
    ren.AddVolume(volume_vtk)
    ren.SetBackground(1, 1, 1)
    ren_win.SetSize(800, 800)

    ren_win.Render()
    iren.Start()

if __name__ == "__main__":
    path = r"/Users/aviralbansal/Desktop/test/CTscanDataset" 
    slices = load_scan(path)
    volume_rendering(slices)
