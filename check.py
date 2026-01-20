import os

train_dir = "../dataset/train"

fresh_count = len(os.listdir(os.path.join(train_dir, "fresh")))
rotten_count = len(os.listdir(os.path.join(train_dir, "rotten")))

print("Fresh images :", fresh_count)
print("Rotten images:", rotten_count)
