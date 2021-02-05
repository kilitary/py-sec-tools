rule _GIF89a_Graphics_format_riukja
{
	meta:
		description = "GIF89a Graphics format"
	strings:
		$a = {474946383961}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
