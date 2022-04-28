from PIL import Image, ImageFont, ImageDraw 
from datetime import datetime, timedelta

today = datetime.now()
today_str = today.strftime("%d/%m/%Y")
next_week_str = (today + timedelta(days = 7)).strftime("%d/%m/%Y")
fixed_cnpj = '12.3456.789/0001-99'
fixed_bank_branch_and_code = '1234/123456'

# Abrir o boleto "base"
base_boleto = Image.open('base_boleto.jpg')

# Escolha da fonte
title_font = ImageFont.truetype('Lato-Regular.ttf', 13)

# Variável de interação com a imagem
image_editable = ImageDraw.Draw(base_boleto)

# Printando Data de Documento e Data de Processamento
image_editable.text((32,160), today_str, (0, 0, 0), font=title_font)
image_editable.text((475,160), today_str, (0, 0, 0), font=title_font)

# Printando Data de Vencimento
image_editable.text((640,85), next_week_str, (0, 0, 0), font=title_font)

# Printando CNPJ
image_editable.text((475,123), fixed_cnpj, (0, 0, 0), font=title_font)

# Printando Agência e Código de Cedente
image_editable.text((640,123), fixed_bank_branch_and_code, (0, 0, 0), font=title_font)

base_boleto.save("result.pdf")