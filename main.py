from tkinter import *       #tkinter library for gui
from tkinter import ttk
from googletrans import Translator,LANGUAGES        #googletrans for translation

def translate():
    #input and output language selected
    from_lang=languages[lang1.current()]
    to_lang=languages[lang2.current()]

    #creating translator object
    translator = Translator()

    #clearing output field
    text2.configure(state='normal')
    text2.delete(0.0, 'end')
    text2.configure(state='disabled')

    #checking if input is empty if not translating and pasting output
    if(text1.get(1.0,'end').strip()!=""):
        text_to_translate = translator.translate(text=text1.get(1.0,'end'),src=from_lang,dest=to_lang)
        translated_text = text_to_translate.text

        text2.configure(state='normal')
        text2.insert(0.0,chars=translated_text)
        text2.configure(state='disabled')

if __name__=='__main__':
    # Configuring gui window
    root = Tk()
    root.geometry('800x400')
    root.title("Translator")

    #Creating dropdown menu to choose input language
    languages = tuple(LANGUAGES.values())       #Languages to choose between
    lang1 = ttk.Combobox(root)
    lang1['values'] = languages
    lang1.current(languages.index('english'))
    lang1.grid(row=0,column=0,padx=10,pady=10)

    #Creating dropdown menu to choose output language
    lang2 = ttk.Combobox(root)
    lang2['values'] = languages
    lang2.current(languages.index('hindi'))
    lang2.grid(row=0,column=2,padx=10,pady=10)

    #Enter text label
    label1 = Label(root,text="ENTER TEXT HERE:")
    label1.grid(row=1,column=0,sticky='w',padx=10)

    #Translation label
    label2 = Label(root,text="TRANSLATION:")
    label2.grid(row=1,column=2,sticky='w',padx=10)

    #Input field
    text1 = Text(root,height=10,width=40)
    text1.grid(row=2,column=0,padx=10,pady=10)

    #Translate button
    button = Button(root,text="Translate",command=translate)
    button.grid(row=2,column=1,padx=20,pady=10)

    #Output field
    text2 = Text(root,height=10,width=40,state='disabled')
    text2.grid(row=2,column=2,padx=10,pady=10)

    #mainloop keeps windows running until it gets user input for exit
    root.mainloop()