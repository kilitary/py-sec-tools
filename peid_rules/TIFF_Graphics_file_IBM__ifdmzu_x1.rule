rule _TIFF_Graphics_file_IBM__ifdmzu
{
	meta:
		description = "TIFF Graphics file _IBM_"
	strings:
		$a = {49492A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
