from io import BytesIO
from django.shortcuts import render
from  reportlab.pdfgen import canvas
from django.http import HttpResponse

def pdf_doc(request):
	# create the Httpresponse object wtih the appropriate pdf Headers
	response = HttpResponse(content_type = 'application/pdf')
	response['Content-Dispostion'] = 'attachment; filename = "a.pdf'

	buffer = BytesIO()

    	# Create the PDF object, using the BytesIO object as its "file."
    	p = canvas.Canvas(buffer)

   	 # Draw things on the PDF. Here's where the PDF generation happens.
    	# See the ReportLab documentation for the full list of functionality.
   	p.drawString(100, 100, "Hello world.")

   	 # Close the PDF object cleanly.
    	p.showPage()
    	p.save()

    	# Get the value of the BytesIO buffer and write it to the response.
    	pdf = buffer.getvalue()
    	buffer.close()
    	response.write(pdf)
    	return response

def index(request):
  
  
  
  
        return HttpResponse("Rango Sasy hey there world <br/> <a href='/rango/about'>About </a>")