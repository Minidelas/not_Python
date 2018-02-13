##############################################################################
#
# A simple example of some of the features of the XlsxWriter Python module.
#
# Copyright 2013-2016, John McNamara, jmcnamara@cpan.org
#
# Add a bold format to use to highlight cells.
# bold = workbook.add_format({'bold': True})

# Write some simple text.
# worksheet.write('A1', 'Hello')

# Text with formatting.
# worksheet.write('A2', 'World', bold)

import xlsxwriter
import random

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet('Test Formulas')

# Widen the first column to make the text clearer.
worksheet.set_column('A:B', 20)
aux = 0
# Write some numbers, with row/column notation.
for value in range(20):
    aux = value+1
    worksheet.write('A'+str(aux), random.randint(1, 100))
    pass

worksheet.write('B1', 'Total')
worksheet.write_formula('B2', '=SUM(A1:A'+str(aux)+')')

workbook.close()
