# coding=utf-8
__author__ = 'Pedro'
import random

from mechanize import *

br = Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 '
                                'Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

for x in range(0, 18):
    br.open("http://goo.gl/forms/HnPoFG4NXJ")
    br.select_form(nr=0)

    br.form['entry.1270768841'] = ['Si', ]  # Te gusta el cine?

    br.submit()

    br.select_form(nr=0)
    lista = br.form.controls[0].get_items()
    listaGenero = br.form.controls[1].get_items()
    listaVisita = br.form.controls[2].get_items()

    br.form['entry.299115494'] = [
        lista[random.randint(0, len(lista) - 1)].name]  # ¿Cuándo fue la última vez que asististe al cine?
    try:
        br.form['entry.1324501201'] = [listaGenero[random.randint(0, len(listaGenero) - 1)].name, listaGenero[
            random.randint(0, len(listaGenero) - 1)].name]  # ¿Cual es tu género(s) preferido(s)?
    except Exception as e:
        br.form['entry.1324501201'] = [listaGenero[1].name, listaGenero[3].name]

    br.form['entry.1180334965'] = [listaVisita[0].name]  # ¿Has asistido a algún festival de cine?

    br.submit('continue')
    br.select_form(nr=0)

    listaAsistio = br.form.controls[0].get_items()
    listaFestivales = br.form.controls[1].get_items()
    listaExperiencia = br.form.controls[2].get_items()
    listaGusto = br.form.controls[3].get_items()
    listaRedesSociales = br.form.controls[4].get_items()

    br.form['entry.1422577231'] = [
        listaAsistio[random.randint(0, len(listaAsistio) - 1)].name]  # Asisito mas de una vez

    try:
        br.form['entry.169182791'] = [listaFestivales[random.randint(0, len(listaFestivales) - 1)].name,
                                      listaFestivales[
                                          random.randint(0, len(listaFestivales) - 1)].name]  # Lista de festivales
    except Exception as e:
        br.form['entry.169182791'] = [listaFestivales[1].name, listaFestivales[3].name]

    try:
        br.form['entry.327814251'] = [listaGusto[random.randint(0, len(listaGusto) - 1)].name, listaGusto[
            random.randint(0, len(listaGusto) - 1)].name]  # Lista de festivales
    except Exception as e:
        br.form['entry.327814251'] = [listaGusto[1].name, listaGusto[3].name]

    br.form['entry.22992892'] = [
        listaExperiencia[random.randint(0, len(listaExperiencia) - 1)].name]  # Experiencia de Festivales
    br.form['entry.1819820249'] = ['Si', ]
    br.submit('continue')

    br.select_form(nr=0)
    listaRedesExtendida = br.form.controls[0].get_items()

    try:
        br.form['entry.1991110922'] = [listaRedesExtendida[random.randint(0, len(listaRedesExtendida) - 1)].name,
                                       listaRedesExtendida[
                                           random.randint(0, len(
                                               listaRedesExtendida) - 1)].name]  # Lista de Redes extendidad
    except Exception as e:
        br.form['entry.1991110922'] = [listaRedesExtendida[1].name, listaRedesExtendida[3].name]

    br.submit('continue')

    br.select_form(nr=0)
    listaMedios = br.form.controls[0].get_items()
    listaAsistir = br.form.controls[1].get_items()

    try:
        br.form['entry.484568453'] = [listaMedios[random.randint(0, len(listaMedios) - 1)].name, listaMedios[
            random.randint(0, len(listaMedios) - 1)].name]  # Lista de Redes extendidad
    except Exception as e:
        br.form['entry.484568453'] = [listaMedios[1].name, listaMedios[3].name]

    br.form['entry.193243677'] = ['Si', ]  # Has escuchado del evento?
    br.submit('continue')

    br.select_form(nr=0)
    listaFuenteInformacion = br.form.controls[0].get_items()

    try:
        br.form['entry.879356540'] = [listaFuenteInformacion[random.randint(0, len(listaFuenteInformacion) - 1)].name,
                                      listaFuenteInformacion[
                                          random.randint(0, len(listaFuenteInformacion) - 1)].name]
    except Exception as e:
        br.form['entry.879356540'] = [listaFuenteInformacion[1].name, listaFuenteInformacion[3].name]

    br.submit('continue')

    br.select_form(nr=0)
    listaOpcionesAsistir = br.form.controls[0].get_items()

    br.form['entry.578360842'] = ['No', ]  # Vasir?

    br.submit('continue')

    br.select_form(nr=0)
    br.submit('continue')

    br.select_form(nr=0)

    listaSexo = br.form.controls[0].get_items()
    listaEdad = br.form.controls[1].get_items()

    br.form['entry.1416455614'] = [listaSexo[random.randint(0, len(listaSexo) - 1)].name]  # Sexo
    br.form['entry.1943223090'] = [listaEdad[random.randint(0, len(listaEdad) - 1)].name]  # Edad
    br.form['entry.646761179'] = 'Toluca, Estado de Mexico'
    br.submit('submit')

    print x
    print br.response().code
