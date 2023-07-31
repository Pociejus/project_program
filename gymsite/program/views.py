from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Program, ProgramDay
from django.template.loader import get_template
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm



def program_list(request):
    # Gaukite visus Program objektus
    programs = Program.objects.all()
    return render(request, 'program_list.html', {'programs': programs})

def program_days(request, program_id):
    # Gaukite Program objektą pagal program_id
    program = get_object_or_404(Program, id=program_id)

    # Gaukite visus ProgramDay objektus susijusius su šia programa
    program_days = program.programday_set.all()

    return render(request, 'program_days.html', {'program': program, 'program_days': program_days})


def generate_program_day_pdf(request, programday_id):
    # Gaukite ProgramDay objektą pagal programday_id
    try:
        programday = ProgramDay.objects.get(id=programday_id)
    except ProgramDay.DoesNotExist:
        return HttpResponse("ProgramDay not found.", status=404)

    # Nustatome puslapio dydį ir kraštinių paraštę
    page_width, page_height = letter
    left_margin = 1.5 * cm
    right_margin = 1.5 * cm
    top_margin = 1.5 * cm
    bottom_margin = 1.5 * cm

    # Sukurkite naują PDF dokumentą
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    # Įtraukite informaciją apie ProgramDay į PDF dokumentą
    pdf.drawString(left_margin, page_height - top_margin, f"Programos diena: {programday.day_number}")
    pdf.drawString(left_margin, page_height - top_margin - 20, f"Programa: {programday.program}")
    pdf.drawString(left_margin, page_height - top_margin - 40, "Pratimai:")
    pdf.drawString(left_margin, page_height - top_margin - 60, "--------------")
    y = page_height - top_margin - 80

    # Įtraukite informaciją apie pratimus į PDF dokumentą
    for exercise in programday.exercise.all():
        pdf.drawString(left_margin, y, f"{exercise.name}")
        pdf.drawString(left_margin, y - 20, f"Serijos: {exercise.sets}, Pakartojimai: {exercise.reps}")
        if exercise.image:
            image_path = exercise.image.path
            img = Image.open(image_path)
            img.thumbnail((50, 50))
            pdf.drawImage(ImageReader(img), page_width - right_margin - 50, y - 30, width=50, height=50)
        y -= 50

    # Įtraukite informaciją apie streches į PDF dokumentą
    pdf.drawString(left_margin, y, "------------")
    pdf.drawString(left_margin, y - 20, "Tempimo pratimai:")
    y -= 40

    for strech in programday.strech.all():
        pdf.drawString(left_margin, y, f"{strech.name}")
        pdf.drawString(left_margin, y - 20, f"Serijos: {strech.sets}, pakarotojimai: {strech.reps} sek.")
        if strech.image:
            image_path = strech.image.path
            img = Image.open(image_path)
            img.thumbnail((50, 50))
            pdf.drawImage(ImageReader(img), page_width - right_margin - 50, y - 30, width=50, height=50)
        y -= 50

    # Išsaugokite PDF dokumentą
    pdf.save()

    # Nustatykite atsakymo turinį ir tipą
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="program_day_{programday.day_number}.pdf"'

    # Įrašykite PDF dokumento turinį į atsakymą
    buffer.seek(0)
    response.write(buffer.read())

    return response