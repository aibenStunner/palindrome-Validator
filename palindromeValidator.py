__author__ = '8.Ball'

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.core.audio import SoundLoader



#Keeping a fixed window size
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'width', '500')

#Getting audio into program
global soundPal, soundNonPal
soundPal = SoundLoader.load('audio/soundPal.mp3')
soundNonPal = SoundLoader.load('audio/soundNonPal.mp3')


"""
Main Class
"""
class PalindromeApp(App):
    def build(self):
        self.title = 'Palindrome Validator'
        self.icon = 'images/icon.png'

        #Creating the layout for the interaction screen
        self.layout = GridLayout()

        #Displaying the logo
        self.logo = Image(source = 'images/icon_validator.png',
                          size= (350, 350),
                          x = 75,
                          y = 50)
        self.layout.add_widget(self.logo)
        self.animate(self.logo)
        self.animateLogo(self.logo)


        #Displaying the entry area
        self.inputArea = TextInput(hint_text= 'Enter text here',
                                   multiline= False,
                                   size = (470, 30),
                                   x = 15,
                                   y = 80
                                   )
        self.inputArea.bind(on_text_validate= self.start)
        self.layout.add_widget(self.inputArea)
        self.animate(self.inputArea)
        self.animateEntry(self.inputArea)


        #Displaying the Validate Button
        self.checkBtn = Button(text= 'Check',
                               size = (100, 30),
                               x = 200,
                               y = 30,
                               on_press= self.start)
        self.layout.add_widget(self.checkBtn)
        self.animate(self.checkBtn)
        self.animateCheck(self.checkBtn)

        #Displaying the Clear Button
        self.clear = Button(text= '×',
                            font_size= 22,
                            color= (215, 215, 215, 1),
                            background_color= (228, 228, 228, .1),
                            size= (29, 27),
                            x = 456,
                            y = 82,
                            on_press= self.clearText)
        self.layout.add_widget(self.clear)
        self.animate(self.clear)
        self.animateX(self.clear)


        #Displaying Help Button
        self.help = Button(text= 'Help   |',
                           font_size= 10,
                           background_color= (0, 0, 0, 0),
                           size= (45, 20),
                           x = 420,
                           y = 0,
                           on_press= self.showHelp)
        self.layout.add_widget(self.help)


        #Displaying About Button
        self.about = Button(text= 'About',
                           font_size= 10,
                           background_color= (0, 0, 0, 0),
                           size= (45, 20),
                           x = 455,
                           y = 0,
                           on_press= self.showAbout)
        self.layout.add_widget(self.about)

        #Displaying copyright tag
        self.copyright = Label(text='Copyright © 2019  |_aiben',
                               font_size= 11,
                               x = 27,
                               y = -40)
        self.layout.add_widget(self.copyright)

        return self.layout

    #Funciton to animate logo
    def animateLogo(self, what):
        anim = Animation(x = 75, y = 50)
        anim += Animation(x = 75, y = 170, duration= 0.5)
        anim.start(what)

    #Funciton to animate logo
    def animateEntry(self, what):
        anim = Animation(x = 15, y = 80)
        anim += Animation(x = 15, y = 250, duration= 0.5)
        anim.start(what)

    #Funciton to animate check
    def animateCheck(self, what):
        anim = Animation(x = 200, y = 30)
        anim += Animation(x = 200, y = 200, duration= 0.5)
        anim.start(what)

    #Funciton to animate check
    def animateX(self, what):
        anim = Animation(x = 456, y = 82)
        anim += Animation(x = 456, y = 252, duration= 0.5)
        anim.start(what)

    #Fade in animation function
    def animate(self, what):
        anim = Animation(opacity=0, duration=0)
        anim += Animation(opacity=1, duration=2)
        anim.start(what)

    #Fade out animation function
    def animateOut(self, what):
        anim = Animation(opacity=0, duration=0)
        anim += Animation(opacity=1, duration=0.5)
        anim.start(what)

    #Function to get input from the text widget
    def start(self, *args):
        self.userInput = self.inputArea.text
        userInput = self.userInput


        #Checking if input is palindromic
        self.status = self.palindromeString(self.userInput)

        #Outputing the result
        if self.status == True:
            if self.userInput == '':
                self.showHelpError()
            else:
                self.statusGood()

        elif self.status == False:
            self.statusBad()



    #Function to clear the entry area
    def clearText(self, instance):
        #Clear the input area
        self.inputArea.text= ''


        #Clear the area
        self.check = Image(source= 'images/Blank.png',
                           x = 200,
                           y = 81)
        self.layout.add_widget(self.check)
        self.animateOut(self.check)

        #Clear text area
        self.clearStatusText = Image(source= 'images/clearStatus.png',
                                size= (350, 350),
                                x = 60,
                                y = -120)
        self.layout.add_widget(self.clearStatusText)
        self.animateOut(self.clearStatusText)


    def showHelp(self, instance):
        help = GridLayout()
        closeBtn = Button(text='Close',
                          size= (100, 30),
                          x = 385,
                          y = 20)

        text_1 = 'Type any string(combination of characters) and\nPalindrome Validator 1.0.0 will determine if it is palindromic\nor not.'
        helpText_1 = Label(text= text_1, markup= True,
                         font_size= 14,
                         x = 250,
                         y = 230)
        text_2 = 'Everything is accessible in the environment.'
        helpText_2 = Label(text= text_2, markup= True,
                         font_size= 14,
                         x = 201,
                         y = 165)
        text_3 = 'The environment will display a green swoosh(correct sign)\nif the string is palindromic and a red cross(wrong sign) if\nit is not.'
        helpText_3 = Label(text= text_3, markup= True,
                         font_size= 14,
                         x = 246,
                         y = 105)
        text_4 = 'Contact us on  [size=12]info@palindrome.org  [size=14]if you face any challenges.'
        helpText_4 = Label(text= text_4, markup= True,
                         font_size= 14,
                         x = 195,
                         y = 30)
        icon = Image(source= 'images/helpIcon.png',
                     size= (85, 85),
                     x = 15,
                     y = 230)
        help.add_widget(icon)
        help.add_widget(helpText_1)
        help.add_widget(helpText_2)
        help.add_widget(helpText_3)
        help.add_widget(helpText_4)
        help.add_widget(closeBtn)
        helpPopup = Popup(title='Help',
                          content= help,
                          size= (250, 250),
                          auto_dismiss= False)
        closeBtn.bind(on_press=helpPopup.dismiss)
        helpPopup.open()

    #Function to call about popup
    def showAbout(self, instance):
        about = GridLayout()
        closeBtn = Button(text='Close',
                          size= (100, 30),
                          x = 385,
                          y = 20)

        icon = Image(source= 'images/icon.png',
                     size= (125, 125),
                     x = 30,
                     y = 150)

        text_1 = '[b]Palindrome  Validator'
        aboutText_1 = Label(text= text_1, markup= True,
                         font_size= 23,
                         x = 250,
                         y = 270)
        text_2 = '1.0.0  Maiden'
        aboutText_2 = Label(text= text_2, markup= True,
                         font_size= 17,
                         x = 188,
                         y = 240)

        text_3 = 'Palindrome Validator is full-featured environment \naiming to show if a string is palindromic.'
        aboutText_3 = Label(text= text_3, markup= True,
                         font_size= 13,
                         x = 278,
                         y = 190)
        text_4 = 'A palindrome is a string(combination of characters)\nthat reads the same backwards and forwards.\nENJOY!'
        aboutText_4 = Label(text= text_4, markup= True,
                         font_size= 13,
                         x = 282,
                         y = 130)
        text_5 = 'Help and join us!'
        aboutText_5 = Label(text= text_5, markup= True,
                         font_size= 12,
                         x = 184,
                         y = 60)
        text_6 = 'info@palindrome.org'
        aboutText_6 = Label(text= text_6, markup= True,
                         font_size= 11,
                         x = 190,
                         y = 40)
        text_7 = 'http://wwww.palindrome.org'
        aboutText_7 = Label(text= text_7, markup= True,
                         font_size= 11,
                         x = 210,
                         y = 25)
        copyright = Label(text='Copyright © 2019  |_aiben',
                               font_size= 11,
                               x = 31,
                               y = -33)
        about.add_widget(copyright)
        about.add_widget(icon)
        about.add_widget(aboutText_1)
        about.add_widget(aboutText_2)
        about.add_widget(aboutText_3)
        about.add_widget(aboutText_4)
        about.add_widget(aboutText_5)
        about.add_widget(aboutText_6)
        about.add_widget(aboutText_7)
        about.add_widget(closeBtn)
        aboutPopup = Popup(title='About',
                          content= about,
                          size= (250, 250),
                          auto_dismiss= False)
        closeBtn.bind(on_press=aboutPopup.dismiss)
        aboutPopup.open()


    #Function that checks Palindrome
    def palindromeString(self, userInput):
        CuserInput = ''
        for char in userInput:
            if char != ' ':
                CuserInput += char

        print(CuserInput)
        reversedInput = CuserInput[::-1]
        if CuserInput == reversedInput:
            return True
        else:
            return False

    #Function to display palindromic
    def statusGood(self):
        #Clear the area
        self.check = Image(source= 'images/Blank.png',
                           x = 200,
                           y = 80)
        self.layout.add_widget(self.check)

        #Display icon
        self.check = Image(source= 'images/checkIcon.PNG',
                           x = 200,
                           y = 80)

        self.layout.add_widget(self.check)
        self.animate(self.check)

        #Play sound
        soundPal = SoundLoader.load('audio/soundPal.mp3')
        soundPal.play()

        #Clear text area
        self.clearStatusText = Image(source= 'images/clearStatus.png',
                                size= (350, 350),
                                x = 60,
                                y = -120)
        self.layout.add_widget(self.clearStatusText)

        #Display Text
        self.statusText = Label(text= 'Palindromic',
                                color= (0, 79, 175, 1),
                                font_size= 25,
                                x = 200,
                                y = 10,)
        self.layout.add_widget(self.statusText)
        self.animate(self.statusText)



    #Function to display non-palindromic
    def statusBad(self):
        #Clear the area
        self.check = Image(source= 'images/Blank.png',
                           x = 200,
                           y = 80)
        self.layout.add_widget(self.check)

        #Display icon
        self.check = Image(source= 'images/xIcon.PNG',
                           x = 200,
                           y = 80)
        self.layout.add_widget(self.check)
        self.animate(self.check)

        #Play sound
        soundNonPal = SoundLoader.load('audio/soundNonPal.mp3')
        soundNonPal.play()

        #Clear text area
        self.clearStatusText = Image(source= 'images/clearStatus.png',
                                size= (350, 350),
                                x = 60,
                                y = -120)
        self.layout.add_widget(self.clearStatusText)

        #Display Text
        self.statusText = Label(text= 'Non-Palindromic',
                                color= (41, 0, 0, 1),
                                font_size= 25,
                                x = 200,
                                y = 10,)
        self.layout.add_widget(self.statusText)
        self.animate(self.statusText)


    #Function to call help popup when there is no text in the input area
    def showHelpError(self):
        help = GridLayout()
        closeBtn = Button(text='Close',
                          size= (100, 30),
                          x = 385,
                          y = 20)

        text_1 = 'Type any string(combination of characters) and\nPalindrome Validator 1.0.0 will determine if it is palindromic\nor not.'
        helpText_1 = Label(text= text_1, markup= True,
                         font_size= 14,
                         x = 250,
                         y = 230)
        text_2 = 'Everything is accessible in the environment.'
        helpText_2 = Label(text= text_2, markup= True,
                         font_size= 14,
                         x = 201,
                         y = 165)
        text_3 = 'The environment will display a green swoosh(correct sign)\nif the string is a palindromic and a red cross(wrong sign)\nit is not.'
        helpText_3 = Label(text= text_3, markup= True,
                         font_size= 14,
                         x = 246,
                         y = 105)
        text_4 = 'Contact us on  [size=12]info@palindrome.org  [size=14]if you face any challenges.'
        helpText_4 = Label(text= text_4, markup= True,
                         font_size= 14,
                         x = 195,
                         y = 30)
        icon = Image(source= 'images/helpIcon.png',
                     size= (85, 85),
                     x = 15,
                     y = 230)
        help.add_widget(icon)
        help.add_widget(helpText_1)
        help.add_widget(helpText_2)
        help.add_widget(helpText_3)
        help.add_widget(helpText_4)
        help.add_widget(closeBtn)
        helpPopup = Popup(title='Help',
                          content= help,
                          size= (250, 250),
                          auto_dismiss= False)
        closeBtn.bind(on_press=helpPopup.dismiss)
        helpPopup.open()



PalindromeApp().run()