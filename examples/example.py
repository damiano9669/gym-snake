import time

import gym
import matplotlib.pyplot as plt
import numpy as np

env = gym.make('gym_snake:snake-v0',
               array_size=20, scale_factor=50)

print(f'{env.action_space = }')
print(f'{env.observation_space = }')

env.reset()
rewards = []

done = False
while not done:
    action = np.random.choice(env.snake.ACTIONS)
    print(f'{action = }')
    observation, reward, done, _ = env.step(action)
    print(f'{reward = } - {done = }')

    time.sleep(1)
    rewards.append(reward)
    print('-' * 50)

print(f'{reward = } - {done = }')

plt.plot(rewards)
plt.xlabel('Time')
plt.ylabel('Reward')
plt.title('Rewards')
plt.show()