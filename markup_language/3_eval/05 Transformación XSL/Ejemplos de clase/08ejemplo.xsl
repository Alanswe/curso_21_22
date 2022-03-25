<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"> 
<xsl:template match="ventas">
<html>
<head>
</head>
<body>

<table>

  <tr><th>Denominación</th><th>País</th></tr>

<xsl:apply-templates/>

</table>

</body>
</html>
   </xsl:template>
<!-- fin -->

  <xsl:template match="producto">
    <tr>
      <td><xsl:value-of select="denominacion"/></td>
    </tr>
</xsl:template>
</xsl:stylesheet>
