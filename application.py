from flask import Flask
from flask import url_for, render_template, request, redirect, session

app = Flask(__name__)

app.config['SECRET_KEY'] = '\x81u0\x83\xa9|\xea\xed\xbey\xa0\xe8\xed\x05Mm\xf9\x1e\xe9V\x85p\xfa\xa8'


@app.route('/')
def index():
    session.pop('numbers', None)
    session['numbers'] = [i for i in range(1,66)]
    return render_template('index.html')

@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/contacts')
def contacts():

    return render_template('contacts.html')

@app.route('/task1')
def task1 ():
    session.pop('numbers', None)
    if request.args:
        print ('ok')
        print (request.args)
        session['numbers'] = session['remember']
        if request.args == {'repeat': ['Повторить']}:
            session['numbers'].append(session['numbers'][0])
            session['numbers'].remove(session['numbers'][0])
            print (session['numbers'])
            if session['numbers'] == []:
                session['numbers'] = [i for i in range(1,66)]
                return render_template('final.html')
            session['remember'] = session['numbers']
            return render_template('task1.html', number_of_task = 'number=' + str(session['numbers'][0]))
        if request.args == {'right': ['Правильно']}:
            session['numbers'].remove(session['numbers'][0])
            print (session['numbers'])
            if session['numbers'] == []:
                session['numbers'] = [i for i in range(1,66)]
                return render_template('final.html')
            session['remember'] = session['numbers']
            return render_template('task1.html', number_of_task = 'number=' + str(session['numbers'][0]))
    else:
        print ('not ok')
        session.pop('numbers', None)
        session['numbers'] = [i for i in range(1,66)]

    session['numbers'] = [i for i in range(1,66)]
    session['remember'] = [i for i in range(1,66)]
    return render_template('task1.html', number_of_task = 'number=1')

@app.route('/task2')
def task2 ():
    session.pop('numbers', None)
    if request.args:
        print ('ok')
        print (request.args)
        session['numbers'] = session['remember']
        if request.args == {'repeat': ['Повторить']}:
            session['numbers'].append(session['numbers'][0])
            session['numbers'].remove(session['numbers'][0])
            print (session['numbers'])
            if session['numbers'] == []:
                session['numbers'] = [i for i in range(1,66)]
                return render_template('final.html')
            session['remember'] = session['numbers']
            return render_template('task2.html', number_of_task = 'number=' + str(session['numbers'][0]))
        if request.args == {'right': ['Правильно']}:
            session['numbers'].remove(session['numbers'][0])
            print (session['numbers'])
            if session['numbers'] == []:
                session['numbers'] = [i for i in range(1,66)]
                return render_template('final.html')
            session['remember'] = session['numbers']
            return render_template('task2.html', number_of_task = 'number=' + str(session['numbers'][0]))
    else:
        print ('not ok')
        session.pop('numbers', None)
        session['numbers'] = [i for i in range(1,66)]

    session['numbers'] = [i for i in range(1,66)]
    session['remember'] = [i for i in range(1,66)]
    return render_template('task2.html', number_of_task = 'number=1')

@app.route('/task3')
def task3 ():
    session.pop('numbers', None)
    if request.args:
        print ('ok')
        print (request.args)
        session['numbers'] = session['remember']
        if request.args == {'repeat': ['Повторить']}:
            session['numbers'].append(session['numbers'][0])
            session['numbers'].remove(session['numbers'][0])
            print (session['numbers'])
            if session['numbers'] == []:
                session['numbers'] = [i for i in range(1,66)]
                return render_template('final.html')
            session['remember'] = session['numbers']
            return render_template('task3.html', number_of_task = 'number=' + str(session['numbers'][0]))
        if request.args == {'right': ['Правильно']}:
            session['numbers'].remove(session['numbers'][0])
            print (session['numbers'])
            if session['numbers'] == []:
                session['numbers'] = [i for i in range(1,66)]
                return render_template('final.html')
            session['remember'] = session['numbers']
            return render_template('task3.html', number_of_task = 'number=' + str(session['numbers'][0]))
    else:
        print ('not ok')
        session.pop('numbers', None)
        session['numbers'] = [i for i in range(1,66)]

    session['numbers'] = [i for i in range(1,66)]
    session['remember'] = [i for i in range(1,66)]
    return render_template('task3.html', number_of_task = 'number=1')

@app.route('/task4')
def task4 ():
    session.pop('numbers', None)
    if request.args:
        print ('ok')
        print (request.args)
        session['numbers'] = session['remember']
        if request.args == {'repeat': ['Повторить']}:
            session['numbers'].append(session['numbers'][0])
            session['numbers'].remove(session['numbers'][0])
            print (session['numbers'])
            if session['numbers'] == []:
                session['numbers'] = [i for i in range(1,66)]
                return render_template('final.html')
            session['remember'] = session['numbers']
            return render_template('task4.html', number_of_task = 'number=' + str(session['numbers'][0]))
        if request.args == {'right': ['Правильно']}:
            session['numbers'].remove(session['numbers'][0])
            print (session['numbers'])
            if session['numbers'] == []:
                session['numbers'] = [i for i in range(1,66)]
                return render_template('final.html')
            session['remember'] = session['numbers']
            return render_template('task4.html', number_of_task = 'number=' + str(session['numbers'][0]))
    else:
        print ('not ok')
        session.pop('numbers', None)
        session['numbers'] = [i for i in range(1,66)]

    session['numbers'] = [i for i in range(1,66)]
    session['remember'] = [i for i in range(1,66)]
    return render_template('task4.html', number_of_task = 'number=1')

##if __name__ == '__main__':
##    app.run(host='127.0.0.1',port='80')



##if __name__ == '__main__':
##    app.run(debug=False)

if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
