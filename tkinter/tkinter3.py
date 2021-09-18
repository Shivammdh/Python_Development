from tkinter import *
from PIL import Image, ImageTk


class Face_Recognition_System:
    def _init_(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # first image
        img = Image.open("BeautyPlus_20180921110134297_save.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoImage)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(r"C:\Users\Asus\Pictures\BeautyPlus_20180921110134297_save.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoImage1 = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoImage)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"C:\Users\Asus\Pictures\BeautyPlus_20180921110134297_save.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoImage2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoImage)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # bg image
        img3 = Image.open(r"C:\Users\Asus\Pictures\BeautyPlus_20180921110134297_save.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoImage3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoImage)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # student button
        img4 = Image.open(r"C:\Users\DELL\Downloads\Telegram Desktop\students1.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoImage4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoImage4, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="student Details", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg ="blue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # detect face button
        img5 = Image.open(r"C:\Users\DELL\Downloads\Telegram Desktop\students1.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoImage5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoImage4, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=5000, y=300, width=220, height=40)

        # attendance button
        img6 = Image.open(r"C:\Users\DELL\Downloads\Telegram Desktop\students1.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoImage6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoImage6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        # Help Desk

        img7 = Image.open(r"C:\Users\Asus\Pictures")
        img7 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoImage7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoImage7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Train face button
        img8 = Image.open(r"C:\Users\DELL\Downloads\Telegram Desktop\students1.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoImage8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoImage8, cursor="hand2")
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

        # photos face button
        img9 = Image.open(r"C:\Users\DELL\Downloads\Telegram Desktop\students1.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoImage9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoImage9, cursor="hand2")
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

        # photos face button
        img10 = Image.open(r"C:\Users\DELL\Downloads\Telegram Desktop\students1.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoImage10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoImage10, cursor="hand2")
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System()
    root.mainloop()