import json

from model.dataset import Dataset
from model.models import BasicModel

model = BasicModel.compile(640, 480)

with open("manifest.json", "rb") as infile:
    manifest = json.loads(infile.read())
dataset = Dataset(manifest, "images/normalized")

train_img, train_label, test_img, test_label = dataset.load_data()
model.fit(train_img, train_label, batch_size=5, epochs=25, verbose=1)
loss, acc = model.evaluate(test_img, test_label, verbose=1)
print loss, acc
# model.save("out.m5")
