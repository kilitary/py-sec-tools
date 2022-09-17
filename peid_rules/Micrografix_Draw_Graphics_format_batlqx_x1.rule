rule _Micrografix_Draw_Graphics_format_batlqx
{
	meta:
		description = "Micrografix Draw Graphics format"
	strings:
		$a = {01FF020403020002}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
