rule _IBM_PictureMaker_graphics_file_yrowtr
{
	meta:
		description = "IBM PictureMaker graphics file"
	strings:
		$a = {00??C1??00????????020001}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
