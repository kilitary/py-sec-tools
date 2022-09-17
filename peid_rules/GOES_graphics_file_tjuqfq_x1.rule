rule _GOES_graphics_file_tjuqfq
{
	meta:
		description = "GOES graphics file"
	strings:
		$a = {C8C4D940C1D9C5C1}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
