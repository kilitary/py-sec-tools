rule _JEDMICS_CCITT4_Graphics_format_houngt
{
	meta:
		description = "JEDMICS CCITT4 Graphics format"
	strings:
		$a = {80000000??????00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
