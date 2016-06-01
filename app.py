# -*- coding: utf-8 -*-
import sys, locale
reload(sys)
sys.setdefaultencoding('utf-8')
sys.setdefaultencoding(locale.getpreferredencoding())

from flask import render_template,Flask, request, send_from_directory,send_file
import pay_API ,constants,log_db

app = Flask(__name__, static_url_path="", static_folder='static')

@app.route('/' , methods=['GET', 'POST'])
def router():
    if request.method == 'POST':

        # Записываем в БД в лог таблицу и получаем ID которій потом используем как ID shop (за неимением настоящего ИД от магазина)
        id=log_db.add_pay(request.form)

        if request.form["sel"]=="643":

            # Получаем подпись согласно правил для TIP протокола
            sign=pay_API.getTIPsign(id,request.form)

            return  render_template('payTIP.html',data=request.form, id=id, sign=sign)

        if request.form["sel"]=="980":

            # Получаем подпись согласно правил для API метода
            sign=pay_API.getAPIsign(id,request.form)

            # Дергаем процедуру которая отправит пост на сервер по https
            text_r=pay_API.send_postAPI(id,sign,request.form)

            return render_template('payAPI.html', data=request.form, id=id, sign=sign, text_r=text_r )

    else:

        return render_template('hello.html', data=constants.pay_cur)

@app.route('/log' , methods=['GET', 'POST'])
def log():
    if request.method == 'GET':
        req=log_db.get_last()
        return render_template('log.html',data=req)
    else:
        return render_template('hello.html', data=constants.pay_cur)


@app.route('/success')
def success():
    return "<h1>success :)</h1>"

@app.route('/failed')
def failed():
    return "<h1>failed</h1>"

@app.route('/mess')
def mess():
    print request,request.form
    return "<h1>message - OK </h1>"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



