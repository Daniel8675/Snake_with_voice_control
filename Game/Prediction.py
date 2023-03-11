import os
import numpy as np

from tensorflow.keras import models
from Voice.recording_helper import *
from Voice.tf_helper import *

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

commands = ['down', 'go', 'left', 'no', 'right', 'stop', 'up', 'yes']

loaded_model = models.load_model("Game\snake_model")


def predict_mic():
    audio = record_audio()
    print("Dzwiek", audio)
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    print("Predicted label:", command)
    return command


def predict_mice_with_volume_activation(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > 10:
        print(int(volume_norm))
        command = predict_mic()
