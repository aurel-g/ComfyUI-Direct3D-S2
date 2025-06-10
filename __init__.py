from .nodes import LoadDirect3DS2Model, LoadDirect3DS2Image, Direct3DS2, SaveDirect3DS2Mesh

NODE_CLASS_MAPPINGS = {
    "LoadDirect3DS2Model": LoadDirect3DS2Model,
    "LoadDirect3DS2Image": LoadDirect3DS2Image,
    "Direct3DS2": Direct3DS2,
    "SaveDirect3DS2Mesh": SaveDirect3DS2Mesh,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadDirect3DS2Model": "Load Direct3D S2 Model",
    "LoadDirect3DS2Image": "Load Direct3D S2 Image",
    "Direct3DS2": "Direct3D S2",
    "SaveDirect3DS2Mesh": "Save Direct3D S2 Mesh",
} 

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
