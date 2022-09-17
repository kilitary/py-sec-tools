rule _IBM_IOCA_Graphics_format_zwhycg
{
	meta:
		description = "IBM IOCA Graphics format"
	strings:
		$a = {0011D3A6FB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
