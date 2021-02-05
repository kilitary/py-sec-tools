rule _Alpha_BMP_graphics_file_qvaixp
{
	meta:
		description = "Alpha BMP graphics file"
	strings:
		$a = {FFFF000164000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
