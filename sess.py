import tensorflow as tf

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix1, matrix2)  # matrix multiply,矩阵乘法

# Session使用方法1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()

# Session使用方法2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
# 这种打开模式不需要再close了，他会自动close
