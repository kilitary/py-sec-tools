rule _GIF89a_Graphics_format_ueiwnv
{
	meta:
		description = "GIF89a Graphics format"
	strings:
		$a = {474946383961}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
