from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Program, ProgramDay, UserProfile
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime


def program_list(request):
    # Gaunam visus Program objektus
    programs = Program.objects.all()
    return render(request, 'program_list.html', {'programs': programs})


def program_days(request, program_id):
    # Gaunam Program objektą pagal program_id
    program = get_object_or_404(Program, id=program_id)

    # Gaunam visus ProgramDay objektus tai programai. Dėl many to many naudojam _set.all()
    program_days = program.programday_set.all()

    return render(request, 'program_days.html', {'program': program, 'program_days': program_days})


def generate_program_day_pdf(request, programday_id):
    # Gaunam ProgramDay objektą pagal programday_id (vietoj try ecxept)
    programday = get_object_or_404(ProgramDay, id=programday_id)

    # Nustatome puslapio dydį ir kraštines
    page_width, page_height = letter  # letter yra konstanta 21,59x27,94 cm
    left_margin = 1.5 * cm
    right_margin = 1.5 * cm
    top_margin = 1.5 * cm
    bottom_margin = 1.5 * cm

    # Sukuriam naują PDF failą
    buffer = BytesIO()  # Įrašom į laikiną objektą kol atspausdinsim
    pdf = canvas.Canvas(buffer, pagesize=letter)  # default parametras, sukuria PDF dokumentą

    # priregistruojam naują šriftą su LT raidėm
    pdfmetrics.registerFont(
        TTFont('Arial', 'Arial.ttf'))

    # nustatome Arial srifta kaip pagrindini
    pdf.setFont('Arial', 12)

    # Antraštė
    pdf.drawString(left_margin, page_height - top_margin, f"Programos diena: {programday.day_number}")
    pdf.drawString(left_margin, page_height - top_margin - 20, f"Programa: {programday.program}")
    pdf.drawString(left_margin, page_height - top_margin - 40, "-------------- Pratimai:     --------------")
    y = page_height - top_margin - 60

    # Jėgos pratimai
    for exercise in programday.exercise.all():
        pdf.drawString(left_margin, y, f"{exercise.name}")
        pdf.drawString(left_margin, y - 20, f"Serijos: {exercise.sets}, Pakartojimai: {exercise.reps}")
        if exercise.image:
            image_path = exercise.image.path
            img = Image.open(image_path)
            img.thumbnail((200, 200))
            pdf.drawImage(ImageReader(img), page_width - right_margin - 50, y - 30, width=50, height=50)
        y -= 50

    # Tempimo pratimai
    pdf.drawString(left_margin, y, "------------ Tempimo pratimai:  ------------")
    y -= 20

    for strech in programday.strech.all():
        pdf.drawString(left_margin, y, f"{strech.name}")
        pdf.drawString(left_margin, y - 20, f"Serijos: {strech.sets}, užlaikymas: {strech.reps} sek.")
        if strech.image:
            image_path = strech.image.path
            img = Image.open(image_path)
            img.thumbnail((200, 200))
            pdf.drawImage(ImageReader(img), page_width - right_margin - 50, y - 30, width=50, height=50)
        y -= 50

    # Išsaugom PDF dokumentą kaip buferio objektą tik
    pdf.save()

    # Nustatykite atsakymo turinį ir tipą
    response = HttpResponse(content_type='application/pdf')  # HTTP atsakymas su PDF turinio tipu
    # Nurodom kaip apdoroti atsakymo turinį. Siųstis kaip priedą pavadinimu =
    response[
        'Content-Disposition'] = f'attachment; filename="{programday.user} programos diena{programday.day_number}.pdf"'

    # Įrašom turinį iš bufferio BytesIO į PDF
    buffer.seek(0)  # paimam nuo nulinio visą turinį.(skaitymo vietos pradžia)
    response.write(buffer.read())  # nuskaitom turinį iš buferio ir įrašo į atsakymo turinį.

    return response  # gražinamas atsakymas su PDF turiniu išsaugojimui.


def client_list(request):
    # Gaunam visus userprofile objektus
    clients = UserProfile.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


def client_detail(request, user_id):
    # Gauname UserProfile objektą pagal nurodytą user_id
    client = get_object_or_404(UserProfile, user_id=user_id)

    # Skaičiuojame kliento amžių pagal gimimo datą
    birth_date = client.birth
    today = datetime.today().date()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    # skaičiuojam pulso zonas pagal amžių
    max_hr = 220 - age
    zone2 = round(max_hr * 0.6)
    zone3 = round(max_hr * 0.7)
    zone4 = round(max_hr * 0.8)
    zone5 = round(max_hr * 0.9)
    # skaičiuojam KMI
    kmi = round(client.weight/(client.height **2))
    if kmi <18.5 :
        tekstas = 'Indeksas žemiau normos, reikia derinti sportą ir mitybą masės didinimui'
    elif 18.5 <= kmi <= 25:
        tekstas = 'Indeksas normalus'
    elif 25 < kmi <= 30:
        tekstas = 'Indeksas nežymiai virsyja normalų, derinti mitybą masės mažinimui'
    elif kmi > 30 :
        tekstas = 'Indeksas per didėlis, reikalinga derinti mitybą su fiziniu aktyvumu'

    context = {'client': client, 'age': age, 'max_hr': max_hr, 'zone2': zone2, 'zone3': zone3, 'zone4': zone4,
               'zone5': zone5, 'KMI': kmi, 'tekstas': tekstas}
    return render(request, 'client_detail.html', context)
