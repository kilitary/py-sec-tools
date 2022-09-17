rule _Lotus_Graphics_format_ixhtph
{
	meta:
		description = "Lotus Graphics format"
	strings:
		$a = {0100000001000800}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
