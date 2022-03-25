<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <xsl:template match="ciclos">
    <html>
    <head>
    <style>
    table {border-collapse: collapse;}
       td {border:2px solid red;}
    </style>
    </head>
    <body>
    <table>
      <tr><th>Ciclos</th></tr>
      <xsl:apply-templates />
    </table>
    </body>
    </html>
  </xsl:template>

  <xsl:template match="ciclo">
    <tr>
      <td><xsl:value-of select="nombre"/></td>
    </tr>
  </xsl:template>

</xsl:stylesheet>
