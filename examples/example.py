import time

import gym
import matplotlib.pyplot as plt
import numpy as np

env = gym.make('gym_snake:snake-v0',
               array_size=20, render_scale_factor=50)

print(f'{env.action_space = }')
print(f'{env.observation_space = }')
print(f'{env.get_available_actions() = }')

env.reset()
rewards = []

done = False
while not done:
    action = np.random.choice(env.get_available_actions())
    print(f'{action = }')
    observation, reward, done, _ = env.step(action)
    print(f'{observation = }')
    print(f'{reward = } - {done = }')

    time.sleep(0.1)
    rewards.append(reward)
    env.render()
    print('-' * 50)

print(f'{reward = } - {done = }')

plt.plot(rewards)
plt.xlabel('Time')
plt.ylabel('Reward')
plt.title('Rewards')
plt.show()
