rule _DrHalo_or_DrGenius_Image_Graphics_format_mtlmsc
{
	meta:
		description = "DrHalo or DrGenius Image Graphics format"
	strings:
		$a = {????3A030000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
