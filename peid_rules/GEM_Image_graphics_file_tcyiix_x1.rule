rule _GEM_Image_graphics_file_tcyiix
{
	meta:
		description = "GEM Image graphics file"
	strings:
		$a = {0001000800040002}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
