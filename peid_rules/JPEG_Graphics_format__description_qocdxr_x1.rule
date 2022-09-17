rule _JPEG_Graphics_format__description_qocdxr
{
	meta:
		description = "JPEG Graphics format _ description"
	strings:
		$a = {FFD8FFFE0027}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
