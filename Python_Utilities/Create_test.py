import Test_classes as le
import os

male_babble = os.listdir("C:\\Users\\craig\\Documents\\Listening-Effort\\Media\\Masking\\male_babble")
female_babble = os.listdir("C:\\Users\\craig\\Documents\\Listening-Effort\\Media\\Masking\\male_babble")

idling = ["Idling/test.mp4"] * 3
screens = le.Screens("C:\\Users\\craig\\Documents\\Listening-Effort\\Test_Files\\positions.txt", idling)

babble_front = le.MaskingCondition("Babble_front", 2)
babble_front.set_source_positions([[1, 0], [1, 0]])
babble_front.set_audio_files([male_babble.pop(), female_babble.pop()])
babble_front.set_video("one_in_front.mp4")

babble_behind = le.MaskingCondition("Babble_behind", 4)
babble_behind.set_source_positions([[1, 135], [1, 135], [1, 225], [1, 225]])
babble_behind.set_audio_files([male_babble.pop(), female_babble.pop(), male_babble.pop(), female_babble.pop()])
babble_behind.set_video("two_behind.mp4")


around = le.MaskingCondition("around", 8)
around.set_source_positions([[1, 45], [1, 45], [1, 135], [1, 135], [1, 225], [1, 225], [1, 315], [1, 315]])
around.set_audio_files([male_babble.pop(), female_babble.pop(), male_babble.pop(), female_babble.pop(), male_babble.pop(), female_babble.pop(), male_babble.pop(), female_babble.pop()])
around.set_video("all_around.mp4")

babble_front_2_TC = le.TestCondition(babble_front, 2, screens)
babble_front_2_TC.description = "One babble source directly in front of the participant. Screen in front."
babble_behind_1_TC = le.TestCondition(babble_behind, 1, screens)
babble_behind_1_TC.description = "Two babble sources at 135 and 225 degrees. Screen to the left."
around_3_TC = le.TestCondition(around, 3, screens)
around_3_TC.description = "Four babble sources at 45, 135, 225 and 315 degrees. Screen to the right."


test_one = le.Test("Example test", [babble_behind_1_TC, around_3_TC, babble_front_2_TC], "BKBQwords_new.txt")
test_one.output("..\\Test_Files", "Example_test", "./../Media/BKB")

# babble_front = le.MaskingCondition("Babble_front", 1)
# babble_front.set_source_positions([1, 0])
# babble_front.set_audio_files("Babble_1.wav")
# babble_front.set_video("one_in_front.mp4")
#
# bf_left = le.TestCondition(babble_front, 1)
# bf_left.description = "One babble source directly in front of the participant, screen to the left"
# bf_right = le.TestCondition(babble_front, 3)
# bf_right.description = "One babble source directly in front of the participant, screen to the right"
#
# test_one = le.Test("Example test", [bf_left, bf_right, bf_left, bf_right])
# test_one.output("..\\XMLs", "debugging", "..\\Max\\ASLQ_Matt")
