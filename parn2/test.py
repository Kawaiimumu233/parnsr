def cutVideo(path,filename):
    video_full_path = path + r'\\' +filename
    video_full_path_new = path + r'\\' +'new_'+filename
    cap = cv2.VideoCapture(video_full_path)
    cap.isOpened()
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
    print(width, height)
 
    if cap.isOpened():  # 当成功打开视频时cap.isOpened()返回True,否则返回False
        # get方法参数按顺序对应下表（从0开始编号)
        rate = cap.get(5)  # 帧速率
        FrameNumber = int(cap.get(7))  # 视频文件的帧数
        duration = FrameNumber / rate  # 帧速率/视频总帧数 是时间，除以60之后单位是分钟
        len = int(duration)
        fps = int(rate)
        print(rate, FrameNumber)
 
        if (width > height):
 
            for i in range(0,len):
                video_full_path_new = path + r'\\' + str(i) + filename
                print(i)
                cmd = 'ffmpeg -i {0} -vcodec libx264 -preset fast -b 10000k -ss 00:00:0{1} -to 00:00:0{2} {3} -y'.format(video_full_path,str(i),str(i+1),video_full_path_new)
                os.system(cmd)
 
        else:
            i = 0
            while (True):
                success, frame = cap.read()
                if success:
                    i += 1
                    # print('i = ', i)
                    if (i % fps == 1):
                        videoWriter = cv2.VideoWriter(path + '/' + str(i) + filename,
                                                      cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'), fps,
                                                      (int(width), int(height)))
                        videoWriter.write(frame)
                    else:
                        videoWriter.write(frame)
                else:
                    print('end')
                    break
 
 
 
    cap.release()
