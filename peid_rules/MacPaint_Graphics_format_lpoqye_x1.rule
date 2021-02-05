rule _MacPaint_Graphics_format_lpoqye
{
	meta:
		description = "MacPaint Graphics format"
	strings:
		$a = {00000002FFFFFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
