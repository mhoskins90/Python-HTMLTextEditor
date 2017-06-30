from tkinter import *
import os, sys, tkinter.filedialog
from tkinter.filedialog import askopenfilename


class EditorProgram(Tk):
	def __init__(self,type):
		self.type = type


	def run_editor(self):
		container=Tk()
		container.title("HoskinsEditor")
		container.configure(background='#f2f2f2')
		global text
		text=Text(container) 
		text.configure(background='#202020', foreground='#00FF7C')

		text.grid(row=0,columnspan=30) 


		button=Button(container, text=" Save ", command=self.saveas)
		button.configure(background='green', foreground='white', cursor="hand2") 
		button.grid(row=1, column=14)

		quit_button=Button(container, text="Close", command=container.quit) 
		quit_button.configure(background='red', foreground='white', cursor="hand2")
		quit_button.grid(row=1, column=15)
		try:
			container.mainloop()
		
		except Exception as error:
			print("Error:", error)
		else:
			print('Goodbye, come back soon!')
	def saveas(self):

		global text
	
		t = text.get("1.0", "end-1c")
		t +='\n\n'+'-'*50+'\n'+'-'*50+'\n Created With MH_Editor'

		try:
			print('Save Dialog Initiated...')
			savelocation=tkinter.filedialog.asksaveasfilename(defaultextension=".mh", filetypes=(("HoskinsEditor Document", "*.mh"),("Text Document", "*.txt"),\
				("Python Document", "*.py"),("Java Document", "*.javac"),("C Document", "*.c"),("HTML Document", "*.html"),("PHP Document", "*.php"),("All Files", "*.*") ))
			file=open(savelocation, "w+")
			file.write(t)
			file.close()
				
		except (FileNotFoundError, Exception) as error:
			print ('Save Dialog Exited Without Saving.'.format(error))
		else:
			print('File Saved Successfully!')



def main():
	regular = EditorProgram("Regular")
	regular.run_editor()


if __name__ == "__main__":
	main()
