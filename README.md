# HornsOrNoHorns

![HA](https://github.com/VW-Stephen/HornsOrNoHorns/blob/master/haaaaa.png "Deergurl")
![LIT](https://github.com/VW-Stephen/HornsOrNoHorns/blob/master/tagger.png "Deerboi")

## Image normalization
Within a directory that contains copies of the raw images, run `mogrify -scale 'wXh!' -color Gray *` where
`w` and `h` are the desired dimensions to scale images.

## Basic Model
```python
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(IMG_HEIGHT, IMG_WIDTH, 1)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(
    loss="binary_crossentropy",
    optimizer="rmsprop",
    metrics=["accuracy"]
)
```

### 640x480 greyscale

| Image Count | Batch Size | Epochs | Loss | Accuracy |
|-------------|------------|--------|------|----------|
| 1,000 | 5 | 5 | 0.6040| 0.7475 |
| 1,000 | 5 | 10 | 0.7040 | 0.7025 |
| 1,000 | 5 | 15 | 0.8006 | 0.7525 |
| 1,000 | 5 | 20 | 1.1005 | 0.7225 |
| 1,000 | 5 | 25 | - | - |
||||||
| 2,000 | 15 | 5 | 0.5443 | 0.7425 |
| 2,000 | 15 | 10 | 0.9248 | 0.7250 |
| 2,000 | 15 | 15 | 1.3593 | 0.7175 |
| 2,000 | 15 | 20 | 1.5665 | 0.6950 |

### 640x480 greyscale, include mirrored images

| Image Count | Batch Size | Epochs | Loss | Accuracy |
|-------------|------------|--------|------|----------|
| 1,000 | 5 | 5 | -| - |
| 1,000 | 5 | 10 | - | - |
| 1,000 | 5 | 15 | - | - |
| 1,000 | 5 | 20 | - | - |
| 1,000 | 5 | 25 | - | - |
||||||
| 2,000 | 15 | 5 | - | - |
| 2,000 | 15 | 10 | - | - |
| 2,000 | 15 | 15 | - | - |
| 2,000 | 15 | 20 | - | - |
