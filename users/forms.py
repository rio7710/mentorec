from django import forms

class FileUploadForm(forms.Form):
    excel_file = forms.FileField(label="엑셀 파일")