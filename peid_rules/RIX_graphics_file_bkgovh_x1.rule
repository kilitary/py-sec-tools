rule _RIX_graphics_file_bkgovh
{
	meta:
		description = "RIX graphics file"
	strings:
		$a = {52495833}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
