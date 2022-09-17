rule _Sun_Raster_Graphics_format_frcarx
{
	meta:
		description = "Sun Raster Graphics format"
	strings:
		$a = {59A66A95}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
