def webp_to_mp4(webp_path, mp4_path, fps=30):
    # 打开WebP文件
    image = Image.open(webp_path)
    
    # 获取帧尺寸
    width, height = image.size
    
    # 创建视频写入对象
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(mp4_path, fourcc, fps, (width, height))
    
    # 遍历每一帧并写入视频
    try:
        while True:
            frame = np.array(image.convert('RGB'))
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            video.write(frame)
            image.seek(image.tell() + 1)
    except EOFError:
        pass
    
    # 释放资源
    video.release()

# 使用示例
# python webp2mp4.py input.webp output.mp4
total = len(sys.argv)
if (total < 2):
    print('input file is required')
    sys.exit(1)

input = sys.argv[1]
output = './output.mp4'
if (total > 2):
  output = sys.argv[2]
print('output:', output)
webp_to_mp4(input, output, fps=24)
