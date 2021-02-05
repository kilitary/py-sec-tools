rule _PNG_Graphics_format_yseqtz
{
	meta:
		description = "PNG Graphics format"
	strings:
		$a = {89504E470D0A1A0A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
