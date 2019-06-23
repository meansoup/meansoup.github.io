from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ListProperty, BooleanProperty, StringProperty

Builder.load_file('widget/verse.kv')

class VerseLabel(ButtonBehavior, GridLayout):
    info_list = ListProperty([])
    eng_content = StringProperty()
    is_search = BooleanProperty(False)

    book = 1
    chapter = 1
    verse = 1
    content = None

    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)
        self.cols=2
        self.markup=True
        self.make_verse()

    def on_info_list(self, instance, value):
        self.book = self.info_list[0]
        self.chapter = self.info_list[1]
        self.verse = self.info_list[2]
        self.content = self.info_list[3]

    def make_verse(self):
        self.ids.verse.text = str(self.verse)
        self.ids.content.text = self.content

    def on_press(self):
        if self.is_search:
            words = "%s %s" % (self.book, self.chapter)
            self.parent.parent.find(words)
        else:
            if self.ids.content.text is self.content:
                self.ids.content.text = self.eng_content
            else:
                self.ids.content.text = self.content

class VerseTitle(Label):
    pass