rule _Amiga_IFFILBM_Graphics_format_przukj
{
	meta:
		description = "Amiga IFFILBM Graphics format"
	strings:
		$a = {464F524D????????494C424D424D4844}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
