rule _BAFF_BMP_s_graphics_library_nuelxm
{
	meta:
		description = "BAFF _BMP_s_ graphics library"
	strings:
		$a = {4241464601000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
