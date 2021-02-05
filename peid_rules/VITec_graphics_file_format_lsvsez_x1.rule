rule _VITec_graphics_file_format_lsvsez
{
	meta:
		description = "VITec graphics file format"
	strings:
		$a = {005B07200000002C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
