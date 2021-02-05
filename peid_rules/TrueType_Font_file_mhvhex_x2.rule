rule _TrueType_Font_file_mhvhex
{
	meta:
		description = "TrueType Font file"
	strings:
		$a = {00010000????????????????4F532F32}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
