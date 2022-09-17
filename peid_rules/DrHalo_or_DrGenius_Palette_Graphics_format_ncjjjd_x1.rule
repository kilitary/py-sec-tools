rule _DrHalo_or_DrGenius_Palette_Graphics_format_ncjjjd
{
	meta:
		description = "DrHalo or DrGenius Palette Graphics format"
	strings:
		$a = {4148E30000000A00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
