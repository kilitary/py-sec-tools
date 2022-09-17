rule _Windows_or_OS2_Graphics_format_zkxwin
{
	meta:
		description = "Windows or OS2 Graphics format"
	strings:
		$a = {424D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
