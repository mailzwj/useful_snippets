from safetensors import safe_open
import sys

total = len(sys.argv)
if (total < 2):
    print('input file is required')
    sys.exit(1)

input = sys.argv[1]

f = safe_open(input, framework='pt')
shapes = set()
[shapes.add(f.get_slice(k).get_shape()[-1]) for k in f.keys() if len(f.get_slice(k).get_shape()) == 2]
print(sorted(shapes))

"""
量化命令（pip install convert_to_quant）
ctq -i input_bf16.safetensors -o input_bf16_int8.safetensors --int8 --scaling_mode row --simple --low-memory --convrot --convrot-group-size 64 --comfy_quant --save-quant-metadata --qwen
"""
