rule _PDS_graphics_file_format_irlyqm
{
	meta:
		description = "PDS graphics file format"
	strings:
		$a = {494D4147454944454E54494649455220}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
