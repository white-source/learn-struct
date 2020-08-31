import time
import gym
env = gym.make('CartPole-v0')
env.reset()
env.render()
done = False
while not done:
    observation, reward, done, info  = env.step(env.action_space.sample()) # take a random action
    env.render()
