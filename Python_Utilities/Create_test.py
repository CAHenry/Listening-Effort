import Test_classes as le


babble_front = le.MaskingCondition("Babble_front", 1)
babble_front.set_source_positions([1, 0])
babble_front.set_audio_files("Babble_1.wav")
babble_front.set_video("one_in_front.mp4")

babble_behind = le.MaskingCondition("Babble_behind", 2)
babble_behind.set_source_positions([[1, 135], [1, 225]])
babble_behind.set_audio_files(["Babble_1.wav", "Babble_2.wav"])
babble_behind.set_video("two_behind.mp4")


around = le.MaskingCondition("around", 4)
around.set_source_positions([[1, 45], [1, 135], [1, 225], [1, 315]])
around.set_audio_files(["Babble_1.wav", "Babble_2.wav", "Babble_3.wav", "Babble_4.wav"])
around.set_video("four.mp4")

babble_front_2_TC = le.TestCondition(babble_front, 2)
babble_front_2_TC.description = "One babble source directly in front of the participant"
babble_behind_1_TC = le.TestCondition(babble_behind, 1)
babble_behind_1_TC.description = "Two babble sources at 135 and 225 degrees"
around_3_TC = le.TestCondition(around, 3)
around_3_TC.description = "Four babble sources at 45, 135, 225 and 315 degrees"


test_one = le.Test("Example test", [babble_behind_1_TC, around_3_TC, babble_front_2_TC])
test_one.output("..\\XMLs", "Babble_front_2", "..\\Max\\ASLQ_Matt") 