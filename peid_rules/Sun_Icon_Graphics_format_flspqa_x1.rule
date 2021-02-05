rule _Sun_Icon_Graphics_format_flspqa
{
	meta:
		description = "Sun Icon Graphics format"
	strings:
		$a = {2F2A20466F726D61745F76657273696F6E3D312C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
