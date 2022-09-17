rule _PCPaintPictor_graphics_file_format_fnprrz
{
	meta:
		description = "PCPaintPictor graphics file format"
	strings:
		$a = {3412????????0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
