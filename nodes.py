from direct3d_s2.pipeline import Direct3DS2Pipeline


class LoadDirect3DS2Model:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_path": ("STRING", {"default": "wushuang98/Direct3D-S2"}),
                "subfolder_path": ("STRING", {"default": "direct3d-s2-v-1-1"}),
                "device": ("STRING", {"default": "cuda"})
            }
        }

    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "load_model"
    CATEGORY = "Direct3D‑S2"

    def load_model(self, model_path, subfolder_path, device):
        pipeline = Direct3DS2Pipeline.from_pretrained(
          model_path, 
          subfolder=subfolder_path
        )
        pipeline.to(device)
        model = pipeline
        
        return (model,)


class LoadDirect3DS2Image:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image_path": ("STRING", {"default": "assets/test/13.png"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "input_image"
    CATEGORY = "Direct3D‑S2"

    def input_image(self, image_path):
        image = image_path
        return (image,)





mesh = pipeline(
  'assets/test/13.png', 
  sdf_resolution=1024, # 512 or 1024
  remesh=False, # Switch to True if you need to reduce the number of triangles.
)["mesh"]

mesh.export('output.obj')
