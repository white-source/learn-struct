import gym
import numpy as np
import time

env = gym.make('FrozenLake-v0')


Q = np.zeros([env.observation_space.n,env.action_space.n])
lr = .5
y = .95

success = 0
for i_episode in range(500000):
    s = env.reset()
    for t in range(10000):
        print(chr(27) + "[2J")
        env.render()
        # time.sleep(5)
        print("episode: ", i_episode)
        print("success: ", success)
        print("rate: {:.2f}%".format(success/max(1, i_episode)*100,))
        print(s)
        #action = env.action_space.sample()
        a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*max((1./(i_episode+1)), 0.01))
        s1, r, d, info = env.step(a)
        Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a])
        s = s1
        print(s1)
        if d == True:
            if r >0.5:
                success += 1
            break
        
