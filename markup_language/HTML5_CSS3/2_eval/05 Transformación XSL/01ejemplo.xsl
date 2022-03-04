<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" >
  <xsl:template match="/">
    <html>
    <head>
      <style>
      table {border-collapse: collapse;}
      th { border:2px red solid;}
        td { text-align:center; border:2px red solid;}
      </style>
    </head>
    <body>
    <h1>Mi biblioteca</h1>
    <table>
      <tr><th>Título</th><th>Autor</th></tr>
      <xsl:for-each select="libreria/libro">
      <tr>
          <td><xsl:value-of select="titulo"/></td>
          <td><xsl:value-of select="autor"/></td>
      </tr>     
      </xsl:for-each>
    </table>
    </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
