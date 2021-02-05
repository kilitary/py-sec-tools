rule _JPEG__GIF_library_file_piolhl
{
	meta:
		description = "JPEG _ GIF library file"
	strings:
		$a = {0005160700020000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
