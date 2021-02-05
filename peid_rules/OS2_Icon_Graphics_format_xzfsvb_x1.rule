rule _OS2_Icon_Graphics_format_xzfsvb
{
	meta:
		description = "OS2 Icon Graphics format"
	strings:
		$a = {43494E000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
