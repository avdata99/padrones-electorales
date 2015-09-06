
# extraer cada pagina a imagen (formato OBM)
echo "Extrayendo imagenes del PDF" 
pdfimages -l 1 ELECTORAL\ MENDIOLAZA\ X.pdf images/padron
cd images

# partir cada imagen en dos columnas

# -density 288
# -threshold 50% 
# -colorspace Gray 
# -depth 8 
# -resample 200x200
for i in *pbm; do echo "Partiendo $i"; convert $i  -crop 50%x100% +repage $i.png ; done

# gOCR apesta
echo "Haciendo tesseract OCR sobre las páginas"
for i in *png; do echo tesseract $i; tesseract $i $i -l spa; done


