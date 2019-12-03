import Test_classes as le


babble_front = le.MaskingCondition("Babble_front", 1)
babble_front.set_source_positions([1, 0])
babble_front.set_audio_files("Babble_1.wav")

babble_behind = le.MaskingCondition("Babble_behind", 1)
babble_behind.set_source_positions([1, 180])
babble_behind.set_audio_files("Babble_1.wav")

around = le.MaskingCondition("around", 4)
around.set_source_positions([[1, 0], [1, 90], [1, 180], [1, 270]])
around.set_audio_files(["Babble_1.wav", "Babble_2.wav", "Babble_3.wav", "Babble_4.wav"])

babble_front_2_TC = le.TestCondition(babble_front, 2)
babble_behind_1_TC = le.TestCondition(babble_behind, 1)
around_3_TC = le.TestCondition(around, 3)


test_one = le.Test([babble_behind_1_TC, around_3_TC, babble_front_2_TC])
test_one.output("..\\XMLs", "Babble_front_2", "..\\Max\\ASLQ_Matt") 