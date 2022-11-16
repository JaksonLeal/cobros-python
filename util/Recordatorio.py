#DEV 1/NOV/2022 JAKSON LEAL

def mensaje (numWhatsapp, name, correoDestino, direccion, txtValor, deuda):

    message = ('Señor (a)\n'
        '%s' % str(name).upper() +'\n'
        'Dir.: %s' % (direccion) +'\n'
        'Tel:   %s' % (numWhatsapp) +'\n'
        'Email: %s' % (correoDestino) +'\n'
        'Ciudad.\n'
        '\n'
        'Buen día.\n'
        '\n'
        'Escribe Deiber Larios, Abogado & Analista Jurídico de la empresa SÚPERGIROS, mediante el presente mensaje se recuerda deuda a su nombre registrada en el sistema de la compañía por la suma de %s' % (txtValor)+' M/CTE ($ %s'% (format(int(deuda), ',d')) +')\n' 
        'Así las cosas, y con la finalidad de precaver la iniciación de las acciones legales en su contra le hacemos un llamado para que en esta etapa realice abonos o dar inicio a un acuerdo de pago evitando reportes negativos en centrales de riesgos, demandas, embargos y cobros reiterativos mediante llamadas o correos.\n'
        'En caso de realizar abonos acercarse a un punto principal de SUPERGIROS bajo el concepto "abono a faltante" con su número de cédula y esperar el soporte de pago.\n'
        'Favor enviar soportes de pago a los siguientes medios: prueba@ejemplo.co – Y/O al abonado telefónico 333 111 2222 – indicando su nombre completo y numero de cedula.')

    return message
    