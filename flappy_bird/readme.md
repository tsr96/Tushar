Flappy Bird AI — Reinforcement Learning Project
🎮 Overview
This project implements an AI agent that learns to play Flappy Bird using Q-Learning, a fundamental Reinforcement Learning (RL) algorithm.
The bird learns to flap at the right times to avoid pipes and maximize its score — completely autonomously.
The environment is built using Pygame, and training progress is visualized with Matplotlib.
🧠 Key Features
🕹️ Game Environment built from scratch using Pygame.
🧩 Q-Learning Algorithm to train the bird on when to jump or stay still.
🎨 Customizable Graphics: Easily replace bird, background, and pipe images.
📊 Training Visualization using Matplotlib (plots generation vs score).
🧮 Reward System:
+15 reward for surviving/passing a pipe
−1000 penalty for crashing