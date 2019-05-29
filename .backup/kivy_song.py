# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListItemButton, ListItemLabel, \
        CompositeListItem,ListView
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.adapters.dictadapter import DictAdapter
from kivy import Config
from PyQt5.QtSql import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

Config.set('graphics', 'multisamples', '0')   #to fix OpenGL bug


#class query_song(Widget):
#    def ui_init(self):
#        self.size = 500, 500
#        self.g_grid = GridLayout(cols=2, 
#                height=self.height*0.2, width=self.width, y=self.top)
#        self.add_widget(self.g_grid)
#        self.g_btn1 = Button(text='Search by Song')
#        self.layout.add_widget(self.g_btn1)
#        self.g_btn2 = Button(text='Search by Singer')
#        self.layout.add_widget(self.g_btn2)
#        self.g_view = ModalView(width=self.width, height=self.height)
#        self.add_widget(self.g_view)
#        self.g_list = ListView(item_strings=[str(index) for index in range(100)])
#        self.g_view.add_widget(self.g_list)
        
class SongApp(App):
   
    def build(self):
        self.g_layout = BoxLayout(padding=0, orientation="vertical")
        #cols=2→set the grid to be 2 columns
        #size_hint_y=0.1→Grid's size set to 1% height of the parent object(self.g_layout)
        self.g_grid = GridLayout(cols=3, size_hint_y=0.08)
        self.g_layout.add_widget(self.g_grid)
        self.g_grid2 = GridLayout(cols=4, size_hint_x=0.5)
        self.g_grid.add_widget(self.g_grid2)
        self.g_chk1 = CheckBox(group="group1")   #search by song's name
        self.g_chk1.bind(active=self.on_checkbox_active)
        self.g_grid2.add_widget(self.g_chk1)
        self.g_btn1 = Button(text='By Song', font_size=15)
        self.g_grid2.add_widget(self.g_btn1)
        self.g_chk2 = CheckBox(group="group1")   #search by singer's name
        self.g_chk2.bind(active=self.on_checkbox_active)
        self.g_grid2.add_widget(self.g_chk2)
        self.g_btn2 = Button(text='By Singer', font_size=13)
        self.g_grid2.add_widget(self.g_btn2)
        self.g_list = ListView(item_strings=[str(index) for index in range(100)])
        self.g_layout.add_widget(self.g_list)
        
        
        

        
        
        self.g_text= TextInput(text='Pls insert keywords', multiline=False)
        self.g_grid.add_widget(self.g_text)
        self.g_btn3 = Button(text='Search', size_hint_x=0.2)
        
        self.g_grid.add_widget(self.g_btn3)
        app_pyqt = QtWidgets.QApplication(sys.argv)
        self.db = pyqt_object()
        self.db.connect_db()
        self.g_btn3.fbind('on_press', self.db.fetch_data)
        #self.g_btn3.bind(on_press=self.test_fun)
        
        return self.g_layout
    def test_fun(self, obj):
        print("This is a test function")
        
    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active')
        else:
            print('The checkbox', checkbox, 'is inactive')
class pyqt_object(object):
    def connect_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        #filename = "D:\\Coding\\Python\\py_folder\\qt_program\\qry_song\\crazyktv.db3"
        filename = "crazyktv.db3"
        db.setDatabaseName(filename)
        print(QSqlDatabase.isDriverAvailable("QSQLITE"))
        if not db.open():
            print("Initialize fail")
            err_str = db.lastError().text()
            print(err_str)
    def fetch_data(self, obj):
        query = QSqlQuery()
        if song.g_chk1.active:
            p_active = True
        else:
            p_active = False
        l_wc = None   #輸入的查詢條件
        if song.g_chk1.active:
            l_text = song.g_text.text
            l_text = "%" + l_text + "%"
            l_wc = "Song_SongName" + " LIKE '%s'"  % l_text
        elif song.g_chk2.active:
            l_text = song.g_text.text
            l_text = "%" + l_text + "%"
            l_wc = "Song_Singer" + " LIKE '%s'"  % l_text
        l_sql = "SELECT Song_Singer,Song_SongName,Song_Id"\
                   "  FROM ktv_Song,ktv_Singer"\
                   " WHERE Song_Singer = Singer_Name"
        
        if l_wc is None:
            #如果沒有輸入查詢條件，不要查詢出東西來，以防資料量龐大，查詢時間會非常久
            l_wc = "1=2"
            return
        l_sql = l_sql + " AND " + l_wc
        l_i = 0
        #l_dict = {}
        
        query.exec_(l_sql)
        #塞資料到表格時，需先關避sort功能，塞完資料才可開啟
        #self.tb_1.setSortingEnabled(False)
        l_i = 1
        print("query.isActive", query.isActive())
        while query.next():
            integers_dict[l_i] = {'is_selected': False,'singer_name':query.value(0), 
                                                  'song_name':query_value(1), 
                                                  'song_id':query_value(2)}
            #l_return1 = query.value(0)
            #l_return2 = query.value(1)
            #l_return3 = query.value(2)
            #l_return = []
            #l_return.append(query.value(0))
            #l_return.append(query.value(1))
            #l_return.append(query.value(2))
        args_converter = lambda row_index, rec: {'text': rec['text'],
                'size_hint_y': None,
                'height': 25,
                'cls_dicts': [{'cls': ListItemButton,'kwargs': {'text': rec['singer_name']}}, 
                                    {'cls': ListItemLabel,'kwargs': {'text': rec['song_name']}},
                                    {'cls': ListItemButton,'kwargs': {'text': rec['song_id']}}]}
        try:
            item_strings = ["{0}".format(index) for index in range(0, len(intergers_dict))]
        except:
            return
        dict_adapter = DictAdapter(sorted_keys=item_strings,
                                   data=integers_dict,
                                   args_converter=args_converter,
                                   selection_mode='single',
                                   allow_empty_selection=False,
                                   cls=CompositeListItem)

if __name__ == '__main__':
    #app_pyqt = QtWidgets.QApplication(sys.argv)
    #ui = pyqt_object()
    #ui.connect_db()
    
    song = SongApp()
    song.run()
