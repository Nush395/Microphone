import unittest
import transcribe


class MyTestCase(unittest.TestCase):

    def test_transcribe_audio(self):
        output_text = transcribe.transcribe_audio("testaudio.mp3", model_name="tiny")
        print(output_text)


if __name__ == '__main__':
    unittest.main()
