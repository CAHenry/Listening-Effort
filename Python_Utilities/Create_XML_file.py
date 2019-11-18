import os
import numpy as np


# Phi is the angle from the lateral plane, theta is the azimuth and anti-clockwise
def spherical_2_cartesian(r, phi, theta):
    theta = np.deg2rad(theta)
    phi = np.deg2rad(phi)

    x = r * np.cos(phi) * np.cos(theta)
    y = r * np.cos(phi) * np.sin(theta)
    z = r * np.sin(phi)

    return [x, y, z]

def write_source(file, num, pos, name, location, vol, vol_db, slider_pos=45, reverb_state="Off"):
    file.write("\t<Source%d_x>%.9f</Source%d_x>\n" % (num, pos[0], num))
    file.write("\t<Source%d_y>%.9f</Source%d_y>\n" % (num, pos[1], num))
    file.write("\t<Source%d_z>%.9f</Source%d_z>\n" % (num, pos[2], num))
    file.write("\t<Source%d_vol>%.9f</Source%d_vol>\n" % (num, vol, num))
    file.write("\t<Source%d_vol_dB>%.9f</Source%d_vol_dB>\n" % (num, vol_db, num))
    file.write("\t<Source%d_sliderPosition>%d</Source%d_sliderPosition>\n" % (num, slider_pos, num))
    file_path = location + "/" + name
    file.write("\t<Source_%d_filePath>%s</Source_%d_filePath>\n" % (num, file_path, num))
    # file.write("\t<Source_%d_reverb>%s</Source_%d_reverb>\n" % (num, reverb_state, num))
    # file.write("\t<Source_%d_NF>Off</Source_%d_NF>\n" % (num, num))
    # file.write("\t<Source_%d_FD>Off</Source_%d_FD>\n" % (num, num))


ASLQ_words = "C:\\Users\\craig\\Documents\\Listening-effort\\Max\\ASLQ"
Masking = "C:\\Users\\craig\\Documents\\Listening-effort\\Max\\Masking"

source_distance = 1

frame_size = 256
reverb_order = "3D"
gain = 0.5
num_sources = len(os.listdir(ASLQ_words)) + len(os.listdir(Masking))

xml_filename = "Separate_sources.xml"
xml = open(os.path.join("C:\\Users\\craig\\Documents\\Listening-effort\\XMLs", xml_filename), "w+")

xml.write("<BinauralApp>\n"
          "\t<FrameSize>%d</FrameSize>\n"
          "\t<ListenerPosX>0.000000000</ListenerPosX>\n"
          "\t<ListenerPosY>0.000000000</ListenerPosY>\n"
          "\t<ListenerPosZ>0.000000000</ListenerPosZ>\n"
          "\t<ListenerOrX>-0.000000000</ListenerOrX>\n"
          "\t<ListenerOrY>-0.000000000</ListenerOrY>\n"
          "\t<ListenerOrZ>0.000000000</ListenerOrZ>\n"
          "\t<ListenerOrW>1.000000000</ListenerOrW>\n"
          "\t<Platform>Windows</Platform>\n"
          "\t<OSCListenPort>12300</OSCListenPort>\n"
          "\t<ReverbOrder>%s</ReverbOrder>\n"
          "\t<NumSources>%d</NumSources>\n" % (frame_size, reverb_order, num_sources))

source = 0
for filename in os.listdir(Masking):
    cart = spherical_2_cartesian(source_distance, 0, 0)
    write_source(xml, source, cart, filename, "./../Max/Masking", gain * 0.501187, 20 * np.log10(gain * 0.501187), reverb_state="On")
    source += 1
    xml.write("\n")

for filename in os.listdir(ASLQ_words):
    cart = spherical_2_cartesian(source_distance, 0, 0)
    write_source(xml, source, cart, filename, "./../Max/ASLQ", gain, 20 * np.log10(gain), reverb_state="On")
    source += 1
    xml.write("\n")


xml.write("</BinauralApp>")
xml.close()
