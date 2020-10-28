import io

from django.http import HttpResponse

from reportlab.pdfgen import canvas

from .models import Clientes
from django.views.generic import ListView


class ClientList(ListView):
    model = Clientes


def pdf_reportlab(request):
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 810, "Hello world.")

    palavras = ['palavra', 'palavra', 'palavra']

    y = 790

    for palavra in palavras:
        p.drawString(10, y, palavra)
        y -= 40

        # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


def pdf_clientes(request):
    response = HttpResponse(content_type='application/pdf')

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(200, 810, "RELATÓRIO DE CLIENTES")
    p.drawString(0, 800, "_" * 150)

    clientes = Clientes.objects.all()

    y = 750

    for cliente in clientes:
        str = f'Cliente - {cliente.nome_razao_social} | E-mail {cliente.email} | Celular {cliente.celular}'
        p.drawString(10, y, str)
        y -= 20

        # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
