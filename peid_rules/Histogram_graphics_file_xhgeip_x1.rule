rule _Histogram_graphics_file_xhgeip
{
	meta:
		description = "Histogram graphics file"
	strings:
		$a = {6D6877616E68000401020102}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
