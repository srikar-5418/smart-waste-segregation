import cv2 as cv
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.title("smart waste segregation")
cam =cv.VideoCapture(0)
s=""
s1="captured_image.jpg"
x = False
def select_img():
    s=filedialog.askopenfilename(initialdir="HOME",title="select a file",filetypes=(("jpg files","*.jpg"),("jpeg files","*.jpeg")))
    if s:
        x = True
        top=Toplevel()
        top.title("select an image")
        image=Image.open(s)
        img_label=Label(top)
        img_label.image = ImageTk.PhotoImage(image)
        img_label.config(image=img_label.image)
        img_label.pack()
        b=Button(top,text="close",command=top.destroy).pack()


def show_webcam():
    def close_window():
        window.destroy()
        
    def capture_image():
        # Read frame from the webcam
        ret, frame = cap.read()
        if ret:
            # Save the frame as an image file
            cv.imwrite("captured_image.jpg", frame)
        close_window()
        top=Toplevel()
        top.title("captured image")
        image=Image.open(s1)
        img_label=Label(top)
        img_label.image = ImageTk.PhotoImage(image)
        img_label.config(image=img_label.image)
        img_label.pack()
        response=messagebox.askyesno("do you like the image","do you like the image")
        if response==0:
            top.destroy()
            show_webcam()
           
        b=Button(top,text="close",command=top.destroy).pack()


     

    
    def update_frame():
        # Read frame from the webcam
        ret, frame = cap.read()
        if ret:
            # Convert the frame to RGB format
            frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            
            # Convert the frame to an ImageTk format
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            
            # Update the label with the new frame
            label.imgtk = imgtk
            label.config(image=imgtk)
        
        # Call update_frame again after 10 ms
        label.after(10, update_frame)
    
    # Initialize the webcam capture
    cap = cv.VideoCapture(0)
    
    # Create a new Tkinter window
    window = Toplevel()
    window.title("Webcam Viewer")
    
    # Create a label to display the video feed
    label = Label(window)
    label.pack()
    
    # Button to capture an image
    capture_button = Button(window, text="Capture Image", command=capture_image)
    capture_button.pack()
    
    # Button to close the webcam window
    close_button = Button(window, text="Close", command=close_window)
    close_button.pack()
    
    # Call the update_frame function to start updating the video feed
    update_frame()




title=Label(root,text="SMART  WASTE  SEGREGATION",width=100,pady=50,font=('Arial,10,bold')).pack()
b1=Button(root,text="select an image",command=select_img).pack()
b2=Button(root,text="take an image",command=show_webcam).pack()

p=-1

from load_predict import pre
if(x):
    l=[]
    l.append(s)
    p=pre(l)
else:
    l = []
    l.append(s1)
    p=pre(l)
print(p)
o=Label(root,text=str(p)).pack()
# top=Toplevel()
root.mainloop()



cam.release()
cv.destroyAllWindows()
