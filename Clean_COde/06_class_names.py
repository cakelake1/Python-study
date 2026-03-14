# 3.1. Улучшите пять имён классов в вашем коде.
# Пример 1
# class Node:
#     def __init__(self, v):
#         self.value = v
#         self.next = None
# class ListNode:
#     def __init__(self, v):
#         self.value = v
#         self.next = None
# Пример 2
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
# class SingleLinkedList: # односвязный список
#     def __init__(self):
#         self.head = None
#         self.tail = None
# Пример 3
# class DynArray: 
#     def __init__(self):
#         self.count = 0
#         self.capacity = 16
#         self.array = self.make_array(self.capacity)

# class DynamicArray: 
#     def __init__(self):
#         self.count = 0
#         self.capacity = 16
#         self.array = self.make_array(self.capacity)
# Пример 4
# class Stack:
#     def __init__(self):
#         self.stack = []

# class LinkedListStack:
#     def __init__(self):
#         self.stack = []
# Пример 5
# class OrderedList:
#     def __init__(self, asc):
#         self.head = None
#         self.tail = None
#         self.__ascending = asc

# class SortedLinkedList:
#     def __init__(self, asc):
#         self.head = None
#         self.tail = None
#         self.__ascending = asc


#3.2.Улучшите семь имён методов и объектов по схеме из пункта 2:

# Вот такой я нашел код на гите:
# from tkinter import*
# from tkinter import ttk
# from pathlib import Path

# # main window
# win = Tk() - window = Tk() # Пример 1
# win.title("Calculator")
# win.resizable(False,False)
# win.geometry("700x750")        
# win.config(bg = "black")         
# c = Canvas(win,width = 350,height = 110,bg = "pink")       # output canvas
# c.place(relx = 0.3,rely = 0.02)  
# path = r"numbers/" 

# live_label_text = StringVar()
# live_label = Label(win,textvariable = live_label_text,fg = "black",bg = "pink",font = ("arial",40,"bold") )
# result_label_text = StringVar()
# result_label = Label(win,textvariable = result_label_text , fg = "black" , bg ="pink",font = ("arial",40,"bold"))
# p = [] -  expression_parts = [] Пример 2
# status = [] - has_result = [] Пример 3
# result_status = [] - has_expression = [] ПРимер 4

# # =======================
# try:
#     def result(): - def calculate() # Пример 5
    
#         process = ""
#         for a in p:
#             process += a
#         result = eval(process)
#         result_label_text.set("= " + str(result))
#         live_label_text.set("")
#         live_label.place(relx =0.328 ,rely = 0.053)
#         result_label.place(relx =0.328 ,rely = 0.053)
#         status.append("True")
#         result_status.append("True")


#     def result_deleter(): - def clear_result() # ПРимер 6
#         if "True" in status:
#             result_label_text.set("")
#             for member in range(len(status)):
#                 status.remove(status[0])


#     def list_reseter(): - def clear_expression() # пример 7
#         if "True" in result_status:
#             for x in range(len(p)):
#                 p.remove(p[0])

#             for member in range(len(result_status)):
#                 result_status.remove(result_status[0])

# except:
#    result_label_text.set("Error")
#    result_label.place(relx =0.328 ,rely = 0.053)
            
# дальнейший код я удаляю, улучшений там нет


