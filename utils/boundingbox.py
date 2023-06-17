import cv2


rectangles = []
current_rectangle = []
cropping = False

def click_and_crop(event, x, y, flags, param):
    global rectangles, cropping, current_rectangle

    if event == cv2.EVENT_LBUTTONDOWN:
        current_rectangle = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        current_rectangle.append((x, y))
        cropping = False

        cv2.rectangle(image, current_rectangle[0], current_rectangle[1], (0, 255, 0), 2)
        cv2.imshow("image", image)
        rectangles.append(tuple(current_rectangle))

image = cv2.imread("img/image.jpg")
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()

    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break

# close all open windows
cv2.destroyAllWindows()

for rect in rectangles:
    # print(f"Top left: {rect[0]}, Bottom right: {rect[1]}")
    print(f"<area shape=\"rect\" coords=\"{rect[0][0]},{rect[0][1]},{rect[1][0]},{rect[1][1]}\" alt=\"NAME\" href=\"faces/NAME.html\">")
