
# API OCR

Servicio para extraccion de informacion (texto) de pdf con estructuras complejas (forms, img, etc.)

## Instrucciones

Enviar un request, en ***Form-Data***, donde el campo del archivo sea llamado **file**.

La respuesta seguira la siguiente estructura

```
{
	"text": "TEXT_EXTRAIDO_DEL_DOCUMENTO"
}
```
