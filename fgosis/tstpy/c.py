import pdfcrowd
from django.http import HttpResponse

def generate_pdf_view(request):
    try:
        # create an API client instance
        client = pdfcrowd.Client("susahe", "31184c7f95430a5d528990c4a421a9c2")

        # convert a web page and store the generated PDF to a variable
        pdf = client.convertURI("http://www.google.com")

         # set HTTP response headers
        response = HttpResponse(mimetype="application/pdf")
        response["Cache-Control"] = "max-age=0"
        response["Accept-Ranges"] = "none"
        response["Content-Disposition"] = "attachment; filename=google_com.pdf"

        # send the generated PDF
        response.write(pdf)
    except pdfcrowd.Error, why:
        response = HttpResponse(mimetype="text/plain")
        response.write(why)
    return response