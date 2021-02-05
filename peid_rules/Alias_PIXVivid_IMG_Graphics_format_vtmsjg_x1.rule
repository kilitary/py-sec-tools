rule _Alias_PIXVivid_IMG_Graphics_format_vtmsjg
{
	meta:
		description = "Alias PIXVivid IMG Graphics format"
	strings:
		$a = {????????0000????0018????????01}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
