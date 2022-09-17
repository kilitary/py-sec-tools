rule _Windows_Icon_Graphics_format_baxtem
{
	meta:
		description = "Windows Icon Graphics format"
	strings:
		$a = {00000100}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
