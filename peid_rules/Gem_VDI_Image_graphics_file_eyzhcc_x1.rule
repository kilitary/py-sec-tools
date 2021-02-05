rule _Gem_VDI_Image_graphics_file_eyzhcc
{
	meta:
		description = "Gem VDI Image graphics file"
	strings:
		$a = {000100??00??0001}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
