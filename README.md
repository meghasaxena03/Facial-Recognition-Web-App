# Facial-Recognition-Web-App
Facial Recognition In a Web Application
What is facial recognition?

Facial recognition is a way of identifying or confirming an individual’s identity using their face. Facial recognition systems can be used to identify people in photos, videos, or in real-time. Facial recognition is a category of biometric security. Other forms of biometric software include voice recognition, fingerprint recognition, and eye retina or iris recognition. The technology is mostly used for security and law enforcement, though there is increasing interest in other areas of use.

How Does Facial Recognition work?

Many people are familiar with face recognition technology through the FaceID used to unlock iPhones (however, this is only one application of face recognition). Typically, facial recognition does not rely on a massive database of photos to determine an individual’s identity — it simply identifies and recognizes one person as the sole owner of the device, while limiting access to others.
Beyond unlocking phones, facial recognition works by matching the faces of people walking past special cameras, to images of people on a watch list. The watch lists can contain pictures of anyone, including people who are not suspected of any wrongdoing, and the images can come from anywhere — even from our social media accounts. Facial technology systems can vary, but in general, they tend to operate as follows:
Step 1: 
Face detection
The camera detects and locates the image of a face, either alone or in a crowd. The image may show the person looking straight ahead or in profile.
Step 2: 
Face analysis
Next, an image of the face is captured and analyzed. Most facial recognition technology relies on 2D rather than 3D images because it can more conveniently match a 2D image with public photos or those in a database. The software reads the geometry of your face. Key factors include the distance between your eyes, the depth 
of your eye sockets, the distance from forehead to chin, the shape of your cheekbones, and the contour of the lips, ears, and chin. The aim is to identify the facial landmarks that are key to distinguishing your face
.
Step 3: 
Converting the image to data
The face capture process transforms analog information (a face) into a set of digital information (data) based on the person's facial features. Your face's analysis is essentially turned into a mathematical formula. The numerical code is called a faceprint. In the same way that thumbprints are unique, each person has their own faceprint.
Step 4: 
Finding a match
Your faceprint is then compared against a database of other known faces. For example, the FBI has access to up to 650 million photos, drawn from various state databases. On Facebook, any photo tagged with a person’s name becomes a part of Facebook's database, which may also be used for facial recognition. If your faceprint matches an image in a facial recognition database, then a determination is made.
Of all the biometric measurements, facial recognition is considered the most natural. Intuitively, this makes sense, since we typically recognize ourselves and others by looking at faces, rather than thumbprints and irises. It is estimated that over half of the world's population is touched by facial recognition technology regularly.

Methodology
The project works using python library for face recognition and streamlit for the frontend. The application has some images given to the database (which is the images folder). These images are first converted to black and white and then comparison is made. When we show the camera our image, it will identify it according to the image saved in the database and give us the name associated with that image.
How to Install and Run the Project
We have to download and install python and some of pythons libraries like OpenCV, Face_recognition, numpy  and streamlit.
The code can easily be run in Visual Studios. Before running it, we have to type “streamlit run face.py” in the terminal. It will give us the local URL where our application will open. 
