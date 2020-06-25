import tensorflow as tf


x = tf.placeholder(tf.float32, shape=[None, 2], name="input_layer")
layer1 = tf.layers.Dense(units=3, activation=tf.nn.sigmoid, name="hidden_layer")
hidden = layer1(x)
# hidden =  tf.layers.dense(x, units=3, activation=tf.nn.sigmoid, name="hidden_layer") 
y = tf.layers.dense(hidden, units=1, name="output_layer")

y_true = tf.placeholder(tf.float32, shape=[None, 1], name="y_true")

loss = tf.losses.mean_squared_error(labels=y_true, predictions=y)

optimizer = tf.train.GradientDescentOptimizer(0.01, name = "optimizer")
train = optimizer.minimize(loss, name="min_loss")


init = tf.global_variables_initializer()

with tf.Session() as sess:
  writer = tf.summary.FileWriter("./log/", sess.graph)


summary_loss = tf.summary.scalar('loss', loss)
summary_bias = tf.summary.histogram('hidden_bias', layer1.variables[1])

summary_merged = tf.summary.merge_all()
sess.run(init)


for i in range(2000):
  _, s_loss, s_bias, s_merged = sess.run((train, summary_loss, summary_bias, summary_merged), {x: [[1, 1], [2, 2], [1, 2], [2, 1]], y_true:[[2.5,], [4,], [3, ], [3.5, ]]})
  # tf.summary.histogram("normal/moving_mean", mean_moving_normal)
  # print(loss_value)
  #writer.add_summary(s_loss, global_step=i)
  #writer.add_summary(s_bias, global_step=i)
  writer.add_summary(s_merged, global_step=i)

print(sess.run(y, feed_dict={x: [[1.5, 2]]}))


writer.close()
