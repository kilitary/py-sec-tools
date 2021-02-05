rule _Trilobyte_s_JPEG_graphics_Library_dtrqqw
{
	meta:
		description = "Trilobyte_s JPEG graphics Library"
	strings:
		$a = {8410FFFFFFFF1E000110080000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
