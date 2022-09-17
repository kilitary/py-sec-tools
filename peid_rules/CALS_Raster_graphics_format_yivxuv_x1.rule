rule _CALS_Raster_graphics_format_yivxuv
{
	meta:
		description = "CALS Raster graphics format"
	strings:
		$a = {737263646F6369643A20}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
