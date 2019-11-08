# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:18:27 2019

@author: adjimagnan
"""
def starttag(tag):
    return '<'+tag+'>'
def closetag(tag):
    return '</'+tag+'>' 

def create_tag(tag, content):
    print(starttag(tag)+content+closetag(tag))
    
def th_select():
    selectstart='<select name ="objectId">'
    selectend='</select>'
    ## th_option()
    op= '  <option th:text="${object.id}" \n\tth th:each="obj : ${objects}"  \n\tth:text="${obj.name}"\n\tth:value="${obj.id}"> Default Option i\n  </option>'
    print(selectstart+'\n' + op+ '\n'+ selectend)
   
def th_label(element):
    print('<label th:for="'+element+'">'+(element[0]).upper()+element[1:]+'</label>')

def th_option():
    op= '<option th:text="${object.id}" \n\tth th:each="obj : ${objects}"  \n\tth:text="${obj.name}"\n\tth:value="${obj.id}"> Default Option i\n</option>'
    print(op)
    
def th_input(fieldArray):

    for element in fieldArray:
        label='<label th:for="'+element+'">'+(element[0]).upper()+element[1:]+'</label>'
        inp  ='<input class ="form-control" th:field="*{'+element+'}" name="'+element+'"/>'
        span ='<span class ="error" th:errors="*{'+element+'}"></span>'
        #print('<div class="form-group">')
        print('<div class="form-group">\n    ' +label +'\n    '+ inp + '\n    '+span+'\n'+closetag('div'))
        
        
def th_submit():
    submit='<input type="submit"  class="btn btn-primary" value="Add new object"/>'
    print(submit)
        
def thesinple_form(inputfieldsArray, selectablefields):
    print('<div class="container">')
    print('<form method="POST" style="max-width:600px;" th:object="${obj}" action="add">')
    print(th_input(inputfieldsArray))
    
    for element in selectablefields:
        print(starttag('div'))

        print(th_select())
        
    print(th_submit())
    print(closetag('div')+'\n'+closetag('form'))
    
def th_table(fieldsArray, obj):
    print('<p th:unless="${'+obj+'s}">no ' + obj + ' yet recorded in our system !</p>')
    print('<h1> List of the '+obj+'s<h1>\n')
    print(starttag("table") +'\n\t'+ starttag('thead')+'\n\t\t'+ starttag('tr'))
       
    for element in fieldsArray:
        print('\t\t\t'+starttag('th') + element[0].upper()+element[1:] + closetag('th'))
    
    print('\t\t' + closetag('tr') + '\n\t' + closetag('thead'))
    print('\n\t<tr th:each="'+obj+' : ${'+obj+'s}">\n')
    
    for element in fieldsArray:
        print('\t\t\t<td th:text="${'+obj+'.'+element+'}"></td>') 
    print('\t</tr>')
    print(closetag('table'))   
        
    
    
    
    
    
