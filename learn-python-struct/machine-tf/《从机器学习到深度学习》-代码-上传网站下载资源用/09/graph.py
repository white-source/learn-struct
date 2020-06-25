import tensorflow as tf

a = tf.constant(3.0, dtype=tf.float32, name="a")
b = tf.constant(4.0, name="b") 
total = a + b

print(a)
print(b)
print(total)

writer = tf.summary.FileWriter('./log/')
writer.add_graph(tf.get_default_graph())

writer.close()

sess = tf.Session()
print(sess.run(total))

sub = a - b
print(sess.run({"a+b":total, "a-b":sub}))


a = tf.constant(3.0, name="a")
x = tf.placeholder(tf.float32, name="x")
y = tf.placeholder(tf.float32, name="y")
z = a + x + y
print(sess.run(z, feed_dict={x: 3, y: 4.0}))
print(sess.run(z, {x: 5, y: 4.0}))



x = tf.placeholder(tf.float32, shape=[None, 3])
y = tf.layers.dense(x, units=1)

init = tf.global_variables_initializer()
sess.run(init)

# print(sess.run(y, feed_dict={x: [[[1, 1], [2, 2], [3, 3]], [[4, 4], [5, 5], [6, 6]]]}))

print(sess.run(y, feed_dict={x: [[1, 2, 3], [1, 2, 3]]}))








print("######################")

x = tf.placeholder(tf.float32, shape=[None, 2])
hidden =  tf.layers.dense(x, units=3, activation=tf.nn.sigmoid) 
y = tf.layers.dense(hidden, units=1)

y_true = tf.placeholder(tf.float32, shape=[None, 1])

loss = tf.losses.mean_squared_error(labels=y_true, predictions=y)

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)



init = tf.global_variables_initializer()

sess = tf.Session()

writer = tf.summary.FileWriter("./log/", sess.graph)

sess.run(init)


for i in range(2000):
  _, loss_value = sess.run((train, loss), {x: [[1, 1], [2, 2], [1, 2], [2, 1]], y_true:[[2.5,], [4,], [3, ], [3.5, ]]})
  # print(loss_value)

print(sess.run(y, feed_dict={x: [[1.5, 2]]}))

writer.close()
