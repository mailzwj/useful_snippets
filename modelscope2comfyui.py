"""
小脚本
将Modelscope训练的z-image-turbo模型的LoRA，转换为ComfyUI兼容的LoRA

python modelscope2comfyui /path/source.safetensors [/path/source_comfyui.safetensore]
"""
import sys
from safetensors.torch import load_file, save_file

argLength = len(sys.argv)

if (argLength < 2):
    print("Usage: python modelscope2comfyui.py <input_file> [<output_file>]")
    sys.exit(1)
elif (argLength == 2):
    input_file = sys.argv[1]
    output_file = input_file.replace(".safetensors", "_comfyui.safetensors")
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

print(f"Transform LoRA safetensors from {input_file}...")

tensors = load_file(input_file)
 
renamed_tensors = {}
for name, tensor in tensors.items():
    new_name = name
    new_name = new_name.replace("layers", "diffusion_model.layers")
    # new_name = "diffusion_model." + new_name
    new_name = new_name.replace(".default.", ".")
 
    renamed_tensors[new_name] = tensor
 
save_file(renamed_tensors, output_file)
print(f"Saved renamed LoRA safetensors to {output_file}")
