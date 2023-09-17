import face_recognition
from PIL import Image, ImageDraw

def face_rec():
    jordan_face_img = face_recognition.load_image_file("img/jordan_m.webp")
    jordan_face_location = face_recognition.face_locations(jordan_face_img)

    bulls_img = face_recognition.load_image_file("img/bulls.jpg")
    bulls_faces_locations = face_recognition.face_locations(bulls_img)

    lakers_img = face_recognition.load_image_file("img/lakers.webp")
    lakers_faces_locations = face_recognition.face_locations(lakers_img)

    print(jordan_face_location)
    print(f"Found {len(jordan_face_location)} face(s) in this image")
    print(bulls_faces_locations)
    print(f"Found {len(bulls_faces_locations)} face(s) in this image")
    print(lakers_faces_locations)
    print(f"Found {len(lakers_faces_locations)} face(s) in this image")

    pil_img1 = Image.fromarray(jordan_face_img)
    draw1 = ImageDraw.Draw(pil_img1)

    for(top, right, bottom, left) in jordan_face_location:
        draw1.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

    del draw1
    pil_img1.save("img/new_jordan.webp")

    pil_img2 = Image.fromarray(bulls_img)
    draw2 = ImageDraw.Draw(pil_img2)

    for(top, right, bottom, left) in bulls_faces_locations:
        draw2.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

    del draw2
    pil_img2.save("img/new_bulls.webp")

    pil_img3 = Image.fromarray(lakers_img)
    draw3 = ImageDraw.Draw(pil_img3)

    for(top, right, bottom, left) in lakers_faces_locations:
        draw3.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

    del draw3
    pil_img3.save("img/new_lakers.webp")

def extracting_faces(img_path):
    count = 0
    faces = face_recognition.load_image_file(img_path)
    faces_locations = face_recognition.face_locations(faces)

    for face_location in faces_locations:
      top, right, bottom, left = face_location

      face_img = faces[top:bottom, left:right]
      pil_img = Image.fromarray(face_img)
      pil_img.save(f"img/faces/{count}_face_img.webp")
      count += 1

    return f"Found {count} face(s) in this photo"

def main():
    # face_rec()
    print(extracting_faces("img/lakers.webp"))

if __name__ == '__main__':
    main()
