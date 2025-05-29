import unittest
from microphone import transcribe
import os


class MyTestCase(unittest.TestCase):

    def test_transcribe_audio(self):
        current_dir = os.getcwd()
        test_audio_path = os.path.join(current_dir, "testaudio.mp3")
        print(test_audio_path)
        output_text = transcribe.transcribe_audio(test_audio_path, model_name="tiny")
        print(output_text)


if __name__ == '__main__':
    unittest.main()
