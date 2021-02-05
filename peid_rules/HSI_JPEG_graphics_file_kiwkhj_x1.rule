rule _HSI_JPEG_graphics_file_kiwkhj
{
	meta:
		description = "HSI JPEG graphics file"
	strings:
		$a = {687369310000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
