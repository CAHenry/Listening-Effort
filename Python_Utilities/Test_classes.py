import numpy as np
import os

class Test:
    _test_conditions = []
    _title = ""
    _sentences = ""

    def __init__(self, title, test_conditions, sentences):
        self._title = title
        self._test_conditions.extend(test_conditions)
        self._sentences = sentences

    def add_condition(self, test_condition):
        self._test_conditions.extend(test_condition)

    def output(self, root, test_name, sentences):

        def write_source(file, num, pos, name, location, vol, vol_db, slider_pos=45):
            file.write("\t<Source%d_x>%.9f</Source%d_x>\n" % (num, pos[0], num))
            file.write("\t<Source%d_y>%.9f</Source%d_y>\n" % (num, pos[1], num))
            file.write("\t<Source%d_z>%.9f</Source%d_z>\n" % (num, 0, num))
            file.write("\t<Source%d_vol>%.9f</Source%d_vol>\n" % (num, vol, num))
            file.write("\t<Source%d_vol_dB>%.9f</Source%d_vol_dB>\n" % (num, vol_db, num))
            file.write("\t<Source%d_sliderPosition>%d</Source%d_sliderPosition>\n" % (num, slider_pos, num))
            file_path = location + "/" + name
            file.write("\t<Source_%d_filePath>%s</Source_%d_filePath>\n" % (num, file_path, num))
        xml_filename = test_name + ".xml"
        text_filename = test_name + ".txt"

        xml = open(os.path.join(root, xml_filename), "w+")
        text = open(os.path.join(root, text_filename), "w+")
        text_str = ""
        maskers = []
        files = []
        positions = []
        source_count = 0
        line_count = 2
        for condition in self._test_conditions:
            masker = condition.masking_condition
            num_sources = masker.get_num_sources()

            if masker.name not in maskers:
                maskers.append(masker.name)
                files.extend(masker.get_audio_files())
                positions.extend(masker.get_source_positions())
                masker.source_index = source_count
                source_count += num_sources
            screen_positions = [screen.position for screen in condition.screens]
            screen_idling = [screen.idle for screen in condition.screens]

            text_str += "%i %s \"%s\" %i %i %s %i \r" % (line_count, masker.name, condition.description, masker.source_index, num_sources, masker.get_video(), len(condition.screen))

            line_count += 1

        num_maskers = source_count
        source_count += len(os.listdir(sentences))
        text.write("1 %i %i %i \"%s\" \"%s\"\r" % (source_count, num_maskers, len(self._test_conditions), self._title, self._sentences))
        text.write(text_str)
        text.close()

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
                  "\t<NumSources>%d</NumSources>\n" % (256, "3D", source_count))
        source = 0

        gain = 1
        for i, filename in enumerate(files):
            x, y = positions[i]

            cart = spherical_2_cartesian(1, x, y)
            write_source(xml, source, cart, filename, "./../Media/Masking", gain,
                         20 * np.log10(gain))
            source += 1
            xml.write("\n")

        for filename in os.listdir(sentences):
            cart = spherical_2_cartesian(1, 0, 0)
            write_source(xml, source, cart, filename, sentences, gain, 20 * np.log10(gain))
            source += 1
            xml.write("\n")

        xml.write("</BinauralApp>")
        xml.close()


class TestCondition:
    masking_condition = 0
    screens = []
    description = ""

    def __init__(self, masking_condition, screens):
        self.masking_condition = masking_condition
        self.screens = screens


class Screen:
    position = []
    idle = ""


class MaskingCondition:
    _num_sources = 0
    _sources = 0
    _files = []
    _video = ""
    source_index = []
    name = ""

    def __init__(self, name,  num_sources):
        self.name = name
        self._num_sources = num_sources
        self._sources = np.zeros((num_sources, 2))
        self._files = ["" for _ in range(num_sources)]


    def get_num_sources(self):
        return self._num_sources

    def set_source_positions(self, positions):
        if self._num_sources == 1:
            positions = [positions]
        if len(positions) != self._num_sources:
            print("Number of positions does not match the number of sources")
            return

        for i, position in enumerate(positions):
            self._sources[i] = position

    def get_source_positions(self):
        return self._sources

    def set_audio_files(self, files):
        if type(files) is str:
            files = [files]
        for i in range(self._num_sources):
            if len(files) == 1:
                self._files[i] = files[0]
            else:
                self._files[i] = files[i]

    def get_audio_files(self):
        return self._files

    def set_video(self, video):
        self._video = video

    def get_video(self):
        return self._video


# Phi is the angle from the lateral plane, theta is the azimuth and anti-clockwise
def spherical_2_cartesian(r, phi, theta):
    theta = np.deg2rad(theta)
    phi = np.deg2rad(phi)

    x = r * np.cos(phi) * np.cos(theta)
    y = r * np.cos(phi) * np.sin(theta)
    z = r * np.sin(phi)

    return [x, y, z]




