# Generated by Django 2.2.17 on 2021-01-25 20:09

from django.db import migrations


def add_crm_letters(apps, schema_editor):
    ResponseTemplate = apps.get_model('cts_forms', 'ResponseTemplate')
    subject = 'Response: Your Civil Rights Division Report - {{ record_locator }} from {{ section_name }} Section'
    ResponseTemplate.objects.create(
        title='CRM - R1 Form Letter',
        subject=subject,
        body="""
{{ addressee }},

You contacted the Department of Justice on {{ date_of_intake }}. Your report number is {{ record_locator }}. The Civil Rights Division relies on information from community members to identify potential civil rights violations. The Federal Bureau of Investigation and other law enforcement agencies conduct investigations for the Division. Therefore, you may want to contact your local FBI office or visit www.FBI.gov.

The Criminal Section is one of several Sections in the Civil Rights Division of the U.S. Department of Justice. We are responsible for enforcing federal criminal civil rights statutes. The Criminal Section prosecutes criminal cases involving:

- Civil rights violations by persons acting under color of law, such as federal, state, or other police officers or corrections officers;
- Hate crimes;
- Force or threats intended to interfere with religious activities because of their religious nature;
- Force or threats intended to interfere with providing or obtaining reproductive health services and
- Human trafficking in the form of coerced labor or commercial sex.

We cannot help you recover damages or seek any other personal relief. We also cannot assist you in ongoing criminal cases, including wrongful convictions, appeals, or sentencing. For more detailed information about the Criminal Section or the work we do, please visit our web page: www.justice.gov/crt/about/crm/.

We will review your letter to decide whether it is necessary to contact you for additional information. We do not have the resources to follow-up on or reply to every letter. If your concern is not within this Section’s area of work, you may wish to consult the Civil Rights Division web page to determine whether another Section of the Division may be able to address your concerns: www.justice.gov/crt. Again, if you are writing to report a crime, please contact the federal and/or state law enforcement agencies in your local area, such as the Federal Bureau of Investigation or your local police department or sheriff’s office.

Sincerely,
/s/
The Criminal Section
""")
    ResponseTemplate.objects.create(
        title='CRM - R2 Form Letter',
        subject=subject,
        body="""
{{ addressee }},

You contacted the Civil Rights Division on {{ date_of_intake }}. Your report number is {{ record_locator }}.

The Criminal Section of the Civil Rights Division is responsible for enforcing federal criminal civil rights statutes. Much of our enforcement activity relates to the investigation and prosecution of deprivations of civil rights under color of law. These matters generally involve allegations of excessive physical force or sexual abuse by law enforcement officers.

The information that you furnished is insufficient to permit us to determine the existence of a possible violation of federal criminal civil rights statutes. Therefore, we are unable to authorize an investigation of your complaint at this time. However, we will consider the allegation further if you provide specific information concerning the circumstances involved in your complaint. You should include the name of the person injured; a narrative involving the allegations leading up to and including the incident; the name of any possible witness; the date of the incident and any other information you deem relevant to this incident. Please resubmit this information to our online complaint portal https://civilrights.justice.gov/ and reference your complaint number, listed in the subject line of this email.

You can be assured that if the evidence shows there was a prosecutable violation of a federal criminal civil rights statute, appropriate action will be taken.

Thank you,
/s/
The Criminal Section
""")

    subject_es = 'Respuesta: Su informe de la División de Derechos Civiles - {{ record_locator }} de la Sección {{ es.section_name }}'
    ResponseTemplate.objects.create(
        title='CRM - R1 Form Letter (Spanish)',
        subject=subject_es,
        body="""
{{ es.addressee }}:

Usted se comunicó con el Departamento de Justicia el {{ es.date_of_intake }}. Su número de informe es {{ record_locator }}. La División de Derechos Civiles depende de la información que proporcionan los miembros comunitarios para identificar posibles vulneraciones de derechos civiles.El Buró Federal de Investigaciones y otras agencias encargadas de hacer cumplir la ley realizan investigaciones para la División. Por lo tanto, puede comunicarse con su oficina local del FBI o ir a www.FBI.gov.

La Sección Penal es una de varias secciones de la División de Derechos Civiles del Departamento de Justicia de los EE. UU. Somos responsables de hacer cumplir las leyes penales federales de derechos civiles.La Sección Penal enjuicia casos penales relacionados con:

- Vulneraciones de derechos civiles por personas que actúan con apariencia de legalidad, tales como agentes policiales o penitenciarios federales, estatales u otros;
- Delitos de odio;
- La fuerza o amenazas cuya intención es interferir en las actividades religiosas por motivo de su carácter religioso;
- La fuerza o amenazas cuya intención es interferir en la provisión u obtención de servicios de salud reproductiva y
- La trata de personas en forma de trabajo forzoso o sexo comercial.

No podemos ayudarle a recuperar daños o a buscar cualquier otra compensación personal. Tampoco podemos ayudarle con casos penales en curso, los que incluyen condenas injustas, apelaciones o sentencias. Para más información sobre la Sección Penal o el trabajo que realizamos, visite nuestro sitio web: https://www.justice.gov/crt-espanol/crm.

Nosotros revisaremos su carta para determinar si debemos comunicarnos con usted para pedir información adicional. No tenemos suficientes recursos como para dar seguimiento o responder a cada carta. Si su pregunta o inquietud no está relacionada con los asuntos de los cuales se encarga esta Sección, puede revisar la página web de la División de Derechos Civiles para determinar si tal vez otra sección de la División podría abordar sus inquietudes: https://www.justice.gov/crt-espanol. Le recordamos que, si nos ha escrito para informarnos de algún delito, favor de comunicarse con las agencias federales o estatales encargadas de hacer cumplir la ley en su zona local, o bien su policía u Oficina del Alguacil local.

Atentamente,
/s/
La Sección Penal
""")
    subject_es = 'Respuesta: Su informe de la División de Derechos Civiles - {{ record_locator }} de la Sección {{ es.section_name }}'
    ResponseTemplate.objects.create(
        title='CRM - R2 Form Letter (Spanish)',
        subject=subject_es,
        body="""
{{ es.addressee }}:

Usted se comunicó con la División de Derechos Civiles el {{ es.date_of_intake }}. Su número de informe es {{ record_locator }}.

La Sección Penal de la División de Derechos Civiles es responsable de hacer cumplir las leyes penales federales de derechos civiles. Buena parte de nuestras medidas de aplicación están relacionadas con la investigación y el enjuiciamiento de privaciones de derechos civiles con apariencia de legalidad. Estos asuntos generalmente conllevan alegatos de fuerza física excesiva o abuso sexual por parte de agentes del orden público.

La información que usted proporcionó no es suficiente como para permitirnos determinar si existe una posible vulneración de las leyes penales federales de derechos civiles. Por consiguiente, en este momento no podemos autorizar una investigación de su querella. No obstante, si nos puede brindar información específica acerca de las circunstancias que llevaron a su querella, podremos recontemplar la alegación. Usted debe incluir el nombre de la persona afectada; una descripción de las alegaciones antes y durante el incidente; el nombre de cualquier testigo que pueda haber; la fecha del incidente y cualquier otra información que usted estime que es relevante a este incidente. Por favor vuelva a entregar esta información en nuestro portal de querellas en línea en https://civilrights.justice.gov/, anotando su número de querella, que aparece en la línea de asunto de este correo electrónico. Para acceder al portal en español, desplácese hasta el final de la página principal y seleccione español en la pestaña de idioma.

Le garantizamos que si las pruebas muestran que hubo una vulneración enjuiciable de alguna ley penal federal de derechos civiles, se tomarán las medidas apropiadas.

Gracias,
/s/
La Sección Penal
""")


def remove_crm_letters(apps, schema_editor):
    ResponseTemplate = apps.get_model('cts_forms', 'ResponseTemplate')
    templates = ResponseTemplate.objects.filter(title__icontains='CRM - R1')
    templates.delete()
    templates = ResponseTemplate.objects.filter(title__icontains='CRM - R2')
    templates.delete()



class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0097_create_email_count_view_caseinsensitive'),
    ]

    operations = [
        migrations.RunPython(add_crm_letters, remove_crm_letters)
    ]
