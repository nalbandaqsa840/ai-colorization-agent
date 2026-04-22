from dotenv import load_dotenv
load_dotenv()
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_agent(user_input):
    user_input = user_input.lower()

    # Model suggestion
    if "resnet" in user_input or "model" in user_input:
        return """
Recommended Model:
Use a ResNet-based encoder-decoder architecture.

Details:
- Encoder: Pretrained ResNet (ResNet18 or ResNet34)
- Decoder: Upsampling layers with skip connections
- Loss: L1 + Perceptual Loss
"""

    # Code generation
    elif "code" in user_input:
        return """
import torch
import torch.nn as nn

class ColorizationModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 64, 3, padding=1),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Conv2d(64, 3, 3, padding=1),
            nn.Tanh()
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x
"""

    # Hyperparameters
    elif "hyperparameter" in user_input:
        return """
Recommended Hyperparameters:
- Learning Rate: 0.0001
- Batch Size: 16
- Optimizer: Adam
- Epochs: 50-100
"""

    # Improvement suggestions
    elif "improve" in user_input or "accuracy" in user_input:
        return """
Ways to Improve Model:
- Use perceptual loss (VGG-based)
- Add data augmentation
- Increase dataset size
- Use GAN-based models
"""

    # Default response
    else:
        return """
Image colorization uses deep learning models like CNNs (U-Net, ResNet)
to convert grayscale images into color images.
"""


if __name__ == "__main__":
    print("🤖 AI Colorization Agent (Mock Version)")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Ask your AI Agent: ")

        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break

        output = run_agent(user_input)
        print("\nAgent:", output)
        print("-" * 50)