import PyPDF2
import csv
import re
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def Converte_pdf_para_texto(file_path):

	output_string = StringIO()
	with open(file_path, 'rb') as in_file:
	    parser = PDFParser(in_file)
	    doc = PDFDocument(parser)
	    rsrcmgr = PDFResourceManager()
	    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
	    interpreter = PDFPageInterpreter(rsrcmgr, device)
	    for page in PDFPage.create_pages(doc):
	        interpreter.process_page(page)

	in_file.close()
	return(output_string.getvalue())

def Tratamento_texto(dados):
    nome=''
    rua=''
    bairro=''
    cep=''
    estado=''
    uf=''
    valor_fatura_atual=''
    valot_fatura_anterior=''
    data_vencimento=''
    data_postagem=''
    index=0
    texto_sep=dados.split('\n')
    for line in texto_sep:
        
        busca_1=re.search(r'([0-9]{5}-[0-9]{3})(.*)',line)
        busca_2=re.search(r'Data de Vencimento',line)
        index+=1
        if busca_2:
            print("Valor encontrado.")    
        if busca_1:
            cep=busca_1.group(1).strip()
            uf=busca_1.group(2).strip()[-2:]
            estado=busca_1.group(2).strip()[:-2]
            rua=texto_sep[index-3].strip()
            bairro=texto_sep[index-2].strip()
            nome=texto_sep[index-4].strip()
            print(f"Nome: {nome}\nRua: {rua}\nBairo: {bairro}\nCep: {cep}\nBairro: {bairro}\nUF: {uf}")

		

# text=Converte_pdf_para_texto('fatura.pdf')
# Tratamento_texto(text)

# Testes com Regex
lista=['04194-360','felipe','1195393-2216','Felipe Maciel','teste','444,057,988-42',2321323]
# a=re.search(r'([0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2})(.*)','444.057.988-42 ssdsdas')
a=re.search(r'([a-z]{6}\s(de)\s[a-z]{6})','felipe de maciel')
if a:
    print("Verdadeiro")
else:
    print("Falso")    
    


 
   