# useful_snippets
## webp2mp4.py
将webp格式的动画文件，转换为mp4格式的视频
```bash
python webp2mp4.py input.webp output.mp4
```

## modelscope2comfyui.py
将魔搭平台训练的Z-Image-Turbo模型的LoRA，转换为ComfyUI兼容的LoRA
```bash
python modelscope2comfyui.py /path/to/input.safetensors [/path/to/input_comfyui.safetensors]
```

## show_shapes.py
获取使用convert_to_quant对模型进行int8量化时的`--convrot-group-size`参数(或直接尝试：4、8、16、64)
```bash
python show_shapes.py krea2_turbo_bf16.safetensors
```
量化命令参考：
```bash
ctq -i input_bf16.safetensors -o input_bf16_int8.safetensors --int8 --scaling_mode row --simple --low-memory --convrot --convrot-group-size 64 --comfy_quant --save-quant-metadata --qwen
```
