from direct3d_s2.pipeline import Direct3DS2Pipeline



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



pipeline = Direct3DS2Pipeline.from_pretrained(
  'wushuang98/Direct3D-S2', 
  subfolder="direct3d-s2-v-1-1"
)
pipeline.to("cuda:0")

mesh = pipeline(
  'assets/test/13.png', 
  sdf_resolution=1024, # 512 or 1024
  remesh=False, # Switch to True if you need to reduce the number of triangles.
)["mesh"]

mesh.export('output.obj')
