rule _AVHRR_Graphics_format_eojzeq
{
	meta:
		description = "AVHRR Graphics format"
	strings:
		$a = {D5C8000100030001}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
