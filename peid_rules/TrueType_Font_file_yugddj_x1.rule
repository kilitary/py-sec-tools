rule _TrueType_Font_file_yugddj
{
	meta:
		description = "TrueType Font file"
	strings:
		$a = {00010000????????????????4C545348}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
