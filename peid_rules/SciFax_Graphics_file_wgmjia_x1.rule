rule _SciFax_Graphics_file_wgmjia
{
	meta:
		description = "SciFax Graphics file"
	strings:
		$a = {44543D00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
