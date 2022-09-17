rule _XWD_graphics_format_pnmujm
{
	meta:
		description = "XWD graphics format"
	strings:
		$a = {000000710000000700000002000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
