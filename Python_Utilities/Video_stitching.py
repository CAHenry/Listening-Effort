from moviepy.editor import *

vid_one = VideoFileClip("C:\\Users\\craig\\Documents\\Videos\\two_in_front.mp4")
vid_two = VideoFileClip("C:\\Users\\craig\\Documents\\Videos\\one_infront_one_behind.mp4")

vid_one = vid_one.set_duration(240)
vid_two = vid_two.set_duration(240)

crop_vid_one = vid_one.crop(x1=0, y1=0, x2=vid_one.size[0]/4.0, y2=vid_one.size[1])
crop_vid_two = vid_two.crop(x1=vid_two.size[0]/4.0, y1=0, x2=vid_two.size[0]*3.0/4.0, y2=vid_two.size[1])
crop_vid_three = vid_one.crop(x1=vid_one.size[0]*3.0/4.0, y1=0, x2=vid_one.size[0], y2=vid_one.size[1])

vid_new = clips_array([[crop_vid_one, crop_vid_two, crop_vid_three]])

vid_new.write_videofile("C:\\Users\\craig\\Documents\\Videos\\one_in_front.mp4")
