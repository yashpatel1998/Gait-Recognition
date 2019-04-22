import cv2
import pickle
import random
import os

combined = []

X = []
Y = []

dictionary_angles = {
    "018_X": [], "036_X": [], "054_X": [], "072_X": [], "018_Y": [], "036_Y": [],
    "054_Y": [], "072_Y": [], "090_X": [], "108_X": [], "126_X": [], "144_X": [],
    "162_X": [], "180_X": [], "090_Y": [], "108_Y": [],"126_Y": [], "144_Y": [],
    "162_Y": [], "180_Y": [], "000_X": [], "000_Y": []
}

GEI_PATH = "D:\\MINOR_PROJECT\\Gait Recognition\\src\\gei"

print("Reading Images ...")

for l in os.listdir(GEI_PATH):
    print(l)
    image = cv2.imread(os.path.join(GEI_PATH,l))
    id = "{0:03}".format(int(l.split("-")[0]) + 1)
    angle = l.split("-")[3]
    if angle == "000":
        dictionary_angles[angle + "_X"].append(image)
        dictionary_angles[angle + "_Y"].append(id)
    elif angle == "018":
        dictionary_angles[angle + "_X"].append(image)
        dictionary_angles[angle + "_Y"].append(id)
    elif angle == "036":
        dictionary_angles[angle + "_X"].append(image)
        dictionary_angles[angle + "_Y"].append(id)
    elif angle == "054":
        dictionary_angles[angle + "_X"].append(image)
        dictionary_angles[angle + "_Y"].append(id)
    elif angle == "072":
        dictionary_angles[angle + "_X"].append(image)
        dictionary_angles[angle + "_Y"].append(id)
    elif angle == "090":
        dictionary_angles[angle + "_X"].append(image)
        dictionary_angles[angle + "_Y"].append(id)
    elif angle == "108":
        dictionary_angles[angle + "_X"].append(image)
        dictionary_angles[angle + "_Y"].append(id)
    elif angle == "126":
        dictionary_angles[angle + "_X"].append(image)
        dictionary_angles[angle + "_Y"].append(id)
    elif angle == "144":
        dictionary_angles[angle + "_X"].append(image)
        dictionary_angles[angle + "_Y"].append(id)
    elif angle == "162":
        dictionary_angles[angle + "_X"].append(image)
        dictionary_angles[angle + "_Y"].append(id)
    elif angle == "180":
        dictionary_angles[angle + "_X"].append(image)
        dictionary_angles[angle + "_Y"].append(id)


    # combined.append([image, id])

sum = 0
for i in dictionary_angles:
    sum += len(dictionary_angles[i])
    print(len(dictionary_angles[i]))
print(sum)

print("Shuffling the Data ...")
# random.shuffle(combined)

# for i in combined:
#     X.append(i[0])
#     Y.append(i[1])

# print(len(X))
# print(len(Y))

print("Generating Sweet Pickle ...")
with open('dictionary.pkl', 'wb') as f:
    pickle.dump(dictionary_angles, f)
    f.close()

# with open('Y.pkl', 'wb') as f:
#     pickle.dump(Y, f)
#     f.close()