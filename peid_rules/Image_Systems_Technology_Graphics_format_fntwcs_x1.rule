rule _Image_Systems_Technology_Graphics_format_fntwcs
{
	meta:
		description = "Image Systems Technology Graphics format"
	strings:
		$a = {033A????00??0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
