rule _Erdas_LANGIS_Image_graphics_format_wprbat
{
	meta:
		description = "Erdas LANGIS Image graphics format"
	strings:
		$a = {48454144373400000300}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
