import face_recognition
from PIL import Image, ImageDraw


pic_path = "6.png"
image = face_recognition.load_image_file(pic_path)
face_landmarks_list = face_recognition.face_landmarks(image)
print("我发现了{}张人脸在这张照片中".format(len(face_landmarks_list)))
pil_image = Image.open(pic_path)
for face_landmarks in face_landmarks_list:
    demo = ImageDraw.Draw(pil_image, 'RGBA')
    demo.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    demo.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    demo.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    demo.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    demo.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
    demo.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))
    pil_image.save("faceDraw.jpg")
    pil_image.show()