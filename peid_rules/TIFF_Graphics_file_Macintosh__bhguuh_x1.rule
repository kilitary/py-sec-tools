rule _TIFF_Graphics_file_Macintosh__bhguuh
{
	meta:
		description = "TIFF Graphics file _Macintosh_"
	strings:
		$a = {4D4D00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
