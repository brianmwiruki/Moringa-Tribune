from django.test import TestCase
from .models import Editor, Article, tags

# Create your tests here.

class EditorTestClass(TestCase):

    #set up method
    def setUp(self):
        self.Bryan = Editor(first_name = 'Bryan', last_name = 'Mwiruki', email = 'mwiruki@outlook.com')

    # Testing instance 
    def test_instance(self):
        self.assertTrue(isinstance(self.Bryan,Editor))
        
    #testting save method
    def test_save_method(self):
        self.Bryan.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)