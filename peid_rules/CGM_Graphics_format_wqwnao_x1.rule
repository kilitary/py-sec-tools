rule _CGM_Graphics_format_wqwnao
{
	meta:
		description = "CGM Graphics format"
	strings:
		$a = {002A0848694A61616B2032}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
