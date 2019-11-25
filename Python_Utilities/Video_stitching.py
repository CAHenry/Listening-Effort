from moviepy.editor import *
import moviepy.video.fx.all as mp

vid_one = VideoFileClip("C:\\Users\\craig\\Documents\\Videos\\Condition_3.mp4")
vid_two = VideoFileClip("C:\\Users\\craig\\Documents\\Videos\\Condition_2.mp4")

vid_one = vid_one.set_duration(10)
vid_two = vid_two.set_duration(10)

vid_one = vid_one.crop(x1=0, y1=0, x2=1920, y2=1920)
vid_two = vid_two.crop(x1=1920, y1=0, x2=3840, y2=1920)

vid_three = clips_array([[vid_one, vid_two]])

vid_three.write_videofile("C:\\Users\\craig\\Documents\\Videos\\new.mp4")