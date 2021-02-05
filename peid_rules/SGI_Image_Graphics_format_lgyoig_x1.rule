rule _SGI_Image_Graphics_format_lgyoig
{
	meta:
		description = "SGI Image Graphics format"
	strings:
		$a = {01DA00010003}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
