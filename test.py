import tensorflow as tf;
def main():
    print("Hello World")
    print(tf.reduce_sum(tf.random.normal([360, 360])))
    addition(5,6)
def addition(a,b):
    c=a+b
    print(c)
if __name__=="__main__":
    main()
