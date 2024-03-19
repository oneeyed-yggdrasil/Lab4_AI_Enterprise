import pickle
import os
path = os.getcwd()

def load_model():
  """Loads the model from the pk1 file."""
  with open("/home/rio/Test/AI_In_Enterprise/Lab_4/Lab4_AI_Enterprise/fish_weight_prediction_model.pkl", "rb") as f:
   model = pickle.load(f)

  return model


# Load the model and store it globally (not ideal for production)
loaded_model = load_model()
