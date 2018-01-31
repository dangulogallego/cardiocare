# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.simple_tag
def calculateRCV(self, seguimiento):
    data = {}
    if self.genero == 'F' and not self.has_diabetes(seguimiento):
        rnum = self.calculateRCVF(seguimiento) * 0.25
    else:
        rnum = self.calculateRCVF(seguimiento)
    data['numeric'] = str(self.calculateRCVCount(seguimiento)) + '/91 (' + str(rnum) + ')'
    data['conceptual'] = self.getRisk(rnum)
    data['percentage'] = rnum
    return data


@register.simple_tag
def calculateAvE(self):
    pacientes = self
    data = [
        [],
        []
    ]
    contRangeH1 = 0
    contRangeH2 = 0
    contRangeH3 = 0
    contRangeH4 = 0
    contRangeH5 = 0
    contRangeH6 = 0
    contRangeH7 = 0
    asaRangeH1 = 0
    asaRangeH2 = 0
    asaRangeH3 = 0
    asaRangeH4 = 0
    asaRangeH5 = 0
    asaRangeH6 = 0
    asaRangeH7 = 0
    contRangeM1 = 0
    contRangeM2 = 0
    contRangeM3 = 0
    contRangeM4 = 0
    contRangeM5 = 0
    contRangeM6 = 0
    contRangeM7 = 0
    asaRangeM1 = 0
    asaRangeM2 = 0
    asaRangeM3 = 0
    asaRangeM4 = 0
    asaRangeM5 = 0
    asaRangeM6 = 0
    asaRangeM7 = 0
    for paciente in pacientes:
        edad = paciente.age()
        lipid_test = paciente.examenes.filter(tipo__nombre="Examen Lipídico").order_by('seguimiento').last()
        if lipid_test:
            last_asa = paciente.examenes.filter(tipo__nombre="Test Asa", seguimiento=lipid_test.seguimiento).first()
            if last_asa:
                if last_asa.paciente.genero == 'F':
                    if edad > 17 and edad < 35:
                        asaRangeM1 += last_asa.resultado
                        contRangeM1 += 1
                    if edad > 34 and edad < 40:
                        asaRangeM2 += last_asa.resultado
                        contRangeM2 += 1
                    if edad > 39 and edad < 45:
                        asaRangeM3 += last_asa.resultado
                        contRangeM3 += 1
                    if edad > 44 and edad < 50:
                        asaRangeM4 += last_asa.resultado
                        contRangeM4 += 1
                    if edad > 49 and edad < 55:
                        asaRangeM5 += last_asa.resultado
                        contRangeM5 += 1
                    if edad > 54 and edad < 60:
                        asaRangeM6 += last_asa.resultado
                        contRangeM6 += 1
                    if edad > 59 and edad < 66:
                        asaRangeM7 += last_asa.resultado
                        contRangeM7 += 1
                else:
                    if edad > 17 and edad < 35:
                        asaRangeH1 += last_asa.resultado
                        contRangeH1 += 1
                    if edad > 34 and edad < 40:
                        asaRangeH2 += last_asa.resultado
                        contRangeH2 += 1
                    if edad > 39 and edad < 45:
                        asaRangeH3 += last_asa.resultado
                        contRangeH3 += 1
                    if edad > 44 and edad < 50:
                        asaRangeH4 += last_asa.resultado
                        contRangeH4 += 1
                    if edad > 49 and edad < 55:
                        asaRangeH5 += last_asa.resultado
                        contRangeH5 += 1
                    if edad > 54 and edad < 60:
                        asaRangeH6 += last_asa.resultado
                        contRangeH6 += 1
                    if edad > 59 and edad < 66:
                        asaRangeH7 += last_asa.resultado
                        contRangeH7 += 1
    if contRangeM1 > 0:
        data[1].append((asaRangeM1 / contRangeM1))
    else:
        data[1].append(0)
    if contRangeM2 > 0:
        data[1].append((asaRangeM2 / contRangeM2))
    else:
        data[1].append(0)
    if contRangeM3 > 0:
        data[1].append((asaRangeM3 / contRangeM3))
    else:
        data[1].append(0)
    if contRangeM4 > 0:
        data[1].append((asaRangeM4 / contRangeM4))
    else:
        data[1].append(0)
    if contRangeM5 > 0:
        data[1].append((asaRangeM5 / contRangeM5))
    else:
        data[1].append(0)
    if contRangeM6 > 0:
        data[1].append((asaRangeM6 / contRangeM6))
    else:
        data[1].append(0)
    if contRangeM7 > 0:
        data[1].append((asaRangeM7 / contRangeM7))
    else:
        data[1].append(0)
    if contRangeH1 > 0:
        data[0].append((asaRangeH1 / contRangeH1))
    else:
        data[0].append(0)
    if contRangeH2 > 0:
        data[0].append((asaRangeH2 / contRangeH2))
    else:
        data[0].append(0)
    if contRangeH3 > 0:
        data[0].append((asaRangeH3 / contRangeH3))
    else:
        data[0].append(0)
    if contRangeH4 > 0:
        data[0].append((asaRangeH4 / contRangeH4))
    else:
        data[0].append(0)
    if contRangeH5 > 0:
        data[0].append((asaRangeH5 / contRangeH5))
    else:
        data[0].append(0)
    if contRangeH6 > 0:
        data[0].append((asaRangeH6 / contRangeH6))
    else:
        data[0].append(0)
    if contRangeH7 > 0:
        data[0].append((asaRangeH7 / contRangeH7))
    else:
        data[0].append(0)
    if len(data[0]) == 0:
        data[0] = [0, 0, 0, 0, 0, 0, 0]
    elif len(data[1]) == 0:
        data[1] = [0, 0, 0, 0, 0, 0, 0]
    return data


@register.simple_tag
def calculateRvE(self):
    pacientes = self
    data = [
        [],
        []
    ]
    contRangeH1 = 0
    contRangeH2 = 0
    contRangeH3 = 0
    contRangeH4 = 0
    contRangeH5 = 0
    contRangeH6 = 0
    contRangeH7 = 0
    rcvRangeH1 = 0
    rcvRangeH2 = 0
    rcvRangeH3 = 0
    rcvRangeH4 = 0
    rcvRangeH5 = 0
    rcvRangeH6 = 0
    rcvRangeH7 = 0
    contRangeM1 = 0
    contRangeM2 = 0
    contRangeM3 = 0
    contRangeM4 = 0
    contRangeM5 = 0
    contRangeM6 = 0
    contRangeM7 = 0
    rcvRangeM1 = 0
    rcvRangeM2 = 0
    rcvRangeM3 = 0
    rcvRangeM4 = 0
    rcvRangeM5 = 0
    rcvRangeM6 = 0
    rcvRangeM7 = 0
    for paciente in pacientes:
        edad = paciente.age()
        lipid_test = paciente.examenes.filter(tipo__nombre="Examen Lipídico").order_by('seguimiento').last()
        if lipid_test:
            if paciente.genero == 'F':
                if edad > 17 and edad < 35:
                    rcvRangeM1 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeM1 += 1
                if edad > 34 and edad < 40:
                    rcvRangeM2 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeM2 += 1
                if edad > 39 and edad < 45:
                    rcvRangeM3 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeM3 += 1
                if edad > 44 and edad < 50:
                    rcvRangeM4 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeM4 += 1
                if edad > 49 and edad < 55:
                    rcvRangeM5 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeM5 += 1
                if edad > 54 and edad < 60:
                    rcvRangeM6 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeM6 += 1
                if edad > 59 and edad < 66:
                    rcvRangeM7 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeM7 += 1
            else:
                if edad > 17 and edad < 35:
                    rcvRangeH1 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeH1 += 1
                if edad > 34 and edad < 40:
                    rcvRangeH2 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeH2 += 1
                if edad > 39 and edad < 45:
                    rcvRangeH3 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeH3 += 1
                if edad > 44 and edad < 50:
                    rcvRangeH4 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeH4 += 1
                if edad > 49 and edad < 55:
                    rcvRangeH5 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeH5 += 1
                if edad > 54 and edad < 60:
                    rcvRangeH6 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeH6 += 1
                if edad > 59 and edad < 66:
                    rcvRangeH7 += paciente.calculateRCVCount(lipid_test.seguimiento)
                    contRangeH7 += 1
    if contRangeM1 > 0:
        data[1].append((rcvRangeM1 / contRangeM1))
    else:
        data[1].append(0)
    if contRangeM2 > 0:
        data[1].append((rcvRangeM2 / contRangeM2))
    else:
        data[1].append(0)
    if contRangeM3 > 0:
        data[1].append((rcvRangeM3 / contRangeM3))
    else:
        data[1].append(0)
    if contRangeM4 > 0:
        data[1].append((rcvRangeM4 / contRangeM4))
    else:
        data[1].append(0)
    if contRangeM5 > 0:
        data[1].append((rcvRangeM5 / contRangeM5))
    else:
        data[1].append(0)
    if contRangeM6 > 0:
        data[1].append((rcvRangeM6 / contRangeM6))
    else:
        data[1].append(0)
    if contRangeM7 > 0:
        data[1].append((rcvRangeM7 / contRangeM7))
    else:
        data[1].append(0)
    if contRangeH1 > 0:
        data[0].append((rcvRangeH1 / contRangeH1))
    else:
        data[0].append(0)
    if contRangeH2 > 0:
        data[0].append((rcvRangeH2 / contRangeH2))
    else:
        data[0].append(0)
    if contRangeH3 > 0:
        data[0].append((rcvRangeH3 / contRangeH3))
    else:
        data[0].append(0)
    if contRangeH4 > 0:
        data[0].append((rcvRangeH4 / contRangeH4))
    else:
        data[0].append(0)
    if contRangeH5 > 0:
        data[0].append((rcvRangeH5 / contRangeH5))
    else:
        data[0].append(0)
    if contRangeH6 > 0:
        data[0].append((rcvRangeH6 / contRangeH6))
    else:
        data[0].append(0)
    if contRangeH7 > 0:
        data[0].append((rcvRangeH7 / contRangeH7))
    else:
        data[0].append(0)
    if len(data[0]) == 0:
        data[0] = [0, 0, 0, 0, 0, 0, 0]
    elif len(data[1]) == 0:
        data[1] = [0, 0, 0, 0, 0, 0, 0]
    return data
