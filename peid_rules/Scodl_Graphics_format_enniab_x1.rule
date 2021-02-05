rule _Scodl_Graphics_format_enniab
{
	meta:
		description = "Scodl Graphics format"
	strings:
		$a = {E001??00????00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
