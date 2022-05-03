import qrcode 
from tkinter import *
root=Tk()
root.title("Qr code generator")
qr=qrcode.QRCode(
	version=1,
	box_size=10,
	border=10)
data=0
imgj="1000"
def onclick():
	global data
	global imgj
	data=e.get()
	imgj=f.get()+".png"
	e.delete(0,END)
	f.delete(0,END)
	qr.add_data(data)
	qr.make(fit=True)
	img=qr.make_image(fill="black",back_color="white")
	img.save(imgj)
	k=Label(root,text="QRCode generated in same file").pack()
	
e=Entry(root,width=100,borderwidth=10)
e.insert(0,"Data for qr code")
e.pack()

f=Entry(root,width=100,borderwidth=10)
f.insert(0,"Name for the QRCode file")
f.pack()
Button(root,text='Generate',command=onclick,width=50,height=1).pack()
root.mainloop()
