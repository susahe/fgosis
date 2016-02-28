from django.shortcuts import render
from  reportlab.pdfgen import canvas
from django.http import HttpResponse

def pdf_doc(request):
	# create the Httpresponse object wtih the appropriate pdf Headers
	response = HttpResponse(content_type = 'application/pdf')
	response['Content-Dispostion'] = 'attachment; filename = "a.pdf'

	p = canvas.Canvas(response)

	p.drawString(100,100,"Hello man .")
	p.showPage()
	p.save()
	return response
