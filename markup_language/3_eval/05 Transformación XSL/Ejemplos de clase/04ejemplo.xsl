<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
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
        <h1>Catálogo</h1>
        <table>
          <tr>
            <th>Código</th>
            <th>Nombre</th>
            <th>Precio</th>
          </tr>
          <xsl:for-each select="productos/producto">
            <tr>
                  <td><xsl:value-of select="@pid"/></td>
                  <td><xsl:value-of select="nombre"/></td>
                  <td><xsl:value-of select="@precio"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
